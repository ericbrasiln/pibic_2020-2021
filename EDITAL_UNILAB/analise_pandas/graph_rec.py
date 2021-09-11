import pandas as pd
import plotly.graph_objects as go

#function to read xlsx into a dataframe
def read_xlsx(path):
    # read the csv
    df = pd.read_excel(path, index_col=0)
    return df

# function to read the csv from the HDB-ANPUH
def read_csv(path):
    # read the csv
    df = pd.read_csv(path, sep=',', index_col=0)
    return df

path = input("Enter the path to the csv file: ")

#df = read_csv(path)
df = read_xlsx(path)

df = df.reset_index()

# rename columns
df.columns = ['CATEGORIA', 'ASPECTO_POLÍTICO', 'CAMPO_DE_PESQUISA_ESTUDO',\
              'CRÍTICA_DO_TERMO', 'DEFINIÇÃO_DO_TERMO', 'EXTINÇÃO_DO_CATIVEIRO',\
              'NOTA_RODAPÉ', 'PERSPECTIVA_COMPARATIVA', 'PERSPECTIVA_TEÓRICA']

# change columns for rows, rename columns
df2 = df.T
df2.columns = df2.iloc[0]

#drop the first row (columns names)
df2 = df2.drop(df2.index[0])

# add new index column and keep the old index
df2.index.name = ''
df2.reset_index(inplace=True)
df2.columns = ['CATEGORIA', 'TEMA_CENTRAL', 'TEMA_INCIDENTAL']

# Colored Horizontal Bar Chart with go.Bar
fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=df2.CATEGORIA,
    y=df2.TEMA_CENTRAL,
    name='TEMA_CENTRAL',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
fig2.add_trace(go.Bar(
    x=df2.CATEGORIA,
    y=df2.TEMA_INCIDENTAL,
    name='TEMA_INCIDENTAL',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))
fig2.update_layout(
    title='TEMAS CENTRAIS E INCIDENTAIS',
    yaxis_title='CITAÇÕES',
    barmode='stack'
)
fig2.show()
# save the graph as html and png
fig2.write_html('bar_analise.html')
fig2.write_image('bar_analise.png')
