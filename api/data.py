from fastapi import FastAPI, Request, HTTPException
from pymongo import MongoClient
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi.middleware.cors import CORSMiddleware # this will help
# with CORS issues when the frontend tries to send data to the backend 
# from a different origin. You can configure it to allow requests 
# from your frontend's origin.
# CORS = Cross-Origin Resource Sharing which means allowing 
# resources to be requested from another domain outside 
# the domain from which the resource originated.
import os

app = FastAPI()

# Configure CORS to allow requests from any origin (you can 
# restrict this in production).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Read required secrets from environment.
MONGO_URI = os.environ["MONGO_URI"]
API_KEY = os.environ["API_KEY"]
NEW_YORK_TZ = ZoneInfo("America/New_York")
DATABASE_NAME = "esp32_db"
COLLECTION_NAME = "door-usage-data"

# Create Mongo objects once so each request can reuse them.
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def current_time_string():
    # Save timestamps in New York time for consistent reporting.
    return datetime.now(NEW_YORK_TZ).strftime("%Y-%m-%d %H:%M:%S")

@app.get("/api/data")
def health_check():
    return {"message": "Server is working"}

@app.post("/api/data")
async def receive_data(request: Request):
    # Accept writes only from clients with the shared API key.
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    body = await request.json()
    state = body.get("state")
    device = body.get("device", "esp32")

    if state is None:
        raise HTTPException(status_code=400, detail="Missing state")

    record = {
        "time": current_time_string(),
        "state": state,
        "device": device
    }
    collection.insert_one(record)

    return {"message": "Data saved"}

#------------------------------------------------------------------
# this will talk to the front end and give it data 
@app.get("/api/usage-per-hour")
def usage_per_hour():
    records = list(collection.find({}, {"_id": 0}))

    hourly_counts = {}

    for record in records:
        time_str = record.get("time")
        if not time_str:
            continue

        dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        hour_key = dt.strftime("%Y-%m-%d %H:00")

        if hour_key not in hourly_counts:
            hourly_counts[hour_key] = 0

        hourly_counts[hour_key] += 1

    result = []
    for hour in sorted(hourly_counts.keys()):
        result.append({
            "hour": hour,
            "count": hourly_counts[hour]
        })

    return result