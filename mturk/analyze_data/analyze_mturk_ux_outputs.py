import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.stats.inter_rater import fleiss_kappa
from copy import deepcopy

# FILENAMES = ['triple_batch.csv', 'second_time.csv']
DATASET_FILE, FILENAMES = 'sampled_fails_500.csv', ['triple_batch.csv']
RUNS = ['bert_large:squad', 'bert_large:nq_closed']

LABELS = { "Definetly incorrect": -3, "I dont think its correct": -2, "Unsure": 0, "I think its correct": 2, "Definitely correct": 3  }
LABELS_LINEAR = { "Definetly incorrect": 1, "I dont think its correct": 2, "Unsure": 3, "I think its correct": 4, "Definitely correct": 5  }

# read all data
info_dataframes = []
for file in FILENAMES:
    df = pd.read_csv(file)
    df = df[['Input.qap_question', 'Input.qap_modelans', 'Input.qap_goldans', 'Input.qap_context', 'Input.qap_id', 'Answer.sentiment.label', 'WorkerId']]
    info_dataframes.append(df)

# calculate overlap statistics
all_dfs = pd.concat(info_dataframes)

data = pd.read_csv(DATASET_FILE)
data = data[data['run'].isin(RUNS)]
run_names = [data[data['id'] == id]['run'].array[0] for id in all_dfs['Input.qap_id']]
all_dfs['run'] = run_names

# all_dfs = all_dfs.reset_index(drop=True)
all_dfs = all_dfs.set_index(['run', 'Input.qap_id'])

pure_df = deepcopy(all_dfs)
all_dfs['worker_score'] = all_dfs['Answer.sentiment.label'].map(LABELS)
grouped = all_dfs.groupby('Input.qap_id')
# plt.hist(grouped['worker_score'].agg(sum).apply(abs), bins=range(7))
if __name__ == '__main__':
    # chart agreements
    agreements = grouped['worker_score'].agg(sum).apply(abs)
    agreements = pd.DataFrame(agreements).groupby('worker_score').size()
    plt.bar(agreements.index, agreements)   # DOC: why did we choose these weights for agreement? well, two "probably nots" should be more than one "definitely yes" and so on. these encode the meaning of the phrase
    plt.savefig('annotation_agreement.png')

    def show_fleiss_kappa(fleiss_df, name='all'):
    # Fleiss's Kappa
        fleiss_df['worker_score'] = fleiss_df['Answer.sentiment.label'].map(LABELS_LINEAR)
        # fleiss_df = fleiss_df[fleiss_df['worker_score'] != 3] # filter out unsures
        fleiss_group = fleiss_df.groupby('Input.qap_id')
        # fleiss_table = fleiss_group['worker_score'].value_counts(bins=list(range(0, 6)), sort=False)
        fleiss_table = fleiss_group['worker_score'].value_counts(bins=[0, 3, 6], sort=False)
        if True:
            # flatten the fleiss table, as per https://stackoverflow.com/a/35049899/10372825
            # create an empty array of NaN of the right dimensions
            shape = map(len, fleiss_table.index.levels)
            arr = np.full(tuple(shape), 0)

            # fill it using Numpy's advanced indexing
            arr[tuple(fleiss_table.index.codes)] = fleiss_table.values.flat

        # print(fleiss_table, type(fleiss_table))
        # print('epic')
        print(f"fleiss_kappa ({name}):", fleiss_kappa(arr))

    show_fleiss_kappa(deepcopy(pure_df))
    for run in RUNS:
        df = deepcopy(pure_df)
        df = df.loc[[run]]
        show_fleiss_kappa(df, name=run)

    # generate the manual analysis file
    labeled_truths = grouped.agg(sum).apply(lambda score: score > 0)
    num_truths = len(labeled_truths[labeled_truths['worker_score']])
    print("Number of false negatives by EM:", num_truths, f"({num_truths/len(labeled_truths)*100:.2f}%)")
    labeled_truths.insert(0, 'failure mode', ['unknown']*len(labeled_truths))
    labeled_truths.index.names = ['id']
    labeled_truths.to_csv(f"analyzed_fails_{len(labeled_truths)}.tsv", sep="	", header=True)
