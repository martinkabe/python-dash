import pandas as pd
import numpy as np


np.random.seed(101)

mat = np.random.randint(1,101,(100,5))
print(mat)

df = pd.DataFrame(mat)
print(df)


df.columns = 'f1 f2 f3 f4 label'.split()
print(df)

random_numbers = np.random.randint(0,100,(50,4))
col_names = 'A B C D'.split()
df = pd.DataFrame(random_numbers)
df.columns = col_names
print(df)