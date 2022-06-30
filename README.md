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

Through this process, the spaCy model is hosted on **AWS SageMaker** and can be invoked as an endpoint at any time. To create the SageMaker endpoint, we need to create our custom spaCy model container on the **AWS ECR** first and prepare our model artifact ready in the format of tar.gz.

To create the model artifact, we could do it either offline or online. Every time we finish training a spaCy model, the trained model is actually saved into a folder. The folder usually contains the following files:

*file* names might be different

- meta.json
- ner (folder)
- tokenizer
- vocab (folder)

In terms of creating the model artifact, we could simply compress this folder into a tar.gz format and upload it to a S3 bucket. Alternatively, we could also train the model online with the AWS SageMaker by creating a training job under the SageMaker Training section. But we need to provide our custom training image from AWS ECR and training data from AWS S3 bucket.

