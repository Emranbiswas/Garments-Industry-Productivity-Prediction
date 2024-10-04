# predictive_model.py
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def train_model(data):
    #data['targeted_productivity'] = data['targeted_productivit'].astype(str)
    data['smv'] = data['smv'].astype(float)
    data['actual_productivity'] = data['actual_productivity'].astype(float)
    
    X = data[['date', 'department_finishing','department_sweing', 'smv', 'incentive', 'over_time', 'workers']]
    y = data['actual_productivity']



    # Create and train the Random Forest model
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    model.fit(X, y)
    return model


    

