# Import packages
from dash import Dash, html, dash_table, dcc, callback
import dash_daq as daq
from dash.dependencies import Input,Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

# Incorporate data
df = pd.read_csv('../weather_data_clean.csv')

# For date slider
weekly_dates = pd.date_range(start=df['date'].min(), end=df['date'].max(), freq='W-MON')
print(weekly_dates)

# Initialize the app
app = Dash()

# App layout
app.layout = html.Div(id='main-container', children=[
    html.H1('Baguio Weather Patterns'),
    html.Div(id='table-container', children=[
        dash_table.DataTable(data=df.to_dict('records'), page_size=10)
    ]),
    html.Div(id='graph-container', children=[
        dcc.Graph(id='temp-graph'),
        dcc.Graph(id='bar-graph'),
        dcc.Graph(id='scatter-graph')
    ]),
    dcc.Slider(
        min=0,
        max=len(weekly_dates) - 1,
        step=1,
        id='week-slider',
        value=len(weekly_dates) - 1,
        marks={i: f'Week {i + 1}' for i in range(len(weekly_dates))},
    )
])

# Callbacks
@callback(
    [Output('temp-graph', 'figure'),
     Output('bar-graph', 'figure'),
     Output('scatter-graph', 'figure')],
    Input('week-slider', 'value')
)
def update_figure(selected_week_index):
    selected_week_date = weekly_dates[selected_week_index]
    df['date'] = pd.to_datetime(df['date'])
    df['average'] = df[['high', 'low']].mean(axis=1)
    filtered_df = df[df['date'] <= selected_week_date]
 
    # Line graph
    line_fig = px.line(filtered_df, x='date', y=['high', 'low'], title='Temperature Range Over Time')
    line_fig.add_trace(
        go.Scatter(
            x=filtered_df['date'],
            y=filtered_df['average'],
            mode='lines',
            name='Average Temperature',
            line=dict(color='firebrick', width=2, dash='dash')
        )
    )
    line_fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
    )

    # Bar graph
    bar_fig = px.bar(filtered_df, x='date', y='high', title='High Temperatures Over Time')
    bar_fig.update_layout(
        xaxis_title='Date',
        yaxis_title='High Temperature (°C)',
    )

    # Scatter plot
    scatter_fig = px.scatter(filtered_df, x='date', y='low', title='Low Temperatures Over Time')
    scatter_fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Low Temperature (°C)',
    )

    return line_fig, bar_fig, scatter_fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
