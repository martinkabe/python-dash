from turtle import title
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools as tls
import pandas as pd

chart_name = 'heatmap-multiple'

df1 = pd.read_csv('data/2010SitkaAK.csv')
df2 = pd.read_csv('data/2010SantaBarbaraCA.csv')
df3 = pd.read_csv('data/2010YumaAZ.csv')
# print(df.head())

data = [df1, df2, df3]
traces = []

for d in data:
    traces.append(
        go.Heatmap(
            x=d['DAY'],
            y=d['LST_TIME'],
            z=d['T_HR_AVG'].values.tolist(),
            colorscale='Jet',
            zmin=5, zmax=40
        )
    )

fig = tls.make_subplots(
    rows=1,
    cols=3,
    subplot_titles=['Sitka AK','SB CA','Yuma AZ'],
    shared_yaxes=True
)

fig['layout'].update(title='Temps for 3 cities')

fig.append_trace(traces[0],1,1)
fig.append_trace(traces[1],1,2)
fig.append_trace(traces[2],1,3)
pyo.plot(fig, filename=f'plots-results/{chart_name}.html')