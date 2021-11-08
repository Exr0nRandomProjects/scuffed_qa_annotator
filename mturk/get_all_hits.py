from creds import ACCESS_ID, ACCESS_KEY

import json
import boto3
import xmltodict
from datetime import datetime
from tqdm import tqdm
from bs4 import BeautifulSoup
import lxml
import pandas as pd

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

        # Approve the Assignment (if it hasn't been already)
        if assignment['AssignmentStatus'] == 'Submitted':
            client.reject_assignment(
                AssignmentId=assignment_id,
                OverrideRejection=False
            )

    # Add the answers that have been retrieved for this item
    item['answers'] = answers
    if len(answers) > 0:
        item['avg_answer'] = sum(answers)/len(answers)

exit()

original_data = pd.read_csv('data.tsv', delimiter='	', names=['id', 'context', 'question', 'model_answer', 'gold_answers'])
original_data['mturk_scores'] = [[]] * len(original_data)
original_data['avg_score'] = [0] * len(original_data)
original_data['mturk_scores'] = original_data['mturk_scores'].astype(object)
print(original_data)
print(original_data['mturk_scores'])
for item in results:
    soup = BeautifulSoup(item['Question'], 'lxml')
    qap_raw = [x.next_sibling.contents[0] for x in soup.find_all("td", { 'class': "text-gray-600" })]

    data_row = original_data[original_data['question'] == qap_raw[0]]

    assert len(data_row) == 1
    assert 'avg_answer' in item

    original_data.loc[data_row.index, 'mturk_scores'] = pd.Series([item['answers']], index=data_row.index, dtype=object)
    original_data.loc[data_row.index, 'avg_score'] = item['avg_answer']

# print(original_data[original_data['mturk_scores'].map(print) > 0])
# print(original_data[original_data['mturk_scores'].map(len) > 0])

print(original_data)
original_data.to_csv('mturk_round_1.tsv', sep='	')

print(datetime.now(), end="\n\n")


