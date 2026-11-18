import requests
url="http://127.0.0.1:8000/predict"
employee_data = {
    "experience": 5.0,
    "attendance": 80.0,
    "performance": 75.0
}
response = requests.post(url, json=employee_data)
print( "STATUS CODE:", response.status_code)
print("PREDICTION RESULT:", response.json())