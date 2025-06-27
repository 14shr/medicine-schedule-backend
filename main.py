import time
import requests
from fastapi import FastAPI

app = FastAPI()

# This URL will ALWAYS fetch the latest Gist content
GIST_RAW_URL = "https://gist.githubusercontent.com/Sree14hari/c815e7714b09c85f78543ccf56df2e5b/raw"

@app.get("/medications/{user_id}")
def get_medications(user_id: str):
    try:
        # Force fresh fetch with timestamp
        url = f"{GIST_RAW_URL}?t={int(time.time())}"
        response = requests.get(url, headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
        })

        if response.status_code == 200:
            medications = response.json()
            return [m for m in medications if m.get("user_id") == user_id]
        return {"error": f"Failed to fetch (HTTP {response.status_code})"}

    except Exception as e:
        return {"error": str(e)}
