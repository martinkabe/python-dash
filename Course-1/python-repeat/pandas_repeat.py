import pandas as pd
import numpy as np


df = pd.read_csv('./data/salaries.csv')
print(df[['Name','Salary']])

ser_of_bool = df['Age'] > 30
print(df[ser_of_bool])

print(df.info())

print(df.describe())
print(df.index)


mat = np.arange(0,10).reshape(5,2)
df_mat = pd.DataFrame(mat, columns=['A','B'])
print(df_mat)
