import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

df = pd.read_csv('databases/FINAL DATASET.csv')

# Drop rows with infinite or NaN values from the selected columns
df_cleaned = df.replace([np.inf, -np.inf], np.nan).dropna()

# Extract the cleaned columns
a = df_cleaned['HDI 2013']
b = df_cleaned['GDI 2015']
c = df_cleaned['GII 2015']
x = df_cleaned['suicides/100k male']
y = df_cleaned['suicides/100k female']
z = df_cleaned['Suicide Ratio (M/F)']

# Calculate correlation using Pearson's correlation coefficient
hdi_gdi_p, _ = pearsonr(a,b)
hdi_gii_p, _ = pearsonr(a,c)
gdi_gii_p, _ = pearsonr(b,c)

hdi_male_p, _ = pearsonr(a,x)
gdi_male_p, _ = pearsonr(b,x)
gii_male_p, _ = pearsonr(c,x)

hdi_female_p, _ = pearsonr(a,y)
gdi_female_p, _ = pearsonr(b,y)
gii_female_p, _ = pearsonr(c,y)

hdi_ratio_p, _ = pearsonr(a,z)
gdi_ratio_p, _ = pearsonr(b,z)
gii_ratio_p, _ = pearsonr(c,z)

print('HDI-GDI Pearson:', hdi_gdi_p)
print('HDI-GII Pearson:', hdi_gii_p)
print('GDI-GII Pearson:', gdi_gii_p)
print('')
print('HDI-MALE SUICIDE Pearson:', hdi_male_p)
print('GDI-MALE SUICIDE Pearson:', gdi_male_p)
print('GII-MALE SUICIDE Pearson:', gii_male_p)
print('')
print('HDI-FEMALE SUICIDE Pearson:', hdi_female_p)
print('GDI-FEMALE SUICIDE Pearson:', gdi_female_p)
print('GII-FEMALE SUICIDE Pearson:', gii_female_p)
print('')
print('HDI-RATIO Pearson:', hdi_ratio_p)
print('GDI-RATIO Pearson:', gdi_ratio_p)
print('GII-RATIO Pearson:', gii_ratio_p)
