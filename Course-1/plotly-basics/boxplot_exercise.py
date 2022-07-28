import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np


chart_name = 'boxplot-exercise'

def random_samples(n, m):
    data = []
    for d in range(n):
        dataset = np.random.choice(df['rings'],m,replace=False)
        data.append(go.Box(y=dataset, name=f'Dataset: {d}'))
    return data

df = pd.read_csv('data/abalone.csv')
n = 5
m = 30
data = random_samples(n, m)
layout = go.Layout(title=f'{n} random samples consist of {m} observations')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename=f'plots-results/{chart_name}.html')
