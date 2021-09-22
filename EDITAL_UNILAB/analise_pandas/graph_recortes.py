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

# fuction to organize the dataframe
def organize_df(df):
    # invert the dataframe
    df = df.T
    print(df)
    #drop the first row (columns names)
    df = df.drop(df.index[0]) # in graph bar_tem delete this line of code
    df.index.name = ''
    # reset the index and rename the columns
    df = df.reset_index()
    df.columns = ['CÓDIGO', 'TEMA_CENTRAL', 'TEMA_INCIDENTAL']
    return df

#function to create the bar chart
def create_bar_chart(df, title, width, height, output):
    # Colored Horizontal Bar Chart with go.Bar
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df.CÓDIGO,
        y=df.TEMA_CENTRAL,
        name='TEMA_CENTRAL',
        marker=dict(
            color='rgba(246, 78, 139, 0.6)',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        x=df.CÓDIGO,
        y=df.TEMA_INCIDENTAL,
        name='TEMA_INCIDENTAL',
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        )
    ))
    fig.update_layout(
        title=title,
        yaxis_title='CITAÇÕES',
        barmode='stack',
        # size
        width=width,
        height=height
        ),
    fig.show()
    # save the graph as html and png
    fig.write_html(output + '.html')
    fig.write_image(output + '.png')

# fuction to create horizontal bar chart
def create_horizontal_bar_chart(df, title, width, height, output):
    # Colored Horizontal Bar Chart with go.Bar
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df.TEMA_CENTRAL,
        y=df.CÓDIGO,
        name='TEMA_CENTRAL',
        orientation='h',
        marker=dict(
            color='rgba(246, 78, 139, 0.6)',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        x=df.TEMA_INCIDENTAL,
        y=df.CÓDIGO,
        name='TEMA_INCIDENTAL',
        orientation='h',
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        )
    ))
    fig.update_layout(
        title=title,
        xaxis_title='CITAÇÕES',
        barmode='stack',
        # size
        width=width,
        height=height
        ),
    fig.show()
    ## save the graph as html and png
    fig.write_html(output + '.html')
    fig.write_image(output + '.png')

# xlsx 'TEMAxANALISE'
df_analise = read_xlsx('/home/ebn/Documentos/Github/development/pibic_2020-2021/EDITAL_UNILAB/ATLAS/COOC_TEMAxANÁLISE.xlsx')
df_analise = df_analise.reset_index()
# rename the old index column
df_analise.rename(columns={'index':'TEMA'}, inplace=True)

# rename columns
df_analise.columns = ['CATEGORIA', 'ASPECTO_POLÍTICO', 'CAMPO_DE_PESQUISA_ESTUDO',\
              'CRÍTICA_DO_TERMO', 'DEFINIÇÃO_DO_TERMO', 'EXTINÇÃO_DO_CATIVEIRO',\
              'NOTA_RODAPÉ', 'PERSPECTIVA_COMPARATIVA', 'PERSPECTIVA_TEÓRICA']

# delete the column 'NOTA_RODAPÉ'
df_analise = df_analise.drop(columns=['NOTA_RODAPÉ'])


# call the function to organize the dataframe
df_analise2 = organize_df(df_analise)

# call the function to create the bar chart
create_bar_chart(df_analise2, 'Usos do termo pós-abolição nos papers da ANPUH: Análise dos sentidos', 800, 600, 'bar_analise')

# xlsx file of 'TEMA x TEMPO'
df_tem = read_xlsx('/home/ebn/Documentos/Github/development/pibic_2020-2021/EDITAL_UNILAB/ATLAS/COOC_TEMAxTEMPORAL.xlsx')
# rename columns
df_tem.columns = ['SÉC_XIX', 'SÉC_XVII','SÉC_XVIII','SÉC_XX','SÉC_XXI']

#call the function to organize the dataframe
df_tem = organize_df(df_tem)
# sort the dataframe by value in column 'TEMA_CENTRAL'
df_tem = df_tem.sort_values(by=['TEMA_CENTRAL'], ascending=False)

# call the function to create the bar chart
create_bar_chart(df_tem, 'Usos do termo pós-abolição nos papers da ANPUH: Recorte Temporal', 800, 600, 'bar_tem')

# xlsx file of 'TEMA x ESPAÇO'
df_esp = df = read_xlsx('/home/ebn/Documentos/Github/development/pibic_2020-2021/EDITAL_UNILAB/ATLAS/COOC_TEMAxESPAÇO.xlsx')

# clean the dataframe deleting string valus in column names
df_esp.columns = df_esp.columns.str.replace('● REC_ESPACIAL::','')
# delete the string values containing '\nGr=' plus one or two digits
df_esp.columns = df_esp.columns.str.replace('\nGr=\d{1,2}','', regex=True)
# call the function to organize the dataframe
df_esp = organize_df(df_esp)
# sort the dataframe by values in column 'TEMA_CENTRAL'
df_esp_sorted = df_esp.sort_values(by=['TEMA_CENTRAL'])
#call the function to create the horizontal bar chart
create_horizontal_bar_chart(df_esp_sorted, 'Usos do termo pós-abolição nos papers da ANPUH: Recorte Espacial', 1200, 1200, 'bar_esp')

# xlsx file of 'TEMA x TEMÁTICA'
df_tema = read_xlsx('/home/ebn/Documentos/Github/development/pibic_2020-2021/EDITAL_UNILAB/ATLAS/COOC_TEMAxTEMÁTICA.xlsx')
# clean the dataframe deleting string valus in column names
df_tema.columns = df_tema.columns.str.replace('● TEMÁTICA_GERAL::','')
# delete the string values from '\nGr='to the end
df_tema.columns = df_tema.columns.str.replace('\nGr=.*','', regex=True)
# delete the column 'NEGRO'
df_tema = df_tema.drop(columns=['NEGROS'])
# call the function to organize the dataframe
df_tema = organize_df(df_tema)
# sort the dataframe by values in column 'TEMA_CENTRAL'
df_tema_sorted = df_tema.sort_values(by=['TEMA_CENTRAL'])
# call the function to create the horizontal bar chart
create_horizontal_bar_chart(df_tema_sorted, 'Usos do termo pós-abolição nos papers da ANPUH: Temática Geral', 1200, 1200, 'bar_tema')

# create a df getting the 10 last rows of the dataframe 'df_tema_sorted'
df_tema_sorted_10 = df_tema_sorted.tail(10)
# create a df getting the 10 last rows of the dataframe 'df_esp_sorted'
df_esp_sorted_10 = df_esp_sorted.tail(10)

# create a horizontal bar chart with the 10 first rows of the dataframe 'df_esp'
create_horizontal_bar_chart(df_esp_sorted_10, 'Usos do termo pós-abolição nos papers da ANPUH: Recorte Espacial - 10 mais frequentes', 1200, 1200, 'bar_esp_10')
# create a horizontal bar chart with the 10 first rows of the dataframe 'df_tema'
create_horizontal_bar_chart(df_tema_sorted_10, 'Usos do termo pós-abolição nos papers da ANPUH: Temática Geral - 10 mais frequentes', 1200, 1200, 'bar_tema_10')
