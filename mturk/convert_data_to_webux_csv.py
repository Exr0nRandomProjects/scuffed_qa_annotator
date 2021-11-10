import csv
from tqdm import tqdm

with open('data.tsv', 'r') as csv_rf:
    reader = csv.reader(csv_rf, delimiter="	")
    qaps = [row for row in reader]

print('creating HITs...')
with open('csv_for_mturkux.csv', 'w') as wf:
    writer = csv.writer(wf)
    writer.writerow(['qap_question', 'qap_modelans', 'qap_goldans', 'qap_context', 'qap_id'])
    for qid, context, question, m_answer, g_answers in tqdm(qaps):
        writer.writerow([question, m_answer, g_answers, context, qid])

