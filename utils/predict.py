import os
import json
import pandas as pd
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split

def predict_disaster(date, location):
    """Loads data from the JSON file."""
    try:
        with open(os.path.join(os.path.dirname(__file__), '../data/data.json'), 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise ValueError("data.json file not found")
    
    # Create DataFrame
    df = pd.DataFrame(data)

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Feature engineering: Extract day and month
    df['Day'] = df['Date'].dt.day
    df['Month'] = df['Date'].dt.month

    # Define features and target variable
    features = ['Temperature (C)', 'Humidity (%)', 'Precipitation (mm)', 'Day', 'Month']
    target = 'Disaster'

    # Split data into features and target variable
    X = df[features]
    y = df[target]

    # Set feature names explicitly
    X.columns = features

    # Initialize Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    rf_classifier.fit(X.values, y)

    # Input today's date and location
    input_date = date
    input_location = location

    
    # Convert input date to datetime
    input_date = datetime.strptime(input_date, '%m/%d/%Y')

    output = []
    # Predict for the next week (7 days)
    for day in range(1, 8):
        # Generate future date
        future_date = input_date + timedelta(days=day)
        
        # Extract day and month
        future_day = future_date.day
        future_month = future_date.month
        
        # Create input features
        input_features = [[25, 75, 5, future_day, future_month]]  # Assuming constant weather conditions
        
        # Make prediction
        prediction = rf_classifier.predict(input_features)[0]
        
        # Interpret prediction
        if prediction == 'None':
            output.append(f"On {future_date.strftime('%m/%d/%Y')}, there is no predicted disaster risk in {input_location}.")
        else:
            output.append(f"Alert: {prediction} can happen in {input_location} after {day} days, be careful.")
        
    # return the results
    return output