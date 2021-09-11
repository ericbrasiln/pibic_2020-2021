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

df = df.reset_index()

# count values for each event
counts = df.groupby('Evento').count()
counts = pd.DataFrame(counts)
counts = counts.reset_index()

#plot the data
fig = go.Figure()
fig.add_trace(go.Bar(x=counts['Evento'], y=counts['P-doc']))
fig.update_layout(title_text='HDB - Documentos com código `Metodologia` divididos por eventos.', xaxis_title='Eventos', yaxis_title='P-doc')
fig.update_traces(texttemplate='%{y:.0f}', textposition='outside')
fig.show()
#save the plot as html and png
fig.write_html('eventos.html')
fig.write_image('eventos.png')
