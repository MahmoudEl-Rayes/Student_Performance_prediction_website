from market import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(60))

class Student(db.Model):
    Student_Id = db.Column(db.Text, primary_key=True)
    Student_Name = db.Column(db.Text, nullable=False)
    Major = db.Column(db.Text, nullable=False)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Study_Hours_Per_Day = db.Column(db.Float, nullable=False)
    Extracurricular_Hours_Per_Day = db.Column(db.Float, nullable=False)
    Sleep_Hours_Per_Day = db.Column(db.Float, nullable=False)
    Social_Hours_Per_Day = db.Column(db.Float, nullable=False)
    Physical_Activity_Hours_Per_Day = db.Column(db.Float, nullable=False)
    GPA = db.Column(db.Float, nullable=False)
    Stress_Level = db.Column(db.String(10), nullable=False)
    Predicted_Score = db.Column(db.Float, nullable=False)
    Performance_Level = db.Column(db.String(20), nullable=False)
    Recommendation = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    Student_Id =db.Column(db.Text, nullable=False)