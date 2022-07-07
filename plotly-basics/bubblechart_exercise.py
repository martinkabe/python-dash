import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('data/mpg.csv')
df.sort_values(by=['horsepower'], ascending=False, inplace=True)
# print(df.head())

data = [
    go.Scatter(
        x=df['displacement'],
        y=df['acceleration'],
        text=df['name'],
        mode='markers',
        marker=dict(
            size=df['weight']/400,
            color=df['cylinders'],
            showscale=True
        )
    )
]

layout = go.Layout(
    title='Vehicle acceleration vs. displacement',
    xaxis=dict(title='Displacement'),
    yaxis=dict(title='Acceleration = seconds to reach 60mph'),
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)