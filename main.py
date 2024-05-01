from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class Data(BaseModel):
    features: list  # Asegúrate de ajustar esto según cómo necesitas recibir los datos

model = joblib.load("casis_svm_model.pkl")  # Asegúrate de que el modelo está en el path correcto

@app.post("/predict/")
def predict(data: Data):
    prediction = model.predict([data.features])
    return {"prediction": prediction.tolist()}
