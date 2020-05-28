import os
import boto3
from botocore import UNSIGNED
from botocore.client import Config


s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED), region_name='eu-central-1')

# use anonymous credentials for the bucket

client = boto3.client('s3', config=Config(signature_version=UNSIGNED), region_name='eu-central-1')
bucket='cycling.data.tfl.gov.uk'
response = s3.Bucket(bucket).objects.all()

#If the /data folder does not exist, create it
path = '../santander-cycles/data/'
if not os.path.exists(path):
    os.makedirs(path)

# download each new .csv file in the bucket
for item in response:
    filename = item.key.rsplit('/', 1)[-1]
    
    if not(os.path.isfile(path + filename)) and filename.endswith('.csv'):
        s3.Object(bucket, item.key).download_file(path + filename)
        print(item.key + " Success")
