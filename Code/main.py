# Import necessary libraries
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, dash_table
from dash.exceptions import PreventUpdate
import base64
import io
from dash import dash_table
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from dash.exceptions import PreventUpdate

# Import your functions and model from other modules
from clean import *
from layout import *
from predict import *
from upload import *
from upload import connect_db
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = create_app_layout()
conn = connect_db()
# Callbacks

@app.callback(
    Output('cleaned-dataset-preview', 'children'),
    Input('clean-button', 'n_clicks'),
    State('upload-data', 'contents')
)
def clean_and_display_data(n_clicks, contents):
    
    if n_clicks and contents:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        uploaded_df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        global cleaned_df
        cleaned_df = clean_data(uploaded_df)

        # Display the top 5 data instances using dash_table.DataTable
        table = dash_table.DataTable(
            data=cleaned_df.head(5).to_dict('records'),  # Display the top 5 rows
            columns=[{'name': col, 'id': col} for col in cleaned_df.columns],
            style_table={'overflowX': 'auto'},
        )

        return table

@app.callback(
    Output('upload-status', 'children'),
    Input('upload-button', 'n_clicks'),
    State('table-name', 'value')
)
def upload_to_mysql(n_clicks, table_name):
    global tables
    tables = table_name
    if n_clicks and table_name:
        try:
            cursor = conn.cursor()

            # Create the table in MySQL
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS `{table_name}` (
                `id` INT PRIMARY KEY,
                
                `date` INT,
                `department_finishing` INT,
                `department_sweing` INT,
                
                `smv` VARCHAR(10),
                `incentive` INT,
                `over_time` INT,
                `workers` INT,
                `actual_productivity` VARCHAR(10)
            )
            """
            cursor.execute(create_table_query)

            # Upload the cleaned data to MySQL
            data_tuples = [tuple(row) for row in cleaned_df.values]

            insert_query = f"""
            INSERT INTO `{table_name}` (id, date, department_finishing, department_sweing,  smv, incentive, over_time, workers, actual_productivity)
            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.executemany(insert_query, data_tuples)
            conn.commit()

            cursor.close()

            return f"Data uploaded to MySQL with table name: {table_name}"
        except Error as e:
            return f"Error: {e}"

    return ""

@app.callback(
    Output('rmse-output', 'children'),
    Input('predict-button', 'n_clicks'),
    State('date', 'value'),
    State('finishing', 'value'),
    State('sweing', 'value'),
    State('smv-input', 'value'),
    State('incentive-input', 'value'),
    State('overtime-input', 'value'),
    State('workers-input', 'value')
)
def predict_rmse(n_clicks, date, finishing, sweing, smv, incentive, overtime, workers):
    if n_clicks:
        if 'cleaned_df' in globals():

            query = f"SELECT * FROM {tables}"
            df= pd.read_sql(query, con= conn)
            model = train_model(df)  # You need to implement this function
            user_input = np.array([[date, finishing, sweing, smv, incentive, overtime, workers]])
            predicton = model.predict(user_input)
            return f"Actual Prductivity: {predicton[0]:.2f}"
            
        else:
            return "Data is not available. Upload and clean the data first."
    else:
        raise PreventUpdate

@app.callback(
    Output('uploaded-data-info', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)


def display_uploaded_data_info(contents, filename):
    if contents is None:
        return "No file selected"
    return f'Selected file: {filename}'
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 80)
