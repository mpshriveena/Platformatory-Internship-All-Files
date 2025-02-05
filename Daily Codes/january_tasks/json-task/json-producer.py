import json
from kafka import KafkaProducer

bootstrap_servers = ['localhost:9094']

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_marks(section, partition):
    with open(f"marksheets-{section}.json", 'r') as file:
        marksheets = json.load(file)
    for marksheet in marksheets:
        producer.send('student_marksheets', value=marksheet, partition=partition)    
    print(f"Marksheets generated for Section {section}")

generate_marks('A', 0)
generate_marks('B', 1)
generate_marks('C', 2)

producer.flush()
producer.close()