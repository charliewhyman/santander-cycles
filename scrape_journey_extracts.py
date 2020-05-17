import os
import boto3
from botocore import UNSIGNED
from botocore.client import Config


s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED), region_name='eu-central-1')

# use anonymous credentials for the bucket

client = boto3.client('s3', config=Config(signature_version=UNSIGNED), region_name='eu-central-1')
bucket='cycling.data.tfl.gov.uk'
response = s3.Bucket(bucket).objects.all()

#https://stackoverflow.com/questions/57979867/how-to-download-amazon-s3-files-on-to-local-machine-in-folder-using-python-and-b
path = '../santander-cycles/data/'
if not os.path.exists(path):
    os.makedirs(path)

for item in response:
    filename = item.key.rsplit('/', 1)[-1]
    if filename.endswith('.csv'):
        s3.Object(bucket, item.key).download_file(path + filename)
        print(item.key + " Success")