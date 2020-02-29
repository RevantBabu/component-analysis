import pandas as pd
import numpy as np

xls = pd.ExcelFile('data_raw/data.xlsx')

df1 = pd.read_excel(xls, "SHAPS", skiprows=2, usecols="A:O", header=None, index_col=0)
df2 = pd.read_excel(xls, "TEPS", skiprows=2, usecols="A:S", header=None, index_col=0)
df3 = pd.read_excel(xls, "Chapman", skiprows=2, usecols="A:BJ", header=None, index_col=0)
df4 = pd.read_excel(xls, "Becu depression", skiprows=2, usecols="A:V", header=None, index_col=0)
df5 = pd.read_excel(xls, "Apathy scale", skiprows=2, usecols="A:S", header=None, index_col=0)

print(df1.shape)
print(df2.shape)
print(df3.shape)
print(df4.shape)
print(df5.shape)

df_conact = pd.concat([df1, df2, df3, df4, df5], axis=1, join='outer')
print("Merged Dataframe size: ", df_conact.shape)

print("Number of nulls: ", df_conact.isnull().sum().sum())
#df.isnull().any(axis=1)
print("List of null indices: ", df_conact[df_conact.isnull().any(axis=1)].index.tolist())

## removing nulls
df_clean = df_conact[df_conact.notnull().all(axis=1)]
print("Dataframe size after removing null rows: ", df_clean.shape)

## two columns had 1a,1b notion, removed for now
df_numeric = df_clean.select_dtypes(include=[np.number])
print("Dataframe size after removing non-numeric columns: ", df_numeric.shape)

## renaming columns
df_numeric.columns = list(range(1,df_numeric.shape[1]+1))

normalized_df_min_max=(df_numeric-df_numeric.min())/(df_numeric.max()-df_numeric.min())
normalized_df_mean=(df_numeric-df_numeric.mean())/(df_numeric.std())

normalized_df_mean.to_csv("data_processed/mean_n.csv")
normalized_df_mean.to_pickle("data_processed/mean_n.pkl")
normalized_df_min_max.to_csv("data_processed/mm_n.csv")
normalized_df_min_max.to_pickle("data_processed/mm_n.pkl")
print("Normalized df using mean_std & min_max and stored in data_processed folder")