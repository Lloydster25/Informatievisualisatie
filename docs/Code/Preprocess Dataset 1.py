import pandas as pd
import numpy as np

df1 = pd.read_csv('docs/databases/DATABASE 1.csv')
df1 = df1[['Country','Human Development Index (HDI)']]
df2 = pd.read_csv('docs/databases/DATABASE 2.csv')
df2 = df2[['Country','Gender Development Index (GDI)']]
df3 = pd.read_csv('docs/databases/DATABASE 3.csv')
df3 = df3[['Country', '2015']]
df3 = df3.rename(columns={'2015': 'Average suicide 2015'})

df = pd.merge(df1, df2, on='Country')
df = pd.merge(df, df3, on='Country')
df = df.rename(columns={'Gender Development Index (GDI)': 'GDI 2015', 'Human Development Index (HDI)': 'HDI 2015'})
df = df.replace('..', np.nan).dropna()
df.to_csv('docs/databases/IV DATASET 1.csv', index=False)

print(df)