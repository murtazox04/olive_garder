import os
import json
import django
from confluent_kafka import Consumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# from apps.models import KafkaError

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'myGroup',
    'auto.offset.reset': 'earliest'
})

# Provide a list of topic names (even if it's just one topic)
consumer.subscribe(['order_topic'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print(msg.key())

    import apps.listeners

    try:
        getattr(
            apps.listeners, msg.key().decode('utf-8'))(json.loads(msg.value()))
    except Exception as e:
        print(e)
        # KafkaError.objects.create(
        #     key=msg.key(),
        #     value=msg.value(),
        #     error=e
        # )

consumer.close()
