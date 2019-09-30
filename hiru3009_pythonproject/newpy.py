import boto3
sns = boto3.client("sns")

def handler(event, context):
    try:
        data = sns.get_topic_attributes(
            TopicArn='arn:aws:sns:us-east-1:318300609668:hirutest'
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
