from distutils.log import debug
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        id='my_div',
        children='My Dashboard!'
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
