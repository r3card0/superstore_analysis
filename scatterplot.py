import pandas as pd
from openpyxl.workbook import workbook
import matplotlib.pyplot as plt
import seaborn as np
from df_copy import copy

def description():
    programa_description= """
    This program creates a scatter plot
    """
    return programa_description

df = copy()

# 01 create a dataframe with 'Profit' and 'Sales' columns
def prof_sal_cols():
    df1 = df[['Profit','Sales']]
    return df1

df1 = prof_sal_cols()

def run():
    print(df1)

if __name__ == "__main__":
    run()