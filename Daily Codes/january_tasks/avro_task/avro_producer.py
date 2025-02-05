import json
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

with open('avro_schema.avsc', 'r') as schema_file:
    value_schema = avro.loads(schema_file.read())

with open('avro_data.json', 'r') as data_file:
    employee_data = json.load(data_file)

config = {
    'bootstrap.servers': 'localhost:9094',
    'schema.registry.url': 'http://localhost:8081'
}

producer = AvroProducer(config, default_value_schema=value_schema)

for record in employee_data:
    producer.produce(topic='employee_topic', value=record)

producer.flush()

print("Employee data successfully produced!")
