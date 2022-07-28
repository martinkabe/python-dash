import plotly.offline as pyo
import plotly.graph_objs as go

chart_name = 'boxplot'

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]
snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [
    go.Box(
        y=y,
        boxpoints='outliers',
        jitter=0.3,
        pointpos=0
    )
]
pyo.plot(data, filename=f'plots-results/{chart_name}.html')

data_twain = [
    go.Box(y=snodgrass, name='Snodgrass'),
    go.Box(y=twain, name='Twain')
]
pyo.plot(data_twain, filename=f'plots-results/{chart_name}-twain.html')