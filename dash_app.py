"""Instantiate a Dash app."""
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            dbc.themes.BOOTSTRAP,
        ]
    )

    # Create a dataframe (note you will load from file instead)
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    # Create the figure
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    # Create the layout
    dash_app.layout = html.Div(children=[
        html.H1(children='Dash app'),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    return dash_app.server
