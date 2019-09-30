import boto3
s3 = boto3.client("s3")
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
        print(data)
    except BaseException as e:
        print(e)
        raise(e)

        try:
            data = s3.list_objects(
                Bucket='hirudinee0508',
                MaxKeys=10,
                Prefix=''
            )
            print(data)
            """
            data = {
                "Contents": [
                   {
                      "ETag": "\"70ee1738b6b21e2c8a43f3a5ab0eee71\"",
                      "Key": "example1.jpg",
                      "LastModified": "<Date Representation>",
                      "Owner": {
                         "DisplayName": "myname",
                         "ID": "12345example25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc"
                      },
                      "Size": 11,
                      "StorageClass": "STANDARD"
                   },
                   # {...}
               ]
            }
            """
        except BaseException as e:
            print(e)
        
  

    return {"message": "Successfully executed"}
