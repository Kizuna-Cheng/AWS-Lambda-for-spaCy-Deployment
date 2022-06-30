# AWS-Lambda-for-spaCy-Deployment

My solution on how to deploy a custom spaCy model with AWS services including:

- AWS ECR (Elastic Container Registry)
- AWS SageMaker
- AWS Lambda
- AWS S3 Bucket (Optional)

Here is my plan 🧗🏻:

- First, data input can be sent as an event into the AWS Lambda.
- Second, within the Lambda, we invoke a SageMaker endpoint. The endpoint takes the data input coming from the Lambda event and returns a response containing the result from the spaCy model.
- Third, this endpoint response will display as an execution result. Hence we are able to check the response on the AWS Lambda result tab or debug on the AWS CloudWatch.

