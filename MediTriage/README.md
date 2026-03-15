Readme · MD
Copy

# MediTriage — Patient Health Screener
 
A command-line tool that screens patients for three of the most common health risk factors: BMI, blood pressure, and blood glucose. Built with pure Python and zero external libraries.
 
---
 
## The Problem It Solves
 
Community health centers and rural clinics often screen dozens of patients per session using paper forms. Staff then manually interpret each reading against clinical guidelines, which is slow and prone to human error. MediTriage automates that interpretation step. It collects vitals, flags risk levels using WHO and ADA clinical guidelines, and prints a structured report in seconds.
 
---
 
## Features
 
- Screens BMI, blood pressure (AHA guidelines), and fasting blood glucose (ADA guidelines)
- Assigns individual risk levels: LOW, MODERATE, HIGH, or CRITICAL
- Calculates an overall risk level per patient
- Generates a recommendation for each patient
- Runs a full session and prints a summary table at the end
- Flags CRITICAL and HIGH risk patients by name at the end of every session
- Validates all inputs with clear error messages (no crashes on bad input)
 
---
 
## Sample Output
 
```
==========================================================
  MEDITRIAGE  |  Patient Health Screener v1.0
  Screens BMI, Blood Pressure, and Blood Glucose
  For clinical decision support only.
==========================================================
 
----------------------------------------------------------
  NEW PATIENT
----------------------------------------------------------
  Patient name : Juan Dela Cruz
  Age (years)  : 45
 
  -- Body Measurements --
  Weight (kg)  : 88
  Height (cm)  : 168
 
  -- Blood Pressure --
  Systolic  (mmHg) : 145
  Diastolic (mmHg) : 95
 
  -- Fasting Blood Glucose --
  Glucose (mg/dL)  : 130
 
==========================================================
  HEALTH SCREENING REPORT
  Patient : Juan Dela Cruz  |  Age: 45
==========================================================
  Metric               Reading            Status                   Risk
----------------------------------------------------------
  BMI                  31.2               Obese (Class I)          [HIGH]   HIGH
  Blood Pressure       145/95 mmHg        Hypertension Stage 2     [HIGH]   HIGH
  Blood Glucose        130.0 mg/dL        Diabetes Range           [HIGH]   HIGH
----------------------------------------------------------
  OVERALL RISK     : HIGH
  RECOMMENDATION   : Schedule a doctor's appointment within the next 48 hours.
==========================================================
```
 
---
 
## How to Run
 
```bash
python meditriage.py
```
 
Python 3.10 or higher is required (uses the `match` statement).
 
---
 
## Concepts Used
 
This project was built using four core Python concepts:
 
| Concept          | Where it appears in MediTriage                                          |
|------------------|-------------------------------------------------------------------------|
| Functions        | `calculate_bmi()`, `classify_bmi()`, `get_int()`, `screen_patient()`, etc. |
| Variables & Types | `bmi` (float), `age` (int), `name` (str), `RISK_RANK` (dict)          |
| Conditionals     | `if/elif/else` in every `classify_*` function, `match` in `get_recommendation()` |
| Loops            | `while True` in all input helpers, `for` in session summary            |
| Exceptions       | `try/except ValueError` in `get_float()` and `get_int()`               |
 
---
 
## Clinical References
 
- BMI ranges: [WHO Global BMI Classification](https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)
- Blood pressure: [American Heart Association (AHA) Guidelines](https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings)
- Blood glucose: [American Diabetes Association (ADA) Standards](https://diabetes.org/about-diabetes/diagnosis)
 
---
 
## Limitations
 
- This tool is for educational and clinical decision-support purposes only.
- It is not a substitute for professional medical diagnosis.
- Patient data entered during a session is not saved or stored anywhere.
 
---
 
## Author
 
Built as a portfolio project for an Introduction to Programming course using Python.  
Concepts covered: Lecture 0 (Functions, Variables, Types), Lecture 1 (Conditionals), Lecture 2 (Loops), Lecture 3 (Exceptions).