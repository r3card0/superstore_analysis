import pandas as pd
from openpyxl.workbook import workbook
from readfile import readfile

df_read = readfile()

def run():
    print(df_read.head(5))

if __name__ == "__main__":
    run()