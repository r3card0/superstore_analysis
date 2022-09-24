import pandas as pd
from openpyxl.workbook import workbook
import matplotlib.pyplot as plt
from df_copy import copy

df = copy()

# 01 create a dataframe with 'Category' and 'Sales' columns
def cat_sal_cols():
    df1 = df[['Category','Sales']]
    return df1

# global variables
bar_color = ['#ffbf00','#ff033e','#a4c639']
df1 = cat_sal_cols()

# 02 set index to df1 and sum 'Sales' by 'Category'
def group_cat():
    df_grp = df1.groupby('Category').sum().reset_index()
    return df_grp

df2 = group_cat()

# 03 Split by 'Category' and 'Sales'
def category_col():
    category = df2['Category']
    return category

def sales_col():
    sales = df2['Sales']
    return sales

category = category_col()
sales = sales_col()


# 04 create plot
def barplot():
    plt.bar(category,sales,width=0.5,color=bar_color)
    plt.ylabel('Sales $USD')
    plt.xlabel('Category')
    plt.title('Sales by Category')
    #plt.legend('Sales')
    plt.show()


def run():
    print(barplot())

if __name__ == "__main__":
    run()
