import pandas as pd
from openpyxl.workbook import workbook
import matplotlib.pyplot as plt
import seaborn as sns
from df_copy import copy

def description():
    programa_description= """
    This program creates a lineplot
    """
    return programa_description

df = copy()

# Set Order Date as an Index 
def set_time():
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df_time = df.groupby('Order Date').sum()
    return df_time

# Set resample
def time_resample():
    df_time = set_time().resample('Q').sum()
    return df_time

df_time = time_resample()

# 03 Create scatterplot
def lineplot():
    sns.lineplot(data=df_time, x='Order Date', y='Profit')
    plt.show()

def run():
    print(lineplot())

if __name__ == "__main__":
    run()