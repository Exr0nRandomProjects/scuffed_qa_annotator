import pandas as pd
from matplotlib import pyplot as plt

# FILENAMES = ['triple_batch.csv', 'second_time.csv']
FILENAMES = ['triple_batch.csv']

LABELS = { "Definetly incorrect": -3, "I dont think its correct": -2, "Unsure": 0, "I think its correct": 2, "Definitely correct": 3  }

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
grouped = all_dfs.groupby('Input.qap_id')
# plt.hist(grouped['worker_score'].agg(sum).apply(abs), bins=range(7))
if __name__ == '__main__':
    agreements = grouped['worker_score'].agg(sum).apply(abs)
    agreements = pd.DataFrame(agreements).groupby('worker_score').size()
    plt.bar(agreements.index, agreements)   # DOC: why did we choose these weights for agreement? well, two "probably nots" should be more than one "definitely yes" and so on. these encode the meaning of the phrase
    plt.savefig('annotation_agreement.png')

    # generate the manual analysis file
    labeled_truths = grouped.agg(sum).apply(lambda score: score > 0)
    num_truths = len(labeled_truths[labeled_truths['worker_score']])
    print("Number of false negatives by EM:", num_truths, f"({num_truths/len(labeled_truths)*100:.2f}%)")
    labeled_truths.insert(0, 'failure mode', ['unknown']*len(labeled_truths))
    labeled_truths.index.names = ['id']
    labeled_truths.to_csv(f"analyzed_fails_{len(labeled_truths)}.tsv", sep="	", header=True)
