import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('data/mpg.csv')
df.sort_values(by=['horsepower'], ascending=False, inplace=True)

data = [
    go.Scatter(
        x=df['horsepower'],
        y=df['mpg'],
        text=df['name'],
        mode='markers',
        marker=dict(
            size=df['weight']/100,
            color=df['cylinders'],
            showscale=True
        )
    )
]

layout = go.Layout(title='Bubble chart', hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)