import pandas as pd
from openpyxl.workbook import workbook
from df_copy import copy

df = copy()

# select columns 'Category' and 'Sales'
def category_col():
    category = df['Category']
    return category

def sales_col():
    sales = df['Sales']
    return sales

def run():
    print(df)

if __name__ == "__main__":
    run()
