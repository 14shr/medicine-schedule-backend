from fastapi import FastAPI
import requests

app = FastAPI()

GIST_RAW_URL = "https://gist.githubusercontent.com/Sree14hari/c815e7714b09c85f78543ccf56df2e5b/raw/3d1ab695a90517e0ad7c032e5f8f5a790e21d43a/medications.json"

@app.get("/")
def root():
    return {"message": "Smart Medication API is running!"}

@app.get("/medications/{user_id}")
def get_medications(user_id: str):
    try:
        response = requests.get(GIST_RAW_URL)
        if response.status_code == 200:
            medications = response.json()
            user_meds = [m for m in medications if m["user_id"] == user_id]
            return user_meds
        else:
            return {"error": "Failed to fetch data from Gist."}
    except Exception as e:
        return {"error": str(e)}
