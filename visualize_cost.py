import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pprint import pprint

def visualize_cost(filename):
    '''
    1. dataframe komt binnen (kosten, battrijpositie)
    2. dataframe ascending order
    3. visualiseer

    '''

    df = pd.read_csv(filename, sep=',')

    # sort with cost ascending
    sorted_df = df.sort_values(by='Costs')
    pprint(sorted_df)

    # # get the minimumcost
    # min_index = df.idxmin()

    # visualise the cost
    sns.catplot(data=sorted_df, x='Experiment', y='Costs', kind='bar')
    plt.title('Experiment Costs', loc='center')
    # plt.bar(min_index, df[min_index], color='red')
    # plt.legend('hai')
    plt.show()
