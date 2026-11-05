import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Category": ["Apples", "Bananas", "Oranges", "Apples", "Bananas", "Oranges"],
    "Sales": [10, 15, 7, 12, 9, 14],
    "Year": [2024, 2024, 2024, 2025, 2025, 2025]
})

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server  # Required if you deploy to cloud platforms like Render or Heroku later!

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("Dynamic Dropdown Dashboard", className="text-center my-4 text-primary"), width=12)
    ),
    dbc.Row([
        dbc.Col([
            html.Label("Select Year:", className="fw-bold mb-2"),
            dcc.Dropdown(
                id="year-dropdown",
                options=[{"label": str(year), "value": year} for year in df["Year"].unique()],
                value=2024,
                clearable=False
            )
        ], md=4),
        dbc.Col([
            dcc.Graph(id="dynamic-graph")
        ], md=8)
    ])
], fluid=True)

@app.callback(
    Output("dynamic-graph", "figure"),
    Input("year-dropdown", "value")
)
def update_graph(selected_year):
    filtered_df = df[df["Year"] == selected_year]
    fig = px.bar(
        filtered_df, 
        x="Category", 
        y="Sales", 
        title=f"Sales Overview for {selected_year}",
        color="Category"
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)