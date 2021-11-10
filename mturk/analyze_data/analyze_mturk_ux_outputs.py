import pandas as pd

# FILENAMES = ['triple_batch.csv', 'second_time.csv']
FILENAMES = ['triple_batch.csv']

LABELS = { "Definetly incorrect": 1, "I dont think its correct": 2, "Unsure": 3, "I think its correct": 4, "Definitely correct": 5  }

# read all data
info_dataframes = []
for file in FILENAMES:
    df = pd.read_csv(file)
    df = df[['Input.qap_question', 'Input.qap_modelans', 'Input.qap_goldans', 'Input.qap_context', 'Input.qap_id', 'Answer.sentiment.label', 'WorkerId']]
    info_dataframes.append(df)

# calculate overlap statistics
all_dfs = pd.concat(info_dataframes)
all_dfs = all_dfs.reset_index(drop=True)
all_dfs['worker_score'] = all_dfs['Answer.sentiment.label'].map(LABELS)
print(all_dfs['Answer.sentiment.label'])
grouped = all_dfs.groupby('Input.qap_id')
# print(grouped['worker_score'].range())
# print(grouped['worker_score'].std())
# all_dfs = all_dfs.sort_values(by=['Input.qap_id'])
# print(all_dfs)
# print(grouped)
