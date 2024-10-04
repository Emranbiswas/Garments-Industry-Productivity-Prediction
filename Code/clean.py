# Clean data

import pandas as pd
import io
import base64


def clean_data(data):
    if "wip" in data.columns:
        data.drop("wip", axis = 1, inplace = True)
    if "quarter" in data.columns:
        data.drop("quarter", axis = 1, inplace = True)
    if "day" in data.columns:
        data.drop("day", axis = 1, inplace = True)
    if "team" in data.columns:
        data.drop("team", axis = 1, inplace = True)
    if "quarter" in data.columns:
        data.drop("quarter", axis = 1, inplace = True)
    if "idle_time" in data.columns:
        data.drop("idle_time", axis = 1, inplace = True)
    if "idle_men" in data.columns:
        data.drop("idle_men", axis = 1, inplace = True)
    if "no_of_style_change" in data.columns:
        data.drop("no_of_style_change", axis = 1, inplace = True)
    if "no_of_style_change" in data.columns:
        data.drop("no_of_style_change", axis = 1, inplace = True)

    if "date" in data.columns:
        data["date"] = pd.to_datetime(data["date"])
        data['date'] = data['date'].dt.dayofweek
        


    if "department" in data.columns:
        data["department"] = data["department"].str.strip()
        data = pd.get_dummies(data, columns = ['department'], dtype = int)
    if ("over_time" in data.columns and "no_of_workers" in data.columns):
        data["over_time"] = data["over_time"] / data["no_of_workers"]
        data[['over_time', 'no_of_workers']] = data[['over_time', 'incentive']].astype('int')
    
        

    data['smv'] = data['smv'].astype(str)
    data['actual_productivity'] = data['actual_productivity'].astype(str)


    #data.loc[data
    #["actual_productivity"] > 1 , "actual_productivity"] = 1
    #data['actual_productivity'] = data['actual_productivity'].round(2)
    data.reset_index(inplace=True)
    data = data[["index", 'date', 'department_finishing','department_sweing', 'smv', 'incentive','over_time','no_of_workers', 'actual_productivity']]
    data.dropna(inplace=True)
    return data