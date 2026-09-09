import logging
import boto3
import json
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')
sns_client = boto3.client('sns')

def lambda_handler(event, context): 
    logger.info(f"Event: {event}")

    topic = os.environ.get('GRADE_CALCULATOR_TOPIC')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    obj = s3.get_object(Bucket = bucket_name, Key = file_key)

    file_contents = obj['Body'].read().decode('utf-8')
    student_records = json.loads(file_contents)

    for student in student_records:
        logger.info(f"Each student record is: {student}")
        score = student.get('testScore', 0)
        if score >= 80:
            student["grade"] = "A"
        elif score >= 60: 
            student["grade"] = "B"
        else:
            student["grade"] = "C"

        sns_client.publish(
            TopicArn = topic,
            Message = json.dumps({'default': json.dumps(student)}),
            MessageStructure = 'json'
        )
        


