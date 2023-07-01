import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('docs/databases/Age-standardized suicide rates.csv')
df1 = pd.read_csv('docs/databases/IV DATASET 1.csv')
df1 = df1[['Country', 'GDI 2015', 'HDI 2015']]
df = pd.merge(df, df1, on='Country')

df['Sex'] = df['Sex'].str.replace('female', 'F').str.replace('male', 'M')

female_suicides = df[df['Sex'].str.contains('fem', case=False)]
male_suicides = df[df['Sex'].str.contains('male', case=False)]

print(female_suicides)
print(male_suicides)
female_suicides.to_csv('docs/databases/female_suicides.csv')
male_suicides.to_csv('docs/databases/male_suicides.csv')