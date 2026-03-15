def get_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  Value must be at least {min_val}. Try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"  Value must be at most {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("  Please enter a valid number.")
 
 
def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  Value must be at least {min_val}. Try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"  Value must be at most {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("  Please enter a valid whole number.")
 
 
def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("  Please enter 'yes' or 'no'.")

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)
 
 
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "MODERATE"
    elif bmi < 25.0:
        return "Normal weight", "LOW"
    elif bmi < 30.0:
        return "Overweight", "MODERATE"
    elif bmi < 35.0:
        return "Obese (Class I)", "HIGH"
    else:
        return "Obese (Class II+)", "CRITICAL"
 
 
def classify_blood_pressure(systolic, diastolic):
    if systolic >= 180 or diastolic >= 120:
        return "Hypertensive Crisis", "CRITICAL"
    elif systolic >= 140 or diastolic >= 90:
        return "Hypertension Stage 2", "HIGH"
    elif systolic >= 130 or diastolic >= 80:
        return "Hypertension Stage 1", "MODERATE"
    elif systolic >= 120 and diastolic < 80:
        return "Elevated", "MODERATE"
    else:
        return "Normal", "LOW"
 
 
def classify_blood_glucose(glucose_mg_dl):
    if glucose_mg_dl < 70:
        return "Hypoglycemia", "HIGH"
    elif glucose_mg_dl <= 99:
        return "Normal", "LOW"
    elif glucose_mg_dl <= 125:
        return "Prediabetes", "MODERATE"
    else:
        return "Diabetes Range", "HIGH"

RISK_RANK = {"LOW": 0, "MODERATE": 1, "HIGH": 2, "CRITICAL": 3}
RISK_LABEL = {0: "LOW", 1: "MODERATE", 2: "HIGH", 3: "CRITICAL"}
 
 
def get_overall_risk(risk_levels):
    highest = max(RISK_RANK[r] for r in risk_levels)
    return RISK_LABEL[highest]
 
 
def get_recommendation(overall_risk):
    match overall_risk:
        case "CRITICAL":
            return "Seek emergency medical attention immediately."
        case "HIGH":
            return "Schedule a doctor's appointment within the next 48 hours."
        case "MODERATE":
            return "Consult a physician soon and monitor your vitals regularly."
        case _:
            return "Maintain your healthy lifestyle. Book an annual check-up."
 
RISK_ICON = {
    "LOW":      "[OK]     ",
    "MODERATE": "[WARN]   ",
    "HIGH":     "[HIGH]   ",
    "CRITICAL": "[URGENT] ",
}
 
DIVIDER = "-" * 58
HEADER  = "=" * 58
 
 
def print_report(name, age, bmi, bmi_status, bmi_risk,
                 systolic, diastolic, bp_status, bp_risk,
                 glucose, glucose_status, glucose_risk,
                 overall_risk, recommendation):
    print(f"\n{HEADER}")
    print(f"  HEALTH SCREENING REPORT")
    print(f"  Patient : {name}  |  Age: {age}")
    print(HEADER)
    print(f"  {'Metric':<20} {'Reading':<18} {'Status':<24} {'Risk'}")
    print(DIVIDER)
    print(f"  {'BMI':<20} {bmi:<18.1f} {bmi_status:<24} {RISK_ICON[bmi_risk]}{bmi_risk}")
    print(f"  {'Blood Pressure':<20} {f'{systolic}/{diastolic} mmHg':<18} {bp_status:<24} {RISK_ICON[bp_risk]}{bp_risk}")
    print(f"  {'Blood Glucose':<20} {f'{glucose:.1f} mg/dL':<18} {glucose_status:<24} {RISK_ICON[glucose_risk]}{glucose_risk}")
    print(DIVIDER)
    print(f"  OVERALL RISK     : {overall_risk}")
    print(f"  RECOMMENDATION   : {recommendation}")
    print(HEADER)
 
def screen_patient():
    print(f"\n{DIVIDER}")
    print("  NEW PATIENT")
    print(DIVIDER)
 
    name = input("  Patient name : ").strip().title()
    if not name:
        name = "Unknown"
 
    age = get_int("  Age (years)  : ", min_val=1, max_val=120)
 
    print("\n  -- Body Measurements --")
    weight    = get_float("  Weight (kg)  : ", min_val=1.0,  max_val=500.0)
    height_cm = get_float("  Height (cm)  : ", min_val=50.0, max_val=272.0)
    height_m  = height_cm / 100
 
    print("\n  -- Blood Pressure --")
    systolic  = get_int("  Systolic  (mmHg) : ", min_val=50,  max_val=300)
    diastolic = get_int("  Diastolic (mmHg) : ", min_val=20,  max_val=200)
 
    print("\n  -- Fasting Blood Glucose --")
    glucose = get_float("  Glucose (mg/dL)  : ", min_val=20.0, max_val=700.0)
 
    bmi = calculate_bmi(weight, height_m)
 
    bmi_status,     bmi_risk     = classify_bmi(bmi)
    bp_status,      bp_risk      = classify_blood_pressure(systolic, diastolic)
    glucose_status, glucose_risk = classify_blood_glucose(glucose)
 
    overall_risk   = get_overall_risk([bmi_risk, bp_risk, glucose_risk])
    recommendation = get_recommendation(overall_risk)
 
    print_report(
        name, age,
        bmi, bmi_status, bmi_risk,
        systolic, diastolic, bp_status, bp_risk,
        glucose, glucose_status, glucose_risk,
        overall_risk, recommendation
    )
 
    return {"name": name, "age": age, "risk": overall_risk}
 
def print_session_summary(patients):
    print(f"\n{HEADER}")
    print("  SESSION SUMMARY")
    print(HEADER)
    print(f"  Total patients screened: {len(patients)}")
    print(DIVIDER)
    print(f"  {'#':<4} {'Name':<22} {'Age':<6} {'Overall Risk'}")
    print(DIVIDER)
 
    for i, patient in enumerate(patients, start=1):
        icon = RISK_ICON[patient["risk"]]
        print(f"  {i:<4} {patient['name']:<22} {patient['age']:<6} {icon}{patient['risk']}")
 
    print(DIVIDER)
 
    critical = [p for p in patients if p["risk"] == "CRITICAL"]
    high     = [p for p in patients if p["risk"] == "HIGH"]
 
    if critical:
        names = ", ".join(p["name"] for p in critical)
        print(f"\n  [URGENT] CRITICAL patients: {names}")
        print("           Escalate to emergency care immediately.")
 
    if high:
        names = ", ".join(p["name"] for p in high)
        print(f"\n  [HIGH]   HIGH risk patients: {names}")
        print("           Schedule urgent physician consultations.")
 
    print(HEADER)
    print("  End of session. Data is not stored.")
    print(HEADER)
 
def main():
    print(HEADER)
    print("  MEDITRIAGE  |  Patient Health Screener v1.0")
    print("  Screens BMI, Blood Pressure, and Blood Glucose")
    print("  For clinical decision support only.")
    print(HEADER)
 
    screened = []
 
    while True:
        patient = screen_patient()
        screened.append(patient)
 
        if not get_yes_no("\n  Screen another patient? (yes/no): "):
            break
 
    print_session_summary(screened)
 
if __name__ == "__main__":
    main()