from dash import Dash, html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


life_exp_link='https://ourworldindata.org/life-expectancy'
life_exp_logo='https://uptime.com/media/website_profiles/sofifa.com.png'

life_exp_data=pd.read_csv('data/life_expectancy.csv')
year_min=life_exp_data['year'].min()
year_max=life_exp_data['year'].max()

navbar=dbc.NavbarSimple(
    brand='Life Expectancy',
    children=[
        html.Img(
            src=life_exp_logo,
            height=20
        ),
        html.A(
            'Data Source',
            href=life_exp_link,
            target='_blank',
            style={'color':'black'}
        )
    ],
    color='primary',
    fluid=True
)

head_card=dbc.Row(
    dbc.Col(
        dbc.Card([
            html.H4('Life Expectancy by countries'),
            html.Br(),
            dcc.RangeSlider(
                id='year-slider',
                min=year_min,
                max=year_max,
                value=[year_min, year_max],
                marks={i:str(i) for i in range(year_min, year_max+1, 10)},
                tooltip={"placement": "top", "always_visible": True}
            ),
        ],
        body=True,
        style={'textAlign':'center','color':'white'},
        color='lightblue')
    )
)

app=Dash(
    __name__,
    title='Capstone Project II',
    update_title='Loading ...',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div([
    navbar,
    html.Br(),
    head_card,
    html.Br(),
    dcc.Dropdown(
        id='dropdown-countries',
        options=life_exp_data['country'].unique(),
        multi=True
            
    ),
    html.Br(),
    html.Button(id='btn-trigger', children='Submit'),
    html.Br(),
    dcc.Graph(id='life-expectancy-graph')
])

@app.callback(
    Output('life-expectancy-graph','figure'),
    [Input('btn-trigger','n_clicks')],
    State('year-slider','value'),
    State('dropdown-countries','value')
)
def update_chart(n_clicks, selected_years, selected_country):
    if selected_country is None:
        raise PreventUpdate
    msk = (life_exp_data['country'].isin(selected_country)) & \
          (life_exp_data['year'] >= selected_years[0]) & \
          (life_exp_data['year'] <= selected_years[1])
    life_expectancy_filtered = life_exp_data[msk]
    line_fig = px.line(life_expectancy_filtered,
                       x='year', y='life expectancy',
                       title='Life expectancy',
                       color='country')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)