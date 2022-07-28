import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd


app = dash.Dash()

df = pd.read_csv('data/OldFaithful.csv')

app.layout = html.Div(
    [
        dcc.Graph(
        id='scatterplot',
        figure={
            'data': [
                go.Scatter(
                    x=df['X'],
                    y=df['Y'],
                    mode='markers',
                    marker={
                        'size':12,
                        'color':'rgb(51,204,153)',
                        'line':{ 'width':2 }
                    }
                )
            ],
            'layout': go.Layout(
                title='Old Faithful Eruptions',
                xaxis={ 'title':'Duration' },
                yaxis={ 'title':'Interval' }
            )
        }
    )]
)


if __name__ == '__main__':
    app.run_server()
