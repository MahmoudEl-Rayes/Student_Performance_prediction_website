from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FloatField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError, NumberRange
from market.models import User

class RegisterForm(FlaskForm):
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password_confirm = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    role = SelectField(label='Role:', choices=[('user', 'Student'), ('professor', 'Professor'), ('admin', 'Admin')], validators=[DataRequired()])
    submit = SubmitField(label='Create Account')

    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError('Email Address already exists! Please try a different email address')

class LoginForm(FlaskForm):
    email_address = StringField(label='Email Address:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PredictionForm(FlaskForm):
    Student_Id = StringField(label='Student ID:', validators=[DataRequired()])
    study_hours = FloatField(label='Study Hours Per Day:', validators=[DataRequired(), NumberRange(min=0, max=24)])
    extracurricular_hours = FloatField(label='Extracurricular Hours Per Day:', validators=[DataRequired(), NumberRange(min=0, max=24)])
    sleep_hours = FloatField(label='Sleep Hours Per Day:', validators=[DataRequired(), NumberRange(min=0, max=24)])
    social_hours = FloatField(label='Social Hours Per Day:', validators=[DataRequired(), NumberRange(min=0, max=24)])
    physical_activity_hours = FloatField(label='Physical Activity Hours Per Day:', validators=[DataRequired(), NumberRange(min=0, max=24)])
    stress_level = SelectField(label='Stress Level:', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], validators=[DataRequired()])
    submit = SubmitField(label='Submit')