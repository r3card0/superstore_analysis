import pandas as pd
from openpyxl.workbook import workbook
from readfile import readfile

df_read = readfile()

def read_columns():
    readcolumns = df_read.columns
    return readcolumns

def run():
    print(read_columns())

if __name__ == "__main__":
    run()