# Grade Calculator

A serverless application for calculating grades from student test scores uploaded to an S3 bucket. When a file is added to the bucket, the Lambda function reads the event data, calculates the grade for each student, and publishes the result to an SNS topic. A second Lambda function listens to the SNS topic and logs the message in CloudWatch.

## Project overview

This project contains the following key components:

- `grade_calculator/gradecalculator.py` - Triggered by S3 object creation events. It reads the uploaded file from the bucket, parses the student records, calculates the grade for each student based on `testScore`, and publishes the result to SNS.
- `grade_calculator/gradereceiver.py` - Triggered by the SNS topic. It receives the published message and logs the student details with the calculated grade in CloudWatch.
- `template.yaml` - Defines the AWS SAM resources for the S3 bucket, Lambda functions, SNS topic, and IAM permissions.
- `tests/` - Contains the test setup for the project.

## Grade logic

- `testScore >= 80` -> Grade `A`
- `testScore >= 60` -> Grade `B`
- `testScore < 60` -> Grade `C`

## Deployment

To build and deploy the application:

```bash
sam build --use-container
sam deploy --guided
```

## Useful commands

```bash
sam validate
sam logs --stack-name "grade-calculator" --tail
sam delete --stack-name "grade-calculator"
```

## Notes

This project is designed around S3 events and SNS messaging, so there is no API Gateway or REST API flow involved.
