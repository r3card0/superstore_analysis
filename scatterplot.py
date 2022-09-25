import pandas as pd
from openpyxl.workbook import workbook
import matplotlib.pyplot as plt
import seaborn as sns
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

# 02 Split by 'Profit' and 'Sales'
def profit_col():
    profit = df1['Profit']
    return profit

def sales_col():
    sales = df1['Sales']
    return sales

profit = profit_col()
sales = sales_col()

# 03 Create scatterplot
def scatterplot():
    sns.scatterplot(data=df, x='Profit', y='Sales', hue='Order Date')
    plt.show()

def run():
    print(scatterplot())

if __name__ == "__main__":
    run()