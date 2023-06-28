import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

df = pd.read_csv('databases/FINAL DATASET.csv')
print(df)

# Drop rows with infinite or NaN values from the selected columns
df_cleaned = df.replace([np.inf, -np.inf], np.nan).dropna()

# Extract the cleaned columns
a = df_cleaned['HDI 2015']
b = df_cleaned['GDI 2015']
c = df_cleaned['GII 2015']
x = df_cleaned['Average suicide 2013']


# Calculate correlation using Pearson's correlation coefficient
hdi_gdi_p, _ = pearsonr(a,b)
hdi_gii_p, _ = pearsonr(a,c)
gdi_gii_p, _ = pearsonr(b,c)

hdi_p, _ = pearsonr(a,x)
gdi_p, _ = pearsonr(b,x)
gii_p, _ = pearsonr(c,x)



print('HDI-GDI Pearson:', hdi_gdi_p)
print('HDI-GII Pearson:', hdi_gii_p)
print('GDI-GII Pearson:', gdi_gii_p)
print('')
print('HDI-SUICIDE Pearson:', hdi_p)
print('GDI-SUICIDE Pearson:', gdi_p)
print('GII-SUICIDE Pearson:', gii_p)

