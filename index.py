import json
import urllib.parse
import boto3

# boto3 AWS ka official Python tool (SDK) hai jo services se baat karta hai
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # 1. Event se Bucket ka naam nikalna
    bucket = event['Records'][0]['s3']['bucket']['name']
    
    # 2. Event se File (Object) ka naam nikalna
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        # 3. S3 se file ki details fetch karna
        response = s3.get_object(Bucket=bucket, Key=key)
        
        print(f"SUCCESS: File {key} found in bucket {bucket}")
        print(f"CONTENT TYPE: {response['ContentType']}")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'File {key} processed successfully!')
        }
    except Exception as e:
        print(e)
        print(f"ERROR: File process nahi ho payi.")
        raise e
