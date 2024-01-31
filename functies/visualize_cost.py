import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pprint import pprint

def visualize_cost(input_filename, output_filename):
    ''' Visualize the cost with a histogram that counts how many times they appear'''

    df = pd.read_csv(input_filename, sep=',')

    plt.hist(df['Costs'], bins=100)
    plt.xlabel("Costs")
    plt.ylabel("Count")
    plt.title("Experiment Costs")

    # Save the plot to a file
    plt.savefig(output_filename)
    plt.show()
