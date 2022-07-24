import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd


app = dash.Dash(__name__)

nsdq = pd.read_csv('data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol', inplace=True)
options = []

for tick in nsdq.index:
    mydict = {}
    mydict['label'] = nsdq.loc[tick]['Name']
    mydict['value'] = tick
    options.append(mydict)

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Enter a stock symbol:', style={'paddingRight':'30px'}),
        dcc.Dropdown(
            id='my_ticker_symbol',
            options = options,
            value=['TSLA'],
            multi=True
        )
    ], style={'display':'inline-block', 'verticalAllign':'top', 'width':'30%'}),
    html.Div([
        html.H3('Select a start and end date:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed=datetime(2015,1,1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2018,1,1),
            end_date=datetime.today()
        )
    ], style={'display':'inline-block'}),
    html.Div([
        html.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            style={'fontSize':24, 'marginLeft':'30px'}
        )
    ], style={'display':'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
            'data':[
                {'x':[1,2], 'y':[3,1]}
            ]
        }
    )
])


@app.callback(
    Output(component_id='my_graph', component_property='figure'),
    [Input(component_id='submit_button', component_property='n_clicks')],
    [State(component_id='my_ticker_symbol', component_property='value'),
     State(component_id='my_date_picker', component_property='start_date'),
     State(component_id='my_date_picker', component_property='end_date')
    ])
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic, 'yahoo', start, end) # use yahoo instead of iex
        traces.append({'x':df.index, 'y':df['Close'], 'name':tic})

    fig = {
        'data':traces,
        'layout':{'title':stock_ticker}
    }
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)