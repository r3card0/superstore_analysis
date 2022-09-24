import pandas as pd
from openpyxl.workbook import workbook

def readfile():
    df_read = pd.read_excel('/Users/ideasleon/platzi_edu/Tableau/learn/sample-superstore.xls')
    return df_read

def readhead():
    df_head = readfile().head(5)
    return df_head

def run():
    print(readhead())


if __name__ == '__main__':
    run()