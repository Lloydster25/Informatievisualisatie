import pandas as pd
import numpy as np

df1 = pd.read_csv('databases/IV DATASET 1.csv')

print(df1)

df1.to_csv('databases/FINAL DATASET.csv')
