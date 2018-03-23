# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Android Data Visualization'),

    html.Div(children='''
        Android versions marketshare data visusliation using Dash.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['Gingerbread', 'Ice Cream Sandwich', 'Jelly Bean', 'Kitkat',
                 'Lollipop', 'Marshmallow','Nougat', 'Oreo'],
                 'y': [0.3, 0.4, 5, 12, 24.6, 28.10, 28.5, 1.1],
                 'type': 'bar'}
            ],
            'layout': {
                'title': 'Android Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
