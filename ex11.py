import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Read CSV file
df = pd.read_csv("sales_data.csv")

# Create Dash application
app = dash.Dash(__name__)
app.title = "Sales Dashboard"

# Layout
app.layout = html.Div([
    html.H1(
        "Sales Dashboard",
        style={'textAlign': 'center'}
    ),

    html.Label("Select Product:"),

    dcc.Dropdown(
        id='product-dropdown',
        options=[
            {'label': p, 'value': p}
            for p in df['Product'].unique()
        ],
        value='A'
    ),

    dcc.Graph(id='sales-bar-chart'),

    html.Br(),

    dcc.Graph(id='region-pie-chart')
])


# Callback
@app.callback(
    [
        Output('sales-bar-chart', 'figure'),
        Output('region-pie-chart', 'figure')
    ],
    [
        Input('product-dropdown', 'value')
    ]
)
def update_dashboard(selected_product):

    filtered_df = df[df['Product'] == selected_product]

    # Bar chart
    bar_fig = px.bar(
        filtered_df,
        x='Month',
        y='Sales',
        title=f'Sales Trend for Product {selected_product}',
        labels={
            'Sales': 'Sales Amount',
            'Month': 'Month'
        }
    )

    # Pie chart
    pie_fig = px.pie(
        filtered_df,
        names='Region',
        values='Sales',
        title=f'Sales Distribution by Region for Product {selected_product}'
    )

    return bar_fig, pie_fig


# Run application
if __name__ == '__main__':
    app.run(debug=True)