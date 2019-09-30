import boto3
ses = boto3.client("ses")
sns = boto3.client("sns")

def handler(event, context):
    
    try:
        data = ses.send_email(
    		Destination={
    		    "ToAddresses": ['hirudineel@gmail.com'],
    			"CcAddresses": [],
    			"BccAddresses": []
    		},
    		Message={
    			"Body": {
    			    "Text": {
    					"Data": 'Sample body'
    				}
    			},
    			"Subject": { 
    				"Data": 'This is a test'
    			}
    		},
    		Source='hirudinee@adroitlogic.com'
        )
    except BaseException as e:
        print(e)
        raise(e)
  

    return {"message": "Successfully executed"}
