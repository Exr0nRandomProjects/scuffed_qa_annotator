import boto3
from datetime import datetime
import json
from time import sleep

from creds import ACCESS_ID, ACCESS_KEY

client = boto3.client(
        'mturk',
        endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com',
        aws_access_key_id=ACCESS_ID,
        aws_secret_access_key=ACCESS_KEY)

html_layout = open('./SentimentQuestion.html', 'r').read()
QUESTION_XML = """<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
        <HTMLContent><![CDATA[{}]]></HTMLContent>
        <FrameHeight>650</FrameHeight>
        </HTMLQuestion>"""
question_xml = QUESTION_XML.format(html_layout)

tweets = ['in science class right now... urgh... stupid project..',
          'hmmm what to have for breaky?... Honey on toast ',
          'Doing home work  x',
          'Headed out of town for a few days. Will miss my girls']

TaskAttributes = {
    'MaxAssignments': 5,
    # How long the task will be available on MTurk (1 hour)
    'LifetimeInSeconds': 60*60,
    # How long Workers have to complete each item (10 minutes)
    'AssignmentDurationInSeconds': 60*10,
    # The reward you will offer Workers for each response
    'Reward': '0.05',
    'Title': 'Provide sentiment for a Tweet',
    'Keywords': 'sentiment, tweet',
    'Description': 'Rate the sentiment of a tweet on a scale of 1 to 10.'
}

results = []
hit_type_id = ''
for tweet in tweets:
    response = client.create_hit(
        **TaskAttributes,
        Question=question_xml.replace('${content}',tweet)
    )
    hit_type_id = response['HIT']['HITTypeId']
    results.append({
        'tweet': tweet,
        'hit_id': response['HIT']['HITId']
    })

print("You can view the HITs here:")
# print(mturk_environment['preview']+"?groupId={}".format(hit_type_id))
print(f"https://workersandbox.mturk.com/mturk/preview?groupId={hit_type_id}")

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
    print(json.dumps(results,indent=2))

    print(datetime.now(), end="\n\n")
    sleep(60)

