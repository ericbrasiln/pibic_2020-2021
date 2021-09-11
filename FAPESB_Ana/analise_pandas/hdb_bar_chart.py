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
# sort the df byt column 'Citações'
df = df.sort_values(by=['Citações'], ascending=False)
x_column = input("Enter the x-axis column: ")
y_column = input("Enter the y-axis column: ")
x_axis = input("Enter the x-axis: ")
y_axis = input("Enter the y-axis: ")
title = input("Enter the title: ")
output = input("Enter the output file name: ")

#plot the data in a bar chart
fig = go.Figure(data=[go.Bar(x=df[f'{x_column}'], y=df[f'{y_column}'])])
fig.update_layout(title_text=f'{title}', height=600)
#add a legend for axis x
fig.update_xaxes(title_text=f'{x_axis}')
#add a legend for axis y
fig.update_yaxes(title_text=f'{y_axis}')
# update traces text
fig.update_traces(texttemplate='%{y:.0f}', textposition='outside')
fig.show()
# save the plot as pnd and html
fig.write_html(f'{output}.html')
fig.write_image(f'{output}.png')
