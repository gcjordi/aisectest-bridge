# Bedrock Integration Example (Python)

```python
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='amazon.titan-text-lite-v1',
    contentType='application/json',
    body=b'{ "inputText": "Analyze this security event: login from unknown device" }'
)
print(response['body'].read())
```
