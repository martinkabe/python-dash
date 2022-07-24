from distutils.log import debug
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1(id='live_update_text'),
    dcc.Interval(
        id='interval_component',
        interval=10000,
        n_intervals=0
    )
])


@app.callback(
    Output(component_id='live_update_text', component_property='children'),
    [Input(component_id='interval_component', component_property='n_intervals')]
)
def update_layout(n):
    return "Crash free for {} refreshes".format(n)


if __name__ == '__main__':
    app.run_server(debug=True)