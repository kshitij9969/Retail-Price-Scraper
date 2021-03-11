import pandas as pd


df = pd.read_csv('Final.csv')

# print(df['Retail Price'].isna().sum())
# print(len(df))

print(df['Retail Price'].isnull().sum())



