from kafka import KafkaConsumer, TopicPartition
import json

def calculate_pass_percentage(section, partition):
    consumer = KafkaConsumer(
        bootstrap_servers='localhost:9094',
        group_id=f'consumer-group-{section}',
        auto_offset_reset='earliest',
        enable_auto_commit=False
    )
    
    consumer.assign([TopicPartition('student_marksheets', partition)])
    
    total_students = 0
    passed_students = 0
    failed_students = []
    
    for message in consumer:
        total_students += 1
        marksheet = json.loads(message.value.decode('utf-8'))
        total_marks = marksheet["english"] + marksheet["math"] + marksheet["physics"] + marksheet["chemistry"] + marksheet["biology"]
        if total_marks > 300:
            passed_students += 1
        else:
            marksheet["total_marks"] = total_marks
            failed_students.append(marksheet)
        
        if total_students >= 6:
            break
    
    pass_percentage = (passed_students / total_students) * 100
    fail_percentage = 100 - pass_percentage
    
    print(f"Section: {section}")
    print(f"Pass percentage: {pass_percentage:.2f}%")
    print(f"Fail percentage: {fail_percentage:.2f}%")
    print(f"The failed students are")
    for student in failed_students:
        print(f"Student Name:",student["name"])
        print(f"Section:",student["section"])
        print(f"Marks")
        print(f"English:",student["english"])
        print(f"Maths:",student["math"])
        print(f"Physics:",student["physics"])
        print(f"Chemistry:",student["chemistry"])
        print(f"Biology:",student["biology"])
        print(f"Total Marks:",student["total_marks"])

calculate_pass_percentage('A', 0)
calculate_pass_percentage('B', 1)
calculate_pass_percentage('C', 2)