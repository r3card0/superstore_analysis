import pandas as pd
from openpyxl.workbook import workbook
from readfile import readfile

df_read = readfile()

# create a copy of dataframe
def copy():
    df_copy = df_read.copy(deep=True)
    return df_copy

def run():
    print(copy().head(3))

if __name__ == "__main__":
    run()