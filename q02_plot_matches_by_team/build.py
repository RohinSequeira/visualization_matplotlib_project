import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    data = ipl_df.groupby(['batting_team'])['match_code'].agg('nunique')
    data.plot(kind='bar')
    plt.show()
