import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

chart_name = 'heatmap'

df = pd.read_csv('data/2010SantaBarbaraCA.csv')
# print(df.head())

data = [
    go.Heatmap(
        x=df['DAY'],
        y=df['LST_TIME'],
        z=df['T_HR_AVG'].values.tolist(),
        colorscale='Jet'
    )
]

layout = go.Layout(title='SB CA Temps')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename=f'plots-results/{chart_name}.html')