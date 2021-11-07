from creds import ACCESS_ID, ACCESS_KEY

import json
import boto3
import xmltodict
from datetime import datetime
from tqdm import tqdm
from bs4 import BeautifulSoup
import lxml
import pandas

client = boto3.client(
        'mturk',
        endpoint_url='https://mturk-requester.us-east-1.amazonaws.com',
        aws_access_key_id=ACCESS_ID,
        aws_secret_access_key=ACCESS_KEY)

results = []
next_page = None
while True:
    got = client.list_hits(MaxResults=100, NextToken=next_page) if next_page else client.list_hits(MaxResults=10)
    results += got['HITs']
    if 'NextToken' in got:
        next_page = got['NextToken']

    print(len(results))
    if got['NumResults'] == 0:
        break
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

original_data = pandas.read_csv('data.tsv', delimiter='	', names=['id', 'context', 'question', 'model_answer', 'gold_answers'])
new_data = pandas.DataFrame(columns=['question', 'mturk_scores', 'avg_score'])
for item in results:
    # soup = BeautifulSoup(item['Question'], 'html.parser')
    soup = BeautifulSoup(item['Question'], 'lxml')
    qap_raw = [x.next_sibling.contents[0] for x in soup.find_all("td", { 'class': "text-gray-600" })]

    data_row = original_data[original_data['question'] == qap_raw[0]]

    assert len(data_row) == 1
    assert 'avg_answer' in item

    new_data = new_data.append({ 'question': data_row['question'], 'mturk_scores': tuple(item['answers']), 'avg_score': item['avg_answer'] }, ignore_index=True)

print(new_data)
combo_data = original_data.merge(new_data, how='left', on='question')
print(combo_data)
# print(combo_data[~combo_data['mturk_scores'].isna()])

print(datetime.now(), end="\n\n")


