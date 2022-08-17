from dash import Dash, html, dcc
from dash.dependencies import Input, Output


app = Dash(__name__)

input_text = dcc.Input(
        value='Change this text',
        type='text',
        style={'width': '50%', 'height': 50},
    )
output_text = html.Div(style={'whiteSpace': 'pre-line'})

app.layout = html.Div([input_text, output_text])

@app.callback(
    Output(component_id=output_text, component_property='children'),
    [Input(component_id=input_text, component_property='value')]
)
def update_output(value):
    return f'You have entered \n{value}'


if __name__ == '__main__':
    app.run_server(debug=True)
