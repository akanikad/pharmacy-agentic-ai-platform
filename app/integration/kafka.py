import json
import os

def publish_event(topic: str, event: dict):
    # Local demo remains safe when Kafka is unavailable.
    try:
        from confluent_kafka import Producer
        producer = Producer({
            "bootstrap.servers": os.getenv(
                "KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"
            )
        })
        producer.produce(topic, json.dumps(event).encode("utf-8"))
        producer.flush(1)
        return True
    except Exception:
        return False
