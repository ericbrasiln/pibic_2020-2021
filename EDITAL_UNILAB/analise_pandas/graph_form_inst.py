import pandas as pd
import plotly.graph_objects as go

# function to read the csv from the HDB-ANPUH
def read_csv(path):
    # read the csv
    df = pd.read_csv(path, sep=',', index_col=0)
    return df

#function to organize the dataframe
def organize_df(df, code):
    df = df.reset_index()
    df.columns = ['ID','CÓDIGOS']
    #delete column 'ID'
    df = df.drop(columns=['ID'])
    # count the number of times each theme appears
    df_count = df.groupby('CÓDIGOS').size().reset_index(name=code)
    # sort the dataframe by the number of times each theme appears
    df_count = df_count.sort_values(by=code, ascending=False)
    #save the dataframe in a csv file
    return df_count   

# function to concatenate the dataframes
def concat_df(df1, df2):
    dfs = [df1, df2]
    cols = ['CÓDIGOS']
    keys = ['TEMA_CENTRAL', 'TEMA_INCIDENTAL']
    df = pd.concat(
              [df.set_index(cols) for df in dfs],
              axis=1, keys=keys)
    df.columns = df.columns.droplevel(-1)
    #reset the index
    df = df.reset_index()
    #rename columns 
    df.columns = ['CÓDIGOS', 'TEMA_CENTRAL', 'TEMA_INCIDENTAL']
    # change Nan to 0
    df = df.fillna(0)
    # change dtype of column 'TEMA_CENTRAL' and 'TEMA_INCIDENTAL' to int
    df['TEMA_CENTRAL'] = df.TEMA_CENTRAL.astype(int)
    df['TEMA_INCIDENTAL'] = df.TEMA_INCIDENTAL.astype(int)
    return df

#create horizontal bar chart
def create_horizontal_bar_chart(df, title, x_title, output):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['CÓDIGOS'],
        y=df['TEMA_CENTRAL'],
        name='TEMA_CENTRAL',
        marker=dict(
            color='rgba(246, 78, 139, 0.6)',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        x=df['CÓDIGOS'],
        y=df['TEMA_INCIDENTAL'],
        name='TEMA_INCIDENTAL',
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        )
    ))
    fig.update_layout(
        title=title,
        xaxis_title=x_title,
        yaxis_title='CITAÇÕES',
        barmode='stack',
        #size
        width=1000,
        height=600
    )
    fig.show()
    #save the chart as a html and png file
    fig.write_html(output+'.html')
    fig.write_image(output+'.png')

# 'INSTITUIÇÃO'
# call the function to read the csv
df_inst_cent = read_csv('/home/ebn/Documentos/Github/development/pibic_2020-2021/EDITAL_UNILAB/analise_pandas/csv/csv_alter/inst_central_alter.csv')
# call the function to organize the dataframe
df_inst_cent = organize_df(df_inst_cent, 'TEMA_CENTRAL')

# call the function to read the csv 
df_inst_incid = read_csv('/home/ebn/Documentos/Github/development/pibic_2020-2021/EDITAL_UNILAB/analise_pandas/csv/csv_alter/inst_incidental_alter.csv')
# call the function to organize the dataframe
df_inst_incid = organize_df(df_inst_incid, 'TEMA_INCIDENTAL')

# call the function to concatenate the dataframes
df_inst = concat_df(df_inst_cent, df_inst_incid)

# call the function to create the horizontal bar chart
create_horizontal_bar_chart(df_inst, 'Usos do termo pós-abolição nos papers da ANPUH: Instituições dos(as) autores(as)', 'INSTITUIÇÕES', 'instituicoes')

# 'FORMAÇÃO'
# call the function to read the csv
df_form_cent = read_csv('/home/ebn/Documentos/Github/development/pibic_2020-2021/EDITAL_UNILAB/analise_pandas/csv/csv_alter/form_central_alter.csv')
# call the function to organize the dataframe
df_form_cent = organize_df(df_form_cent, 'TEMA_CENTRAL')

# call the function to read the csv
df_form_incid = read_csv('/home/ebn/Documentos/Github/development/pibic_2020-2021/EDITAL_UNILAB/analise_pandas/csv/csv_alter/form_incidental_alter.csv')
# call the function to organize the dataframe
df_form_incid = organize_df(df_form_incid, 'TEMA_INCIDENTAL')

# call the function to concatenate the dataframes
df_form = concat_df(df_form_cent, df_form_incid)

# call the function to create the horizontal bar chart
create_horizontal_bar_chart(df_form, 'Usos do termo pós-abolição nos papers da ANPUH: Formação dos(as) autores(as)', 'FORMAÇÃO', 'formacao')
