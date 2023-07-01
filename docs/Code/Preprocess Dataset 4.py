import pandas as pd

df = pd.read_csv('docs/databases/DATABASE 5.csv')
print(df)
df = df[['country', 'year', 'gov_democracy', 'government', 'political_violence']]

# Rename Countries'
df['country'] = df['country'].replace('Russia', 'Russian Federation')
df['country'] = df['country'].replace('USA', 'United States')
df['country'] = df['country'].replace('UKG', 'United Kingdom')
df['country'] = df['country'].replace('Congo-Brz', 'Congo')
df['country'] = df['country'].replace('St.Lucia', 'Saint Lucia')
df['country'] = df['country'].replace('Dominican Rep', 'Dominican Republic')
df['country'] = df['country'].replace('Central African Rep', 'Central African Republic')
print(df)
# Filter for the most recent year for each country
df_most_recent = df.groupby('country')['year'].max().reset_index()

# Merge the most recent year with the original DataFrame to get the corresponding government type
df = pd.merge(df_most_recent, df, on=['country', 'year'], how='left').drop_duplicates(subset=('country'))
print(df)
df = df.rename(columns={'country': 'Country', 'gov_democracy': 'democracy'})
df = df[['Country', 'democracy', 'government', 'political_violence']]
df.to_csv('docs/databases/IV DATASET 4.csv', index=False)
print(df)
