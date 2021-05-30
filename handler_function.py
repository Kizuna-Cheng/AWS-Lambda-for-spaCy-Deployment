import os
import io
from io import StringIO
import boto3
import json
import csv
import unicodedata
import pandas as pd

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(event))
    df = pd.DataFrame(data, columns=['COLUMN_NAME']
    
    # Define a csv buffer
    csv_buffer = io.StringIO()
                      
    # Saving a dataframe to a csv buffer (same as with a regular file):
    df.to_csv(csv_buffer, sep=",", header=True, index=False)  
                      
    # Get values from the csv buffer. 
    payload = csv_buffer.getvalue()
                      
    # Convert payload to ASCII format
    payload = unicodedata.normalize('NFKD', payload).encode('ascii', 'ignore').decode()
    
    # Invoke the Endpoint                  
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
                      
    # Set the streaming body to a variable, then read it into another variable.
    temp = response['Body']
    result = temp.read()
    
    # Stringfiy and read the byte type string into variable data.
    result=str(result,'utf-8')
    data = StringIO(result) 

    # Define column names and read data into a dataframe. 
    col_Names=["Source", "Prediction"]
    df=pd.read_csv(data, names=col_Names)
    
    # Print out the dataframe. 
    print(df)
    
    # Return the list
    pred_list =  list(df.Prediction)
    
    return pred_list                  
