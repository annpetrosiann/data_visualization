import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash import dash_table
import plotly.express as px
import pandas as pd
import os

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
df = pd.read_csv('SM.csv')
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(html.A(
                            html.Img(src="assets/a.png", height="97px"),
                            href="#home"
                        )),
                        dbc.Col(
                            dbc.Nav(
                                [
                                    dbc.NavItem(dbc.NavLink("Home", href="#home", id="nav-home")),
                                    dbc.NavItem(dbc.NavLink("Survey", href="#survey", id="nav-survey")),
                                    dbc.NavItem(dbc.NavLink("Data", href="#data", id="nav-data")),
                                    dbc.DropdownMenu(
                                        label="Visualization",
                                        children=[
                                            dbc.DropdownMenuItem("Statistics", href="#viz1", id="viz1"),
                                            dbc.DropdownMenuItem("Assumptions", href="#viz2", id="viz2"),
                                            dbc.DropdownMenuItem("Platforms", href="#viz3", id="viz3"),
                                        ],
                                        nav=True,
                                        in_navbar=True,
                                        className="dropdown",
                                        toggleClassName="dropdown-toggle"
                                    ),
                                ],
                                className="ms-auto",
                                navbar=True
                            ),
                            width="auto"
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
            ],
            fluid=True,
            className="px-4"
        ),
        color="dark",
        dark=True,
        className="mb-5"
    ),
    html.Div(id='page-content'),
    dcc.Store(id='form-data')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'hash'),
     Input('nav-home', 'n_clicks'),
     Input('nav-survey', 'n_clicks'),
     Input('nav-data', 'n_clicks'),
     Input('viz1', 'n_clicks'),
     Input('viz2', 'n_clicks'),
     Input('viz3', 'n_clicks')]
)
def display_page(url_hash, home_clicks, survey_clicks, data_clicks, viz1_clicks, viz2_clicks, viz3_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dbc.Container([
            dbc.Row([
                dbc.Col(html.Div(
                    "Social media keeps getting bigger.New apps show up all the time.While this is exciting, it can also be concerning because people are beginning to live their lives online, losing touch with the real world.In this project, we aim to understand the impact of social media on individuals.Social media can negatively affect mental health, and that is what we intend to explore.Our data is collected from a survey consisting of 20 questions, conducted in 2022.The questions are grouped into four general categories of mental issues: ADHD, anxiety, depression, and social comparison.For more information, please click the 'Survey' button.",
                    className="text-box"), width=6),
                dbc.Col(html.Div(
                    "ADHD (Attention-Deficit/Hyperactivity Disorder) is a condition where someone finds it harder than others their age to focus, stay still, or control their actions.This can make it tough for them to do well in school, work, or social situations.It's something people can have from childhood, and for many, it continues into adulthood."
                    "\nAnxiety  is when you feel nervous or worried.Everyone feels anxious now and then, but if someone feels anxious almost all the time and it makes daily life hard, it might be an anxiety disorder."
                    "Depression makes a person feel very sad or lose interest in things they used to like.It’s not just having a bad day; it’s feeling like this for a long time, which makes everyday things hard to do.Social Comparison happens when you look at what other people are doing or have, and you measure yourself against them.On social network sites, this can make you feel bad if it seems like everyone else’s life is better or easier than yours.",
                    className="text-box"), width=6),
            ], className="text-container")
        ], fluid=True, style={'padding-top': '20px'})

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'nav-home':
        return dbc.Container([
            dbc.Row([
                dbc.Col(html.Div(
                    "Social media keeps getting bigger. New apps show up all the time. While this is exciting, it can also be concerning because people are beginning to live their lives online, losing touch with the real world. In this project, we aim to understand the impact of social media on individuals. Social media can negatively affect mental health, and that is what we intend to explore. Our data is collected from a survey consisting of 20 questions, conducted in 2022. The questions are grouped into four general categories of mental issues: ADHD, anxiety, depression, and social comparison. For more information, please click the 'Survey' button'.",
                    className="text-box"), width=6),
                dbc.Col(html.Div(
                    "ADHD (Attention-Deficit/Hyperactivity Disorder) is a condition where someone finds it harder than others their age to focus, stay still, or control their actions. This can make it tough for them to do well in school, work, or social situations. It's something people can have from childhood, and for many, it continues into adulthood.Anxiety  is when you feel nervous or worried. Everyone feels anxious now and then, but if someone feels anxious almost all the time and it makes daily life hard, it might be an anxiety disorder.Depression makes a person feel very sad or lose interest in things they used to like. It’s not just having a bad day; it’s feeling like this for a long time, which makes everyday things hard to do.Social Comparison happens when you look at what other people are doing or have, and you measure yourself against them. On social network sites, this can make you feel bad if it seems like everyone else’s life is better or easier than yours.",
                    className="text-box"), width=6),
            ], className="text-container")
        ], fluid=True, style={'padding-top': '20px','backgroundImage': 'url("/assets/abc.jpg")', 'height':'800px'})
    elif button_id == 'nav-survey':
        return dbc.Container([
            html.H3("Survey Questions", className="survey-title"),
            html.Div([
                html.Div([
                    html.P("1. What is your age?"),
                    html.P("2. Gender"),
                    html.P("3. Relationship Status"),
                    html.P("4. Occupation Status"),
                    html.P("5. What type of organizations are you affiliated"),
                    html.P("6. Do you use social media?"),
                    html.P("7. What social media platforms do you commonly use?"),
                    html.P("8. What is the average time you spend on social media every day?"),
                    html.P("9. How often do you find yourself using Social media without a specific purpose?"),
                    html.P("10. How often do you get distracted by Social media when you are busy doing something?"),
                    html.P("11. Do you feel restless if you haven\'t used Social media in a while?"),
                    html.P("12. On a scale of 1 to 5, how easily distracted are you?"),
                    html.P("13. On a scale of 1 to 5, how much are you bothered by worries?"),
                    html.P("14. Do you find it difficult to concentrate on things?"),
                    html.P("15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?"),
                    html.P("16. Following the previous question, how do you feel about these comparisons, generally speaking?"),
                    html.P("17. How often do you look to seek validation from features of social media?"),
                    html.P("18. How often do you feel depressed or down?"),
                    html.P("19. On a scale of 1 to 5, how frequently does your interest in daily activities fluctuate?"),
                    html.P("20. On a scale of 1 to 5, how often do you face issues regarding sleep?")
                ], className="text-box-survey")
            ], className="survey-questions")
        ], fluid=True)
    elif button_id == 'nav-data':
        if os.path.isfile('SM.csv'):
            df = pd.read_csv('SM.csv')
            return dbc.Container([
                dash_table.DataTable(
                    id='datatable',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                    page_size=10,
                    style_table={'overflowX': 'auto'},
                    style_cell={
                        'height': 'auto',
                        'minWidth': '100px', 'width': '150px', 'maxWidth': '300px',
                        'whiteSpace': 'normal'
                    },
                )
            ], fluid=True)
        else:
            return dbc.Container([
                html.H3("Survey Data", className="data-title"),
                html.Div("No data available.", className="no-data")
            ], fluid=True)
    elif button_id == 'viz1':
        if os.path.isfile('SM.csv'):
            df = pd.read_csv('SM.csv')

            fig_age_group = px.histogram(df, y='Age group', color_discrete_sequence=['#DEB887'])
            fig_gender = px.pie(df, names='Gender', title='Gender Distribution', color_discrete_sequence=['#D2B48C'])
            fig_relationship = px.pie(df, names='Relationship Status', title='Relationship Status Distribution', color_discrete_sequence=['#DEB887'])
            fig_occupation = px.histogram(df, x='Occupation', title='Occupation Status Distribution', color_discrete_sequence=['#D3B083'])
            fig_age_group.update_layout(
                title={
                    'text': 'Age distribution',
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                xaxis={'title': None, 'showgrid': False, 'showticklabels': False},
                yaxis={'title': None},
                showlegend=False,
            )
            fig_age_group.update_layout({
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
            fig_occupation.update_layout({
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
            fig_gender.update_layout({
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
            fig_relationship.update_layout({
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
            fig_relationship.update_layout(title={
                'text': 'Relationship',
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'}, )
            fig_gender.update_layout(title={
                'text': 'Gender',
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'}, )
            fig_occupation.update_layout(
                title={
                    'text': 'Occupation',
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                xaxis={'title': None},
                yaxis={'title': None, 'showgrid': False, 'showticklabels': False},
                showlegend=False,
            )
            return dbc.Container([
                html.H3("", className="viz-title"),
                dbc.Row([
                    dbc.Col(dcc.Graph(figure=fig_gender), width=6, style={'padding': '10px'}),
                    dbc.Col(dcc.Graph(figure=fig_age_group), width=6, style={'padding': '10px'}),
                ]),
                dbc.Row([
                    dbc.Col(dcc.Graph(figure=fig_occupation), width=6, style={'padding': '10px'}),
                    dbc.Col(dcc.Graph(figure=fig_relationship), width=6, style={'padding': '10px'}),
                ])
            ], fluid=True)
        else:
            return dbc.Container([
                html.H3("", className="viz-title"),
                html.Div("No data available for visualizations.", className="no-data")
            ], fluid=True)
    elif button_id == 'viz2':
        return dbc.Container([
            dbc.Row([
                dbc.Col(dcc.Dropdown(
                    id='assumption-y-axis',
                    options=[
                        {'label': 'Occupation', 'value': 'Occupation'},
                        {'label': 'Relationship Status', 'value': 'Relationship Status'},
                        {'label': 'Age Group', 'value': 'Age group'}
                    ],
                    value='Occupation',
                    clearable=False,
                    className="mb-3"
                ), width=6),
                dbc.Col(dcc.Graph(id='assumption-chart'), width=12, style={'padding': '10px'}),
            ]),
            dbc.Row([
                dbc.Col(dcc.Dropdown(
                    id='bar-y-axis',
                    options=[
                        {'label': 'ADHD Score', 'value': 'ADHD Score'},
                        {'label': 'Anxiety Score', 'value': 'Anxiety Score'},
                        {'label': 'Social Comparison Score', 'value': 'Social Comparison Score'},
                        {'label': 'Depression Score', 'value': 'Depression Score'},
                        {'label': 'Total Score', 'value': 'Total Score'}
                    ],
                    clearable=False,
                    value='ADHD Score',
                    className="mb-3"
                ), width=6),
                dbc.Col(dcc.Graph(id='bar-chart'), width=12, style={'padding': '10px'}),
            ]),
        ], fluid=True)
    elif button_id == 'viz3':
        if os.path.isfile('SM1.csv'):
            df1 = pd.read_csv('SM1.csv')

            platform_counts = df1['Platforms'].value_counts()
            fig_plt = px.bar(platform_counts, x=platform_counts.index, y=platform_counts.values,
                         labels={'x': 'Platforms', 'y': 'Counts'},
                         title='Distribution of Platforms')

            fig_plt.update_layout(
                title={
                    'text': 'Platforms Distribution',
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                xaxis={'title': None},
                yaxis={'title': None, 'showgrid': False, 'showticklabels': False,},
                showlegend=False,
            )
            fig_plt.update_layout({
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
            df_exploded = df1.explode('Platforms')
            platform_age_counts = df_exploded.groupby(['Age group', 'Platforms']).size().reset_index(name='Counts')

            fig_age_count = px.bar(platform_age_counts, x='Age group', y='Counts', color='Platforms',
                         labels={'Platforms': 'Platforms', 'Counts': 'Counts'},
                         title='Distribution of Platforms by Age Group',
                         barmode='group')

            fig_age_count.update_layout(
                title={
                    'text': 'Distribution of Platforms by Age Group',
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                xaxis={'title': None},
                yaxis={'title': None, 'showgrid': False, 'showticklabels': False})

            fig_age_count.update_layout({
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
            return dbc.Container([
                dbc.Row([
                    dbc.Col(dcc.Graph(figure=fig_plt), width=6, style={'padding': '10px'}),
                    dbc.Col(dcc.Graph(figure=fig_age_count), width=6, style={'padding': '10px'}),

                ])
            ], fluid=True)
        else:
            return dbc.Container([
                html.H3("Platforms Usage Distribution", className="viz-title"),
                html.Div("No data available for visualizations.", className="no-data")
            ], fluid=True)
    return dbc.Container()

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('bar-y-axis', 'value')]
)
def update_assumption_chart(y_axis):
    if os.path.isfile('SM.csv'):
        df = pd.read_csv('SM.csv')

        fig = plot_bar_chart(df, y_axis)
        return fig
    else:
        return {}

def plot_bar_chart(df, column_name):
    custom_peach_color_scale = [
        [0.0, '#FFDAB9'],
        [0.5, '#FFA07A'],
        [1.0, '#CD5C5C']
    ]

    data = df.groupby(['Gender', column_name]).size().reset_index(name='Count')

    fig = px.bar(data, x='Gender', y='Count', color=column_name,
                 color_continuous_scale=custom_peach_color_scale,
                 labels={'Gender': 'Gender', 'Count': 'Count', column_name: column_name})
    fig.update_layout(
        title={
            'text': f'Gender By {column_name}',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis={'title': None, 'showgrid': False},
        yaxis={'title': None,'showticklabels': False, 'showgrid': False},
        showlegend=False,
        barmode='stack',
    )
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return fig


def plot_stacked_bar_chart(df, column_name):
    colors = [ '#fc5849','#cc3f3f', '#f76d60','#ff8f85', '#f2bdb8']
    data = df.groupby(['Time Spent', column_name]).size().reset_index(name='Count')

    time_spent_order = ['<1 hour', '1-2 hours', '2-3 hours', '3-4 hours', '4-5 hours', '5+ hours']

    fig = px.bar(data, x='Time Spent', y='Count', color=column_name,
                 title=f'Time Spent on Social Media by {column_name}',
                 labels={'Time Spent': 'Time Spent', 'Count': 'Count', column_name: column_name},
                 color_discrete_sequence=colors,
                 category_orders={'Time Spent': time_spent_order})

    fig.update_layout(
        title={
            'text': f'Time Spent By {column_name}',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis={'title': None, 'showgrid': False},
        yaxis={'title': None, 'showticklabels': False, 'showgrid': False},
        barmode='stack'
    )
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return fig

@app.callback(
    Output('assumption-chart', 'figure'),
    [Input('assumption-y-axis', 'value')]
)
def update_assumption_chart(y_axis):
    if os.path.isfile('SM.csv'):
        df = pd.read_csv('SM.csv')

        fig = plot_stacked_bar_chart(df, y_axis)
        return fig
    else:
        return {}

if __name__ == '__main__':
    app.run_server(debug=True)
