import pandas as pd
import numpy as np

df1 = pd.read_csv('databases/IV DATASET 1.csv')
df2 = pd.read_csv('databases/IV DATASET 2.csv')
merge = pd.merge(df1, df2, on='Country')
merge['Average Suicide'] = (merge['suicides/100k male'] + merge['suicides/100k female']) / 2
merge.to_csv('databases/FINAL DATASET.csv')


merge['Suicide Ratio (M/F)'] = np.where(merge['suicides/100k female'] != 0,
                                     merge['suicides/100k male'] / merge['suicides/100k female'],
                                     np.nan)


print(merge)

# Calculate the mean of the 'Suicide Ratio (M/F)' column
suicide_ratio_mean = merge['Suicide Ratio (M/F)'].mean()

# Print the mean
print("Mean Suicide Ratio (M/F):", suicide_ratio_mean)
