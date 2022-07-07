import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('data/2010YumaAZ.csv')
# print(df.head())

days = df['DAY'].unique().tolist()

data = []

for day in days:
    df2 = df[df['DAY']==day]
    trace = go.Scatter(
        x=df2['LST_TIME'],
        y=df2['T_HR_AVG'],
        mode='lines',
        name=day
    )
    data.append(trace)

layout = go.Layout(title='Daily temp avgs')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)