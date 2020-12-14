import pandas as pd

df = pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


del df['Unnamed: 0']
print(df.head())


df_2010 = df[df['Year'] == 2010]


print(df_2010.head())


df_english = df[df['Language'] == 'English']

print(df_english.head())


def filter_by_category(column_name, column_value):
    df_new = df[df[f'{column_name}'] == column_value]
    return df_new

df_italian = filter_by_category('Language', 'Italian')

print(df_italian.head())
