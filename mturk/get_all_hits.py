from creds import ACCESS_ID, ACCESS_KEY

import json
import boto3
import xmltodict
from datetime import datetime
from tqdm import tqdm

client = boto3.client(
        'mturk',
        endpoint_url='https://mturk-requester.us-east-1.amazonaws.com',
        aws_access_key_id=ACCESS_ID,
        aws_secret_access_key=ACCESS_KEY)

results = []
next_page = None
while True:
    got = client.list_hits(MaxResults=100, NextToken=next_page) if next_page else client.list_hits(MaxResults=100)
    results += got['HITs']
    if 'NextToken' in got:
        next_page = got['NextToken']

    print(len(results))
    if got['NumResults'] == 0:
        break

for item in tqdm(results):
    # Get the status of the HIT
    hit = client.get_hit(HITId=item['HITId'])
    item['status'] = hit['HIT']['HITStatus']
    # Get a list of the Assignments that have been submitted
    assignmentsList = client.list_assignments_for_hit(
        HITId=item['HITId'],
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

        # # Approve the Assignment (if it hasn't been already)
        # if assignment['AssignmentStatus'] == 'Submitted':
        #     client.approve_assignment(
        #         AssignmentId=assignment_id,
        #         OverrideRejection=False
        #     )

    # Add the answers that have been retrieved for this item
    item['answers'] = answers
    if len(answers) > 0:
        item['avg_answer'] = sum(answers)/len(answers)

for item in results:
    if 'avg_answer' in item:
        print(item['avg_answer'], item['answers'])
    else:
        print(item)

print(datetime.now(), end="\n\n")


