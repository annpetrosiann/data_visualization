import dash  # type: ignore
from dash import dcc  # type: ignore
from dash import html  # type: ignore
from dash.dependencies import Input, Output
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
import pandas as pd
import numpy as np
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

mouse_data = pd.read_csv('Mouse_metadata.csv')
study_results = pd.read_csv('Study_results.csv')
merged_df = pd.merge(mouse_data, study_results, on='Mouse ID')



color_choices = {
    'light-blue': '#7FAB8',
    'light-grey': '#F7EFED',
    'light-red': '#F1485B',
    'dark-blue': '#33546D',
    'middle-blue': '#61D4E2'
}

drug_colors = {
    'Placebo': '#29304E',
    'Capomulin': '#27706B',
    'Ramicane': '#71AB7F',
    'Ceftamin': '#9F4440',
    'Infubinol': '#FFD37B',
    'Ketapril': '#FEADB9',
    'Naftisol': '#B3AB9E',
    'Propriva': '#ED5CD4',
    'Stelasyn': '#97C1DF',
    'Zoniferol': '#8980D4'
}

colors = {
    'full-background': color_choices['light-grey'],
    'chart-background': color_choices['light-grey'],
    'histogram-color-1': color_choices['dark-blue'],
    'histogram-color-2': color_choices['light-red'],
    'block-borders': color_choices['dark-blue']
}

margins = {
    'block-margins': '10px 10px 10px 10px',
    'block-margins': '4px 4px 4px 4px'
}

sizes = {
    'subblock-heights': '290px'
}


div_title = html.Div(children=html.H1('Mouse Experiment', style={'text-align': 'center'}),
                     style={
                         'border': '3px {} solid'.format(colors['block-borders']),
                         'margin': margins['block-margins'],
                         'text-align': 'center'
                     }
                     )


# Block 1-1
div_1_1_button = dcc.Checklist(
    id='weight-histogram-checklist',
    options=[{'label': drug, 'value': drug} for drug in np.unique(mouse_data['Drug Regimen'])],
    value=['Placebo'],
    labelStyle={'display': 'inline-block'}
)

div_1_1_graph = dcc.Graph(
    id='weight-histogram',

)

div_1_1 = html.Div(children=[div_1_1_button, div_1_1_graph],
                   style={
                       'border': '1px {} solid'.format(colors['block-borders']),
                       'margin': margins['block-margins'],
                       'width': '50%',
                       #'height': sizes['subblock-heights'],
                   }, )

# Block 1-2
div_1_2_button = dcc.RadioItems(
    id='weight-distribution-radio',
    options=[{'label': drug, 'value': drug} for drug in np.unique(mouse_data['Drug Regimen'])],
    value='Placebo',
    labelStyle={'display': 'inline-block'}
)

div_1_2_graph = dcc.Graph(
    id='weight-distribution'
)

div_1_2 = html.Div(children=[div_1_2_button, div_1_2_graph],
                   style={
                       'border': '1px {} solid'.format(colors['block-borders']),
                       'margin': margins['block-margins'],
                       'width': '50%',
                       #'height': sizes['subblock-heights'],
                   })



div_raw1 = html.Div(children=[div_1_1, div_1_2],
                    style={
                        'border': '3px {} solid'.format(colors['block-borders']),
                        'margin': margins['block-margins'],
                        'display': 'flex',
                        'flex-direction': 'row'
                    })


# Block 2-1
div_2_1_primary_checklist = dcc.Checklist(
    id='primary-survival-group-checklist',
    options=[
        {'label': 'Lightweight', 'value': 'Lightweight'},
        {'label': 'Heavyweight', 'value': 'Heavyweight'},
        {'label': 'Placebo', 'value': 'Placebo'}
    ],
    value=['Placebo'],
    labelStyle={'display': 'inline-block'}
)

div_2_1_secondary_checklist = dcc.Checklist(
    id='secondary-survival-group-checklist',
    value=['Placebo'],
    labelStyle={'display': 'inline-block'}
)

div_2_1_graph = dcc.Graph(
    id='survival-function-histogram'
)

div_2_1 = html.Div(children=[
    div_2_1_primary_checklist,
    div_2_1_secondary_checklist,
    div_2_1_graph
],
    style={
        'border': '1px {} solid'.format(colors['block-borders']),
        'margin': margins['block-margins'],
        'width': '50%',
        #'height': sizes['subblock-heights'],
    })

# Block 2-2
div_2_2_primary_checklist = dcc.Checklist(
    id='primary-survival-function-checklist',
    options=[
        {'label': 'Lightweight', 'value': 'Lightweight'},
        {'label': 'Heavyweight', 'value': 'Heavyweight'},
        {'label': 'Placebo', 'value': 'Placebo'}
    ],
    value=['Placebo'],
    labelStyle={'display': 'inline-block'}
)

div_2_2_graph = dcc.Graph(
    id='survival-function-line'
)

div_2_2 = html.Div(children=[
    div_2_2_primary_checklist,
    div_2_2_graph
],
    style={
        'border': '1px {} solid'.format(colors['block-borders']),
        'margin': margins['block-margins'],
        'width': '50%',
        #'height': sizes['subblock-heights'],
    })


div_raw2 = html.Div(children=[div_2_1, div_2_2],
                    style={
                        'border': '3px {} solid'.format(colors['block-borders']),
                        'margin': margins['block-margins'],
                        'display': 'flex',
                        'flex-direction': 'row'
                    })

app.layout = html.Div([
    div_title,
    div_raw1,
	div_raw2
 ],
    style={
        'backgroundColor': colors['full-background'],
    }
)



# block 1-1
@app.callback(
    Output(component_id='weight-histogram', component_property='figure'),
    [Input(component_id='weight-histogram-checklist', component_property='value')]
)
def update_weight_histogram(drug_names):
    traces = []

    for drug in drug_names:
        traces.append(go.Histogram(x=mouse_data[mouse_data['Drug Regimen'] == drug]['Weight (g)'],
                                   name=drug,
                                   opacity=0.9,
                                   marker=dict(color=drug_colors[drug]))
                      )

    return {
        'data': traces,
        'layout': dict(
            barmode='stack',
            xaxis={'title': 'mouse weight',
                   'range': [merged_df['Weight (g)'].min(), merged_df['Weight (g)'].max()],
                   'showgrid': False
                   },
            yaxis={'title': 'number of mice',
                   'showgrid': False,
                   'showticklabels': True
                   },
            autosize=False,
            paper_bgcolor=colors['chart-background'],
            plot_bgcolor=colors['chart-background'],
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},

            legend={'x': 0, 'y': 1},
        )
    }


# block 1-2
@app.callback(
    Output('weight-distribution', 'figure'),
    [Input('weight-distribution-radio', 'value')]
)
def update_weight_distribution(drug):
    traces = [
        go.Histogram(
            x=merged_df['Weight (g)'],
            name='all mice',
            opacity=0.5,
            marker=dict(color=colors['histogram-color-1'])
        ),
        go.Histogram(
            x=merged_df[merged_df['Drug Regimen'] == drug]['Weight (g)'],
            name=drug,
            opacity=0.75,
            marker=dict(color=drug_colors[drug])
        )
    ]

    return {
        'data': traces,
        'layout': dict(
            barmode='overlay',
            xaxis={'title': 'mouse weight',
                   'range': [merged_df['Weight (g)'].min(), merged_df['Weight (g)'].max()],
                   'showgrid': False
                   },
            yaxis={'title': 'number of mice',
                   'showgrid': False,
                   'showticklabels': True
                   },
            autosize=False,
            paper_bgcolor=colors['chart-background'],
            plot_bgcolor=colors['chart-background'],
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
        )
    }

#block 2-1
@app.callback(
    Output('secondary-survival-group-checklist', 'options'),
    [Input('primary-survival-group-checklist', 'value')]
)
def update_secondary_checklist_options(selected_groups):
    avg_weights = merged_df[merged_df['Drug Regimen'] != 'Placebo'].groupby('Drug Regimen')['Weight (g)'].mean()

    lightweight_drugs = avg_weights[avg_weights < 25].index.tolist()
    heavyweight_drugs = avg_weights[avg_weights >= 25].index.tolist()
    placebo_drugs = ['Placebo']

    options = []
    if 'Lightweight' in selected_groups:
        options.extend([{'label': drug, 'value': drug} for drug in lightweight_drugs])
    if 'Heavyweight' in selected_groups:
        options.extend([{'label': drug, 'value': drug} for drug in heavyweight_drugs])
    if 'Placebo' in selected_groups:
        options.extend([{'label': drug, 'value': drug} for drug in placebo_drugs])

    return options


@app.callback(
    Output('secondary-survival-group-checklist', 'value'),
    [Input('primary-survival-group-checklist', 'value')]
)
def update_secondary_checklist_values(selected_groups):
    avg_weights = merged_df[merged_df['Drug Regimen'] != 'Placebo'].groupby('Drug Regimen')['Weight (g)'].mean()

    lightweight_drugs = avg_weights[avg_weights < 25].index.tolist()
    heavyweight_drugs = avg_weights[avg_weights >= 25].index.tolist()
    placebo_drugs = ['Placebo']

    values = []
    if 'Lightweight' in selected_groups:
        values.extend(lightweight_drugs)
    if 'Heavyweight' in selected_groups:
        values.extend(heavyweight_drugs)
    if 'Placebo' in selected_groups:
        values.extend(placebo_drugs)

    return values


@app.callback(
    Output('survival-function-histogram', 'figure'),
    [Input('secondary-survival-group-checklist', 'value')]
)
def update_survival_function_histogram(selected_drugs):
    traces = []
    for drug in selected_drugs:
        subset = merged_df[merged_df['Drug Regimen'] == drug]
        traces.append(go.Histogram(
            x=subset['Weight (g)'],
            name=drug,
            opacity=0.75,
            marker=dict(color=drug_colors.get(drug, '#000000'))
        ))

    return {
        'data': traces,
        'layout': dict(
            barmode='stack',
            xaxis={'title': 'mouse weight',
                   'range': [merged_df['Weight (g)'].min(), merged_df['Weight (g)'].max()],
                   'showgrid': False
                   },
            yaxis={'title': 'number of mice',
                   'showgrid': False,
                   'showticklabels': False
                   },
            autosize=False,
            paper_bgcolor=colors['chart-background'],
            plot_bgcolor=colors['chart-background'],
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
        )
    }

#block 2-2
@app.callback(
    Output('survival-function-line', 'figure'),
    [Input('primary-survival-function-checklist', 'value')]
)
def update_survival_function_line(selected_groups):
    avg_weights = mouse_data[mouse_data['Drug Regimen'] != 'Placebo'].groupby('Drug Regimen')['Weight (g)'].mean()
    lightweight_drugs = avg_weights[avg_weights < 25].index.tolist()
    heavyweight_drugs = avg_weights[avg_weights >= 25].index.tolist()
    placebo_drugs = ['Placebo']

    selected_drugs = []
    if 'Lightweight' in selected_groups:
        selected_drugs.extend(lightweight_drugs)
    if 'Heavyweight' in selected_groups:
        selected_drugs.extend(heavyweight_drugs)
    if 'Placebo' in selected_groups:
        selected_drugs.extend(placebo_drugs)

    traces = []
    for drug in selected_drugs:
        subset = merged_df[merged_df['Drug Regimen'] == drug]
        time_points = sorted(subset['Timepoint'].unique())
        alive_mice = [len(subset[subset['Timepoint'] == t]) for t in time_points]
        traces.append(go.Scatter(
            x=time_points,
            y=alive_mice,
            mode='lines+markers',
            name=drug,
            marker=dict(color=drug_colors.get(drug, '#000000'))  # Default to black if not found
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': 'time point'},
            yaxis={'title': 'number of alive mice',
                   'showgrid': False},
            paper_bgcolor=colors['chart-background'],
            plot_bgcolor=colors['chart-background'],
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 1, 'y': 1, 'xanchor': 'left'},
            showlegend=True
        )
    }


#running
if __name__ == '__main__':
    app.run_server(debug=True,
                   # port = 8081, host = '0.0.0.0')
                   )
