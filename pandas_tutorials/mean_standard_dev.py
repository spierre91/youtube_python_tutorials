import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")

del df['Unnamed: 0']

print(df.head())

print(list(df.columns))

def get_statistics(numerical_column):
    print(f'Mean of {numerical_column}: ', df['IMDb'].mean())
    print(f'Standard Deviation of {numerical_column}: ', df['IMDb'].std())

get_statistics('IMDb')

get_statistics('Runtime')
