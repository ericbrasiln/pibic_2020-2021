import pandas as pd
import plotly.graph_objects as go


# function to read the csv from the HDB-ANPUH
def read_csv(path):
    # read the csv
    df = pd.read_csv(path, sep=',', index_col=0)
    return df

path = input("Enter the path to the csv file: ")

df = read_csv(path)

df = df.reset_index()

# rename the old index
df.rename(columns={'index': 'Categoria'}, inplace=True)

print(df)
# plot the graph
