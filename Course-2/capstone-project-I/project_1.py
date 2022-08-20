from http import server
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import plotly.express as px


avocado = pd.read_csv('./data/avocado.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Avocado Prices Dashboard'),
    dcc.Dropdown(
        id='dropdown-geography',
        options=avocado['geography'].unique(),
        value='New York'
    ),
    dcc.Graph(
        id='avocado-graph'
    )
])

@app.callback(
    Output('avocado-graph','figure'),
    [Input('dropdown-geography','value')]
)
def update_avocado_graph(selected_geography):
    filtered_avocado=avocado[avocado['geography']==selected_geography]
    line_fig=px.line(filtered_avocado,
                        x='date',
                        y='average_price',
                        color='type',
                        title=f'Avocado prices in {selected_geography}')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)