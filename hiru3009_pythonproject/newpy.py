import boto3
ddb = boto3.client("dynamodb")
s3 = boto3.client("s3")
ses = boto3.client("ses")
sns = boto3.client("sns")

def handler(event, context):
    
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
    try:
        data = s3.put_object(
            Body="test",
            Bucket="hirudinee0508",
            Key="sample"
        )
        print(data)
        """
        data = {
            "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\"",
            "VersionId": "pSKidl4pHBiNwukdbcPXAIs.sshFFOc0"
        }
        """
    except BaseException as e:
        print(e)

    try:
            data = s3.get_object(
                Bucket="hirudinee0508",
                Key="*"
            )
            print(data)
            """
            data = {
                "AcceptRanges": "bytes", 
                "ContentLength": 3191, 
                "ContentType": "image/jpeg", 
                "ETag": "\"6805f2cfc46c0f04559748bb039d69ae\"", 
                "LastModified": "<Date Representation>", 
                "Metadata": {}, 
                "TagCount": 2, 
                "VersionId": "null"
            }
            """
    except BaseException as e:
            print(e)

    try:
            data = s3.get_bucket_location(Bucket="hirudinee0508q")
            print(data)
            print('test')
            """
            data = {
                "LocationConstraint": "us-west-2"
            }
            """
    except BaseException as e:
            print(e)

        try:
            data = ddb.put_item(
                TableName='hirudB',
                Item={'name':{'S':'hiru'},'testid':{'S':'001'}}
            )
        except BaseException as e:
            print(e)
            raise(e)



    return {"message": "Successfully executed"}
