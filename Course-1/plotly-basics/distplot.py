import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np


chart_name = 'distplot'

def generate_data_for_distplot(n, m):
    hist_data = []
    group_labels = []
    bin_size = []
    for ch in range(5):
        x = np.random.randn(1000)+ch
        hist_data.append(x)
        group_labels.append(f'Distplot {ch}')
        bin_size.append((ch+1)/10)
    return {'hist_data':hist_data, 'group_labels':group_labels, 'bin_size':bin_size}

distplot_data = generate_data_for_distplot(5, 1000)

fig = ff.create_distplot(
    hist_data=distplot_data['hist_data'],
    group_labels=distplot_data['group_labels'],
    bin_size=distplot_data['bin_size']
)
pyo.plot(fig, filename=f'plots-results/{chart_name}.html')