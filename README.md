# Student Performance Prediction System

An intuitive, data‑driven web application for early identification of at‑risk university students by analyzing lifestyle and behavioral factors. Built with Python, Flask, and machine learning, the system empowers educators and students alike with actionable insights to improve academic outcomes.

---

## 🚀 Table of Contents

1. [Overview](#overview)  
2. [Motivation & Problem Statement](#motivation--problem-statement)  
3. [Features](#features)  
4. [Architecture & Design](#architecture--design)  
5. [Tech Stack](#tech-stack)  
6. [Installation & Setup](#installation--setup)  
7. [Usage](#usage)  
8. [Project Structure](#project-structure)  
9. [Future Enhancements](#future-enhancements)  
10. [Contributing](#contributing)  
11. [License](#license)  
12. [Authors](#authors)  

---

## Overview

Traditional academic monitoring often reacts after students begin to struggle. This **Student Performance Prediction System** takes a proactive approach—collecting data on study habits, sleep patterns, extracurricular involvement, social interactions, physical activity, and stress levels—and leverages machine learning to forecast GPA and performance levels (Excellent, Good, Average, Below Average). Early warnings and personalized recommendations help students and advisors intervene before grades suffer.

---

## Motivation & Problem Statement

University students balance academics with many lifestyle factors that influence success. However, most systems focus only on grades and attendance, missing underlying causes of poor performance. Our system:

- **Identifies at‑risk students early**, enabling timely support  
- **Analyzes holistic data** (behavioral, psychological, and academic)  
- **Provides tailored recommendations** to improve study habits and well‑being  

---

## Features

### Core Functionality

- **Role‑Based Authentication**  
  - Admin, Professor, and Student roles  
  - Secure login (email & password) with hashed credentials  

- **Student Performance Prediction**  
  - Input form for key factors (study hours, sleep, social, extracurricular, exercise, stress)  
  - Predicts GPA (0.0–4.0) and classifies performance level  
  - Delivers concrete, personalized recommendations  

- **History & Reporting**  
  - Stores prediction history per student  
  - Filterable by date range, performance level, or student ID  
  - Exportable reports (e.g., PDF) for advisors and administrators  

- **User Management (Admin)**  
  - Create/edit/delete users and assign roles  
  - Manage student profiles and link to prediction records  

- **Professor Dashboard**  
  - View and update student data  
  - Run bulk predictions and monitor class performance  

- **Student Dashboard**  
  - View own prediction history  
  - Review personalized tips to boost academic success  

---

## Architecture & Design

- **MVC Pattern** with Flask for clear separation of concerns  
- **Relational Database** (SQLite/PostgreSQL) via SQLAlchemy  
- **Machine Learning Models**  
  - Experimented with Random Forest, XGBoost, and Neural Networks  
  - Trained on labeled data and evaluated with R² and RMSE metrics  
- **Data Flow**  
  1. **Collection**: User‑submitted lifestyle surveys  
  2. **Preprocessing**: Missing value imputation & feature scaling  
  3. **Prediction**: Model inference in <3 seconds  
  4. **Output**: Visualization & recommendations  


---

## Tech Stack

- **Backend**: Python 3.10+, Flask  
- **ORM**: SQLAlchemy  
- **ML**: Scikit‑learn, XGBoost  
- **Frontend**: HTML5, Bootstrap 5, Jinja2 templates  
- **Authentication**: Flask‑Login, Werkzeug password hashing  
- **Deployment**: Docker (optional), Gunicorn + Nginx  

---

 **Documentation available in the `/docs` folder**: UML diagrams, data‑flow specs, ERDs, and more.