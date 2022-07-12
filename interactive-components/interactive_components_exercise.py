from distutils.log import debug
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider(
        id='my-range-slider',
        min=-10,
        max=10,
        step=1,
        marks={ i:str(i) for i in range(-10, 11) },
        value=[-3, 3]
    ),
    html.Div(
        id='output-container-range-slider',
        style={ 'width':'48%', 'display':'inline-block', 'font-size':'60px' }
    )
])


@app.callback(
    Output(component_id='output-container-range-slider', component_property='children'),
    [Input(component_id='my-range-slider', component_property='value')]
)
def uptade_output(value_list):
    return value_list[0] * value_list[1]


if __name__ == '__main__':
    app.run_server(
        debug=True
    )