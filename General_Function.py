import pandas as pd
import numpy as np

def basic_explore (df):
#This function is used for basic data exploration for any dataset
    print("Rows: {}, Cols: {}".format(str(df.shape[0]), str(df.shape[1])))
    print('='*100)
    print(df.info())
    print('='*100)
    print("Decriptive stats for numeric columns")
    print(df.describe())
    print('='*100)
    print("Descriptive Statistics for all columns:")
    print(df.describe(include='object'))
    print('='*100)
    print("Description for categorical cols")
    print(df.describe(include='object'))
    print("Non Null Columns and Counts:")
    null_df = pd.DataFrame(df.isnull().sum())
    null_df.columns = ['Count']
    null_df[null_df['Count']>0]
    df_num = df.select_dtypes(exclude='object')
    df_num_cols = df_num.columns
    for c in df_num_cols:
          print(c)
          print(iqr_outlier(df[c])) 

def iqr_outlier(array):
    a = np.nanpercentile(array, 75)
    b = np.nanpercentile(array, 25)
    iqr = a - b
    ub = a +(iqr*1.5)
    lb = b -(iqr*1.5)
    return [i for i in array if i>ub or i<lb] 

titanic = pd.read_csv('D:\\Titanic\\titanic.csv')

basic_explore(titanic)

#mall_data = pd.read_csv('D:\\Titanic\\mall_data.txt')

#basic_explore(mall_data)

if __name__ == "__main__":
    print(basic_explore(titanic))
    
