import pandas as pd
import numpy as np

df1 = pd.read_csv('docs/databases/IV DATASET 1.csv')
df2 = pd.read_csv('docs/databases/IV DATASET 3.csv')
df2 = df2.drop('Unnamed: 0', axis=1)
print(df2)
df = pd.merge(df1, df2, on='Country')
print(df)
df.to_csv('docs/databases/FINAL DATASET.csv')
