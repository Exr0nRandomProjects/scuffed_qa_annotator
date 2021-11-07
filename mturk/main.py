import boto3
from datetime import datetime
import json
from time import sleep
import xmltodict
import csv
from tqdm import tqdm

from creds import ACCESS_ID, ACCESS_KEY

client = boto3.client(
        'mturk',
        # endpoint_url='https://mturk-requester.us-east-1.amazonaws.com',
        endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com',
        aws_access_key_id=ACCESS_ID,
        aws_secret_access_key=ACCESS_KEY)

html_layout = open('./SentimentQuestion.html', 'r').read()
QUESTION_XML = """<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
        <HTMLContent><![CDATA[{}]]></HTMLContent>
        <FrameHeight>650</FrameHeight>
        </HTMLQuestion>"""
question_xml = QUESTION_XML.format(html_layout)

TaskAttributes = {
    'MaxAssignments': 1,
    # How long the task will be available on MTurk (1 hour)
    'LifetimeInSeconds': 60*60*48,
    # 'LifetimeInSeconds': 60*5,
    # How long Workers have to complete each item (10 minutes)
    'AssignmentDurationInSeconds': 60*10,
    # The reward you will offer Workers for each response
    'Reward': '0.05',
    'Title': 'Compare trivia questions and answers!',
    'Keywords': 'question answering',
    'Description': 'Rate the correctness of a trivia answer on a scale of 1 to 5.'
}

question_template = '''
<table class="m-auto text-mono">
<tr><td class="text-gray-600">question</td><td class='max-w-prose p-4'>{}</td></tr>
<tr><td class="text-gray-600">submitted answer</td><td class='max-w-prose p-4'>{}</td></tr>
<tr><td class="text-gray-600">correct answers</td><td class='max-w-prose p-4'>{}</td></tr>
<tr><td class="text-gray-600">context</td><td class='max-w-prose p-4'>{}</td></tr>
</table>
'''

results = []
hit_type_id = ''
# for tweet in tweets:

with open('data.tsv', 'r') as csv_rf:
    reader = csv.reader(csv_rf, delimiter="	")
    qaps = [row for row in reader]

print('creating HITs...')
for qid, context, question, m_answer, g_answers in tqdm(qaps):
    # print(question_template.format(question, m_answer, g_answers, context))
    response = client.create_hit(
        **TaskAttributes,
        Question=question_xml.replace("${content}", question_template.format(question, m_answer, g_answers, context))
    )
    hit_type_id = response['HIT']['HITTypeId']
    results.append({
        'data': (qid, context, question, m_answer, g_answers),
        'hit_id': response['HIT']['HITId']
    })

print("You can view the HITs here:")
# print(mturk_environment['preview']+"?groupId={}".format(hit_type_id))
print(f"https://workersandbox.mturk.com/mturk/preview?groupId={hit_type_id}")

with open(f"out/results_{datetime.now()}_log.txt", "w") as wf:
    while True:
        for item in results:

            # Get the status of the HIT
            hit = client.get_hit(HITId=item['hit_id'])
            item['status'] = hit['HIT']['HITStatus']
            # Get a list of the Assignments that have been submitted
            assignmentsList = client.list_assignments_for_hit(
                HITId=item['hit_id'],
                AssignmentStatuses=['Submitted', 'Approved'],
                MaxResults=10
            )
            assignments = assignmentsList['Assignments']
            item['assignments_submitted_count'] = len(assignments)
            answers = []
            for assignment in assignments:

                # Retreive the attributes for each Assignment
                worker_id = assignment['WorkerId']
                assignment_id = assignment['AssignmentId']

                # Retrieve the value submitted by the Worker from the XML
                answer_dict = xmltodict.parse(assignment['Answer'])
                answer = answer_dict['QuestionFormAnswers']['Answer']['FreeText']
                answers.append(int(answer))

                # Approve the Assignment (if it hasn't been already)
                if assignment['AssignmentStatus'] == 'Submitted':
                    client.approve_assignment(
                        AssignmentId=assignment_id,
                        OverrideRejection=False
                    )

            # Add the answers that have been retrieved for this item
            item['answers'] = answers
            if len(answers) > 0:
                item['avg_answer'] = sum(answers)/len(answers)

        wf.write(json.dumps(results) + str(datetime.now()) + '\n')

        print(json.dumps(results,indent=2))

        print(datetime.now(), end="\n\n")
        sleep(60)

