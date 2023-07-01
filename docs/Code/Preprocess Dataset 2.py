import pandas as pd

df = pd.read_csv('databases/suiciderateall.csv')
df_restructured = df.melt(id_vars='Country', var_name='Year', value_name='Suicides/100k')

# Sort the DataFrame by Country and Year
df_restructured = df_restructured.sort_values(['Country', 'Year']).reset_index(drop=True)

df_restructured.to_csv('databases/IV DATASET 2.csv')
print(df_restructured)