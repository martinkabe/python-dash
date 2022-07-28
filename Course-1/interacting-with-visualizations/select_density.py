import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd


app = dash.Dash()

# Create data
np.random.seed(10)
x1 = np.linspace(0.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

# DataFrame
df1 = pd.DataFrame({ 'x':x1, 'y':y })
df2 = pd.DataFrame({ 'x':x1, 'y':y })
df3 = pd.DataFrame({ 'x':x2, 'y':y })

df = pd.concat([df1,df2,df3])

app.layout = html.Div([
    html.Div([
        dcc.Graph(
        id='plot',
        figure={ 'data':[go.Scatter(
            x=df['x'],
            y=df['y'],
            mode='markers'
            )], 'layout':go.Layout(
                title='Random Scatterplot',
                hovermode='closest'
            )}
        )
    ],
    style={ 'width':'30%', 'display':'inline-block' }),
    html.Div([
        html.H1(id='density', style={ 'paddingTop':25 })
    ],
    style={ 'width':'30', 'display':'inline-block', 'verticalAlign':'top' })
])


@app.callback(
    Output(component_id='density', component_property='children'),
    [Input(component_id='plot', component_property='selectedData')]
)
def find_density(selected_data):
    if selected_data is None:
        return 'Select some data'
    pts = len(selected_data['points'])
    rng_or_lp = list(selected_data.keys())
    rng_or_lp.remove('points')
    max_x = max(selected_data[rng_or_lp[0]]['x'])
    min_x = min(selected_data[rng_or_lp[0]]['x'])
    max_y = max(selected_data[rng_or_lp[0]]['y'])
    min_y = min(selected_data[rng_or_lp[0]]['y'])
    area = (max_x-min_x)*(max_y-min_y)
    d = pts/area
    return 'Density = {:.2f}'.format(d)


if __name__ == '__main__':
    app.run_server(
        debug=True
    )