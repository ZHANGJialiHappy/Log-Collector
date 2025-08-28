from fastapi import FastAPI, Request
from kafka import KafkaProducer
import json
import time

app = FastAPI()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    log = {
        "method": request.method,
        "url": str(request.url),
        "status_code": response.status_code,
        "process_time": process_time,
        "timestamp": start_time
    }

    producer.send("logs", value=log)
    return response

@app.get("/")
def read_root():
    return {"message": "Hello Kafka from FastAPI!"}