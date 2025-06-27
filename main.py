import time
import requests
from fastapi import FastAPI

app = FastAPI()

GIST_RAW_URL = "https://gist.githubusercontent.com/Sree14hari/c815e7714b09c85f78543ccf56df2e5b/raw/3d1ab695a90517e0ad7c032e5f8f5a790e21d43a/medications.json"

@app.get("/")
def root():
    return {"message": "Smart Medication API is running!"}

@app.get("/medications/{user_id}")
def get_medications(user_id: str):
    try:
        # cache-busting with timestamp
        timestamp = int(time.time())
        url = f"{GIST_RAW_URL}?t={timestamp}"
        headers = {
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            medications = response.json()
            return [m for m in medications if m.get("user_id") == user_id]
        else:
            return {"error": "Gist fetch failed", "status": response.status_code}

    except Exception as e:
        return {"error": str(e)}
