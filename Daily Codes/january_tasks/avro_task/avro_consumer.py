from confluent_kafka.avro import AvroConsumer

config = {
    'bootstrap.servers': 'localhost:9094',
    'schema.registry.url': 'http://localhost:8081',
    'group.id': 'employee_group',
    'auto.offset.reset': 'earliest'
}

consumer = AvroConsumer(config)
consumer.subscribe(['employee_topic'])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue

        print(f"Consumed record: {msg.value()}")

except KeyboardInterrupt:
    print("Consumer interrupted")

finally:
    consumer.close()
