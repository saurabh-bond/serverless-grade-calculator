import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Event: {event}")

    message = event['Records'][0]['Sns']['Message']

    logger.info(f"Received message with grade for student: {message}")
