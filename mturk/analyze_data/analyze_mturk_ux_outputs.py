import pandas as pd

FILENAMES = ['triple_batch.csv', 'second_time.csv']

# read all data
info_dataframes = []
for file in FILENAMES:
    df = pd.read_csv(file)
    df = df[['Input.qap_question', 'Input.qap_modelans', 'Input.qap_goldans', 'Input.qap_context', 'Input.qap_id', 'Answer.sentiment.label', 'WorkerId']]
    info_dataframes.append(df)

# calculate overlap statistics
all_dfs = pd.concat(info_dataframes)
all_dfs = all_dfs.reset_index(drop=True)
grouped = all_dfs.groupby('Input.qap_id')
grouped = grouped.agg({'WorkerId': 'nunique'})
grouped = grouped[grouped['WorkerId'] == 3]
# all_dfs = all_dfs.sort_values(by=['Input.qap_id'])
# print(all_dfs)
print(grouped)
