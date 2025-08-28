from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(10):
    log = {"level": "INFO", "message": f"Log message {i}", "timestamp": time.time()}
    producer.send('logs', value=log)
    print(f"Sent: {log}")
    time.sleep(1)

producer.flush()
