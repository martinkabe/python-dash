import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from numpy import random


app = dash.Dash()

df = pd.read_csv('data/mpg.csv')
# Adding jitter
df['year'] = random.randint(-4,4,len(df))*0.05 + df['model_year']

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='mpg_scatter',
            figure={
                'data':[go.Scatter(
                    x=df['year']+1900,
                    y=df['mpg'],
                    text=df['name'],
                    hoverinfo='text+y+x',
                    mode='markers'
                )],
                'layout':go.Layout(
                    title='MPG Data',
                    xaxis={ 'title':'Model Year' },
                    yaxis={  'title':'MPG' },
                    hovermode='closest'
                )
            }
        )
    ], style={ 'width':'50%', 'display':'inline-block'}),
    html.Div([
        dcc.Graph(
            id='mpg_line',
            figure={
                'data':[go.Scatter(
                    x=[0,1],
                    y=[0,1],
                    mode='lines'
                )],
                'layout':go.Layout(
                    title='Acceleration',
                    margin={'l':0}
                )
            }
        )
    ], style={ 'width':'20%', 'height':'50%', 'display':'inline-block' }),
    html.Div([
        dcc.Markdown(
            id='mpg_stats'
        )
    ], style={ 'width':'20%', 'height':'50%', 'display':'inline-block' })
])


@app.callback(
    Output(component_id='mpg_line', component_property='figure'),
    [Input(component_id='mpg_scatter', component_property='hoverData')]
)
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {
        'data':[go.Scatter(
            x=[0,1],
            y=[0,60/df.iloc[v_index]['acceleration']],
            mode='lines',
            line={ 'width':3*df.iloc[v_index]['cylinders'] }
        )],
        'layout':go.Layout(
            title=df.iloc[v_index]['name'],
            margin={'l':0},
            height=300,
            xaxis={ 'visible':False },
            yaxis={ 'visible':False, 'range':[0,60/df['acceleration'].min()] }
        )
    }
    return figure


@app.callback(
    Output(component_id='mpg_stats', component_property='children'),
    [Input(component_id='mpg_scatter', component_property='hoverData')]
)
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
            {} cylinders\n
            {}cc displacement\n
            0 to 60mph in {} seconds
            """.format(
                df.iloc[v_index]['cylinders'],
                df.iloc[v_index]['displacement'],
                df.iloc[v_index]['acceleration']
            )
    return stats


if __name__ == '__main__':
    app.run_server(debug=True)
