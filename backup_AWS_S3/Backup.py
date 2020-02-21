# N Povey
# Program 3
# File name: Backup.py
# How to run: python3 program3/Backup.py directory
# Program always backs up all files to "npovey2" bucket on AWS

import os
import sys
import logging
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import dateutil.parser
import time
    # bucket name hard coded, please change the name as bucket names are unique
BUCKET_NAME = "npovey2"
s3 = boto3.resource("s3")
BUCKET = s3.Bucket(BUCKET_NAME)

# ------------main ------------
def main(backup_directory_name):
    """Main logic to back up the directory
    All directories are backed up to 'npovey2' bucket
    :param backup_directory_name: String local path to the directory
    """
    # check if my bucket already exists
    if(check_if_bucket_exists() == False):
        create_bucket(BUCKET_NAME, 'us-west-2')
    # at this point we must have a bucket "npovey"
    # add directory to bucket "npovey"
    backup_directory(backup_directory_name)

# ------------check_if_bucket_exists ------------
def check_if_bucket_exists():
    """Checks all buckets in the cloud and if bucket 'npovey2' is found returns true
    """
    bucket = s3.Bucket(BUCKET_NAME)
    for bucket in s3.buckets.all():
        if(bucket.name == BUCKET_NAME):
            return True
    return False

# ------------backup_directory ------------
def backup_directory(directory):
    """Put folder  to a bucket in S3
    Pre-Condition: directory must exists
    Post-Condition: The program by default puts all directories in bucket 'npovey2'
    :param directory: String local directory ex: text2
    """
    # code populates the dictionary with the path and key
    bucket = s3.Bucket(BUCKET_NAME)
    new_dict = dict()
    for key in bucket.objects.all():
        new_dict.update({key.key:key});

    # os.walk generates the file names in the directory tree
    # we compare the seconds passed from files creation
    # if cloud timestamp is later than local file creation time we don't copy it
    for dirpath,dirnames,filenames in os.walk(directory): #dirpath is a directoryname
        for f in filenames:
            file_name = os.path.join(dirpath, f)
            # if file exists check the timestamp
            if file_name in new_dict:
                key = new_dict.get(file_name)
                cloudLastModified = key.last_modified.replace(tzinfo=None)
                UnixTime = (datetime(1970, 1, 1))
                cloudLastModifiedSecs = int((cloudLastModified - UnixTime).total_seconds())
                localTime = int(os.path.getmtime(file_name))
                # print(cloudLastModifiedSecs)
                # print(localTime)
                if(cloudLastModifiedSecs < localTime):
                    print("Rewrote: " + file_name)
                    write_to_bucket(file_name, BUCKET_NAME)
                else:
                    print("Already Backed Up: " + file_name)
            else:
                print("Created: " + file_name)
                write_to_bucket(file_name, BUCKET_NAME)

# ------------is_file_in_bucket ------------
def is_file_in_bucket(file_name):
    """Put folder  to a bucket in S3
    Pre-Condition: bucket_name must exist
    Post-Condition: returns boolean value
    :param file_name: String local path to the file ex: text2/hi/bc.txt
    """
    list = []
    bucket = s3.Bucket(BUCKET_NAME)
    for key in bucket.objects.all():
        list.append(key.key)
    if file_name in list:
        return True
    return False

# ------------ write_to_bucket() ------------
def write_to_bucket(file_name, bucket_name):
    """Put folder  to a bucket in S3
    Pre-Condition: bucket_name must exist
    Post-Condition: directory will be put in the given bucket
    :param file_name: String local path to the file ex: text2/hi/bc.txt
    :param bucket_name: Bucket that already exists where to put the directory
    """
    bucket = s3.Bucket(bucket_name)
    file_name.encode('utf-8').strip()

    # must include "rb" otherwise code doesn't work
    with open(file_name, 'rb') as f :
        file_data = f.read()
        bucket.put_object(Body=file_data, Bucket=bucket_name, Key=file_name)

# ------------------- create_bucket ------------
def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region
    code is taken form:
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html
    creates the bucket in the cloud with the given backet name

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# ----------------- main ------------
if __name__ == '__main__':
    directory_name = sys.argv[1]
    main(directory_name)
