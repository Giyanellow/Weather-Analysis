# Import packages
from dash import Dash, html, dash_table, dcc, callback
import dash_daq as daq
from dash.dependencies import Input,Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Incorporate data
df = pd.read_csv('../weather_data_clean.csv')

# For date slider
weekly_dates = pd.date_range(start=df['date'].min(), end=df['date'].max(), freq='W-MON')

# Types of graphs
graph_types = ['line', 'bar', 'scatter']

# Initialize the app
app = Dash()

# App layout
app.layout = html.Div(id='main-container', children=[
    html.H1('Baguio Weather Patterns'),
    html.Div(id='table-container', children=[
        dash_table.DataTable(data=df.to_dict('records'), page_size=10)
        ]),
    html.Div(id='options-container', children=[
        html.H2('Select Week'),
        dcc.Slider(
            min=0,
            max=len(weekly_dates) - 1,
            step=1,
            id='week-slider',
            value=len(weekly_dates) - 1,
            marks={i: f'Week {i + 1}' for i in range(len(weekly_dates))},
            ),
        html.Div(id='col-container', children=[
            html.H2('Select X-Axis Column'),
            dcc.Dropdown(
                id='x-axis-col',
                options=[{'label': col, 'value': col} for col in df.columns],
                value='date'
                ),
            html.H2('Select Y-Axis Column'),
            dcc.Dropdown(
                id='y-axis-col',
                options=[{'label': col, 'value': col} for col in df.columns],
                value='high'
                ),
            ]),
        html.H2('Select Graph Type'),
        dcc.Dropdown(
            id='graph-type',
            options=[{'label': graph_type, 'value': graph_type} for graph_type in graph_types],
            value='line'
            ),
        ]),
    html.Div(id='graph-container', children=[
        dcc.Graph(id='graph'),
    ]),
])

# Callbacks
@callback(
    Output('graph', 'figure'),
    Input('week-slider', 'value'),
    Input('x-axis-col', 'value'),
    Input('y-axis-col', 'value'),
    Input('graph-type', 'value'),
)
def update_figure(selected_week_index,x_col,y_col,graph_type):
    selected_week_date = weekly_dates[selected_week_index]
    df['date'] = pd.to_datetime(df['date'])
    df['average'] = df[['high', 'low']].mean(axis=1)
    filtered_df = df[df['date'] <= selected_week_date]
    
    # print(f'Graph Type: {graph_type}')
    # print(f'X-Axis Column: {x_col}')
    # print(f'Y-Axis Column: {y_col}')
    
    if graph_type == 'line':
        fig = px.line(filtered_df, x=x_col, y=y_col, title=f'{y_col.capitalize()} vs {x_col.capitalize()}')
    elif graph_type == 'bar':
        fig = px.bar(filtered_df, x=x_col, y=y_col, title=f'{y_col.capitalize()} vs {x_col.capitalize()}')
    elif graph_type == 'scatter':
        fig = px.scatter(filtered_df, x=x_col, y=y_col, title=f'{y_col.capitalize()} vs {x_col.capitalize()}')

    fig.update_layout(
        title=f'{y_col.capitalize()} vs {x_col.capitalize()}',
        xaxis_title=x_col.capitalize(),
        yaxis_title=y_col.capitalize()
    )

    return fig
    
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
