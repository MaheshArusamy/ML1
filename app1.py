from fastapi import FastAPI,HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel
app = FastAPI()
class EmployeeData(BaseModel):
    experience: float
    attendance: float
    performance: float
model = joblib.load("Model/employee_model.pkl")
@app.get("/")
def home():
    return {"message": "welcome to Employee Performance Prediction API!"}
@app.post("/predict")
def predict(Employee:EmployeeData   ):
    try:
            
        input_data = pd.DataFrame([{
            "experience": Employee.experience,
            "attendance": Employee.attendance,
            "performance": Employee.performance
        }])
        prediction = model.predict(input_data)
        return{"prediction_result":prediction[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")