import pandas as pd
from openpyxl.workbook import workbook
import matplotlib.pyplot as plt
from df_copy import copy

df = copy()

# select columns 'Category' and 'Sales'
def category_col():
    category = df['Category']
    return category

def sales_col():
    sales = df['Sales']
    return sales


# create global variables
category = category_col()
sales = sales_col()

# create barplot
def barplot():
    plt.bar(category,sales)
    plt.show()


def run():
    print(barplot())

if __name__ == "__main__":
    run()
