# serve.py

import asyncio
import json
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import redis.asyncio as redis

# Create an asynchronous Redis client (make sure Redis is running on localhost:6379)
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Load the trained model (synchronously)
model = joblib.load("phishing_model.pkl")

app = FastAPI()


# Define the request and response data models
class PredictionRequest(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    prediction: str
    probability: float


@app.post("/predict", response_model=PredictionResponse)
async def predict_email(data: PredictionRequest):
    # Use the email text as a cache key
    cache_key = f"prediction:{data.text}"
    cached = await redis_client.get(cache_key)
    if cached:
        return json.loads(cached)

    # Run model inference in a thread to avoid blocking the event loop
    pred = await asyncio.to_thread(model.predict, [data.text])
    prob = await asyncio.to_thread(lambda: model.predict_proba([data.text])[0].max())

    result = {"prediction": str(pred[0]), "probability": float(prob)}

    # Cache the result for 1 hour (3600 seconds)
    await redis_client.setex(cache_key, 3600, json.dumps(result))
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
