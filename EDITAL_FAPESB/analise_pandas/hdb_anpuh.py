# script to analyze the data from the HDB-ANPUH

import pandas as pd
import plotly.graph_objects as go


# function to read the csv from the HDB-ANPUH
def read_csv(path):
    # read the csv
    df = pd.read_csv(path, sep=',', index_col=0)
    return df

path = input("Enter the path to the csv file: ")

df = read_csv(path)

#invert rows and columns
df = df.T

# change the column names
df.columns = ['BIBLIOGRAFIA','DE_IMAGENS', 'DESCRIÇÃO_SUMÁRIA', 'FONTES', 'METODOLOGIA', 'NOTA_DE_RODAPÉ', 'TABELA']

# new dataframe using the last row of the dataframe
df_total = df.iloc[-1]

# create a new dataframe with the values of the last row
df_total = pd.DataFrame(df_total)

#reste index
df_total = df_total.reset_index()

print(df_total)

# rename columns of df_total
df_total.columns = ['Código', 'Citações']
# save the dataframe as csv
df_total.to_csv('hdb_anpuh_total.csv', sep=',', index=False)
