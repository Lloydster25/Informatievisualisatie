import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Read the dataset from the CSV file
df = pd.read_csv('docs/databases/MAIN DATASET.csv')
print(df)


# Drop rows with infinite or NaN values from the selected columns
df_cleaned = df.replace([np.inf, -np.inf], np.nan).dropna()

# Extract the cleaned columns
a = df_cleaned['HDI 2015']
b = df_cleaned['GDI 2015']
c = df_cleaned['Average suicide 2015']
x = df_cleaned['political_violence']
y = df_cleaned['democracy']



# Calculate correlation using Pearson's correlation coefficient
hdi_gdi_p, _ = pearsonr(a, b)
hdi_pv_p, _ = pearsonr(a,x)
hdi_dem_p, _ = pearsonr(a,y)
sui_dem_p, _ = pearsonr(c,y)

print('HDI-GDI Pearson:', hdi_gdi_p)
print('HDI-Political Violence:', hdi_pv_p)
print('HDI-Democracy:', hdi_dem_p)
print('SUICIDE-Democracy:', sui_dem_p)