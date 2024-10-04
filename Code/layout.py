import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
def create_app_layout():
    # Data cleaning section and Data upload section
    data_cleaning_card = dbc.Col(
        dbc.Card([
            dbc.CardHeader("Data Cleaning"),
            dbc.CardBody([
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    multiple=False
                ),
                html.Div(id='uploaded-data-info'),
                dbc.Button("Clean Data", id='clean-button', color="primary", className="mt-2"),
                html.Div(id='cleaned-dataset-preview'),
            ]),
        ], className="mb-4"),
        width=6
    )

    upload_to_mysql_card = dbc.Col(
        dbc.Card([
            dbc.CardHeader("Upload to MySQL"),
            dbc.CardBody([
                dbc.Input(id='table-name', type='text', placeholder='Enter Table Name'),
                dbc.Button("Upload Data to MySQL", id='upload-button', color="primary", className="mt-2"),
                html.Div(id='upload-status', className="mt-2"),
            ]),
        ], className="mb-4"),
        width=6
    )
    blank_card = dbc.Col(
        
        width=6
    )

    user_input_card = dbc.Col(
        dbc.Card([
            dbc.CardHeader("Input Parameters"),
            dbc.CardBody([
                dbc.Label("Select Date", className="mb-2"),
                dcc.Input(id='date', type='number', placeholder='Enter Date', style={'width': '100%'}),
                dbc.Label("Department Finishing", className="mb-2"),
                dcc.Input(id='finishing', type='number', placeholder='0', style={'width': '100%'}),
                dbc.Label("Department Sweing", className="mb-2"),
                dcc.Input(id='sweing', type='number', placeholder='0', style={'width': '100%'}),
                dbc.Label("SMV", className="mb-2"),
                dcc.Input(id='smv-input', type='number', placeholder='SMV', style={'width': '100%'}),
                dbc.Label("Incentive", className="mb-2"),
                dcc.Input(id='incentive-input', type='number', placeholder='Incentive', style={'width': '100%'}),
                dbc.Label("Overtime", className="mb-2"),
                dcc.Input(id='overtime-input', type='number', placeholder='0', style={'width': '100%'}),
                dbc.Label("Number of Workers", className="mb-2"),
                dcc.Input(id='workers-input', type='number', placeholder='Number of Workers', style={'width': '100%'}),
                dbc.Button("Predict", id='predict-button', color="primary", className="mt-2"),
            ]),
        ], className="input-section mb-4"),
        width=6
    )
    blank_card2 = dbc.Col(
        
        width=12
    )
    predicted_rmse_card = dbc.Col(
        dbc.Card([
            dbc.CardHeader("Predicted RMSE"),
            dbc.CardBody([
                html.Div(id='rmse-output', className="lead"),
            ]),
        ], className="mb-4"),
        width=12
    )

    # Create the main layout
    app_layout = dbc.Container([
        html.H1("Industrial Predictive Maintenance Software", className="mt-4 text-center"),  # App Heading
        dbc.Row([
            data_cleaning_card,
            upload_to_mysql_card,
            blank_card,
            user_input_card,
            blank_card2,
            predicted_rmse_card,
        ], justify="between"),
    ], fluid=True)

    return app_layout