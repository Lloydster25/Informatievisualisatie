import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Read the dataset from the CSV file
df = pd.read_csv('docs/databases/FINAL DATASET.csv')

# Drop rows with infinite or NaN values from the selected columns
df_cleaned = df.replace([np.inf, -np.inf], np.nan).dropna()

# Extract the cleaned columns
a = df_cleaned['HDI 2015']
b = df_cleaned['GDI 2015']
x = df_cleaned['Average suicide 2015']

# Calculate correlation using Pearson's correlation coefficient
hdi_gdi_p, _ = pearsonr(a, b)
hdi_suicide_p, _ = pearsonr(a, x)
gdi_suicide_p, _ = pearsonr(b, x)

print('HDI-GDI Pearson:', hdi_gdi_p)
print('HDI-Suicide Pearson:', hdi_suicide_p)
print('GDI-Suicide Pearson:', gdi_suicide_p)
