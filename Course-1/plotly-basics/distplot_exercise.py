import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd


chart_name = 'distplot-exercise'

df = pd.read_csv('data/iris.csv')
# print(df.head())
traces = df['class'].unique().tolist()

hist_data = []
group_labels = traces
for t in traces:
    hist_data.append(df[df['class']==t]['petal_length'])

fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename=f'plots-results/{chart_name}.html')