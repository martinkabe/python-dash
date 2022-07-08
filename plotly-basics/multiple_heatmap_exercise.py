from turtle import title
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools as tls
import pandas as pd

chart_name = 'heatmap-multiple-exercise'

df = pd.read_csv('data/flights.csv')
# print(df.head())

data = [
    go.Heatmap(
        x=df['year'],
        y=df['month'],
        z=df['passengers'].values.tolist(),
        colorscale='Jet'
    )
]

layout = go.Layout(title='Flights')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename=f'plots-results/{chart_name}.html')