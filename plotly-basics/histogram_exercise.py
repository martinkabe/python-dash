import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


chart_name = 'histogram-exercise'

df = pd.read_csv('data/abalone.csv')

data = [
    go.Histogram(
        x=df['length'],
        xbins=dict(start=0.0, end=1.0, size=0.02)
    )
]
layout = go.Layout(title='Histogram')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename=f'plots-results/{chart_name}.html')