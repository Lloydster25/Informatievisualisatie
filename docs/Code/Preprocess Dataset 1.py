import pandas as pd
import numpy as np

df1 = pd.read_csv('docs/databases/human_development.csv')
df1 = df1[['Country','Human Development Index (HDI)']]
df2 = pd.read_csv('docs/databases/gender_development.csv')
df2 = df2[['Country','Gender Development Index (GDI)']]
df3 = pd.read_csv('docs/databases/suiciderateall.csv')
df3 = df3[['Country', '2015']]
df3 = df3.rename(columns={'2015': 'Average suicide 2015'})

merge = pd.merge(df1, df2, on='Country')
merge = pd.merge(merge, df3, on='Country')
merge = merge.rename(columns={'Gender Development Index (GDI)': 'GDI 2015', 'Human Development Index (HDI)': 'HDI 2015'})
merge = merge.replace('..', np.nan).dropna()
merge.to_csv('docs/databases/IV DATASET 1.csv', index=False)

print(merge) 