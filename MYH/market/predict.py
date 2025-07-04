import pandas as pd
import pickle
import os
import joblib as j


# Load the model once (global variable)
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as file:
    model = j.load(file)



def predict_performance(form_data):
    """
    Predicts student GPA based on the provided form data using a trained ML model.

    Args:
        form_data (dict): Dictionary containing the student's metrics:
            - Study_Hours_Per_Day
            - Sleep_Hours_Per_Day
            - Social_Hours_Per_Day
            - Extracurricular_Hours_Per_Day
            - Physical_Activity_Hours_Per_Day
            - Stress_Level

    Returns:
        float: Predicted GPA
    """
    # Prepare input features in the same order used in training
    features = pd.DataFrame([{
        'Study_Hours_Per_Day': form_data.get('Study_Hours_Per_Day', 0),
        'Extracurricular_Hours_Per_Day': form_data.get('Extracurricular_Hours_Per_Day', 0),
        'Sleep_Hours_Per_Day': form_data.get('Sleep_Hours_Per_Day', 0),
        'Social_Hours_Per_Day': form_data.get('Social_Hours_Per_Day', 0),
        'Physical_Activity_Hours_Per_Day': form_data.get('Physical_Activity_Hours_Per_Day', 0),
        'Stress_Level': form_data.get('Stress_Level', 'Medium')
    }])

    # Handle categorical encoding (e.g., Stress_Level)
    # Make sure this matches your model's training preprocessing
    if 'Stress_Level' in features.columns:
            if features['Stress_Level'].dtype == 'object':
                # Convert categorical stress levels to numerical values
                 features['Stress_Level'] = features['Stress_Level'].map({
                'Low': 1,
                'Medium': 2,
                'High': 3
            }).fillna(1).astype(int)

    # Align features with training columns if needed (optional, safer)
    # model_features = model.feature_names_in_
    # features = features.reindex(columns=model_features, fill_value=0)

    # Make prediction
    prediction = model.predict(features)[0]

    return round(prediction, 2)
