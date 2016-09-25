import boto3

sns = boto3.client('sns', region_name='eu-west-1')
sns.publish(
	PhoneNumber = "+886",
	Message = 'Hello World'
	)