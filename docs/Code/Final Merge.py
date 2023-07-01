import pandas as pd

df1 = pd.read_csv('docs/databases/IV DATASET 1.csv')
df2 = pd.read_csv('docs/databases/IV DATASET 4.csv')

df = pd.merge(df1, df2, on='Country')
print(df)
df.to_csv('docs/databases/MAIN DATASET.csv')
