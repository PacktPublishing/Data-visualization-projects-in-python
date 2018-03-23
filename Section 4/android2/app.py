# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Android Data Visualization',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Android versions\' marketshare data visualization using Dash.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

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
                'title': 'Android Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                    }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
