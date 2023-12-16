import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd
from prometheusClient import survived_counter, not_survived_counter
from prometheusClient import metrics_app, age_risk_counter
from prometheusClient import smoking_risk_counter, sex_risk_counter

app = FastAPI()
app.mount("/metrics", metrics_app)


@app.get("/predict")
def prediction_api(age: int, anaemia: int, creatinine_phosphokinase: int,
                   diabetes: int, ejection_fraction: int,
                   high_blood_pressure: int, platelets: float,
                   serum_creatinine: float, serum_sodium: int, sex: int,
                   smoking: int, time: int):
    failure_model = joblib.load("./Heart_Failure_model.joblib")
    x = [age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
         high_blood_pressure, platelets,
         serum_creatinine, serum_sodium, sex, smoking, time]
    x = pd.DataFrame([x], columns=["age", "anaemia",
                                   "creatinine_phosphokinase", "diabetes",
                                   "ejection_fraction",
                                   "high_blood_pressure", "platelets",
                                   "serum_creatinine", "serum_sodium", "sex",
                                   "smoking", "time"])
    prediction = failure_model.predict(x)
    survived = int(prediction) == 1
    if survived:
        survived_counter.inc()
    else:
        not_survived_counter.inc()

        # Calculer l'âge en groupes
        age_group = "0-40" if age <= 40 else (
            "40-70" if age <= 70 else "70-120")
        age_risk_counter.labels(age_group).inc()

        # Interpréter le statut du tabagisme
        smoking_status = "smoker" if smoking == 1 else "non-smoker"
        smoking_risk_counter.labels(smoking_status).inc()

        # Interpréter le sexe
        sex_category = "male" if sex == 1 else "female"
        sex_risk_counter.labels(sex_category).inc()
    hakim = f"est-ce qu'il va mourir : {survived}"
    return hakim


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=5000)
    uvicorn.run('api_heart_failure:app',
                host='127.0.0.1', port=8000,
                log_level='info', workers=2)
