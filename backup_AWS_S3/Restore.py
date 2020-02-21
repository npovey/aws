
# File name: Restore.py
# Example: nps-MacBook-Air-2:Desktop np$ python3 program3/Restore.py text2

# Program always restores from "npovey2" bucket on AWS
# Type in any directory name to back up
# The restore recursive function was taken from
# https://stackoverflow.com/questions/31918960/boto3-to-download-all-files-from-a-s3-bucket
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#examples

import os
import sys
import boto3

# ------------------- main ------------
def main(restore_directory_name, bucket_name):
    # check if my bucket already exists
    bucket_exists = check_if_bucket_exists()
    if (bucket_exists == False):
        print('bucket ' + bucket_name + ' is not found, check again')
        return

    # at this point we must have a bucket "npovey2"
    # add directory to bucket "npovey2"
    restore_directory(restore_directory_name, bucket_name)

# ------------------- check_if_bucket_exists ------------
def check_if_bucket_exists():
    """Checks all buckets in the cloud and if bucket 'npovey2' is found returns true
    """
    resource = boto3.resource('s3')
    for bucket in resource.buckets.all():
        if(bucket.name == BUCKET_NAME):
            return True
    return False

# ------------------- download_dir ------------
def restore_directory(directory, bucket_name):
    """Download directory from the cloud
    Pre-Condition: directory must exists
    Post-Condition: The program by default puts all directories in bucket 'npovey2'
    :param client:
    :param resource: Need resource to find the bucket
    :param directory: String local directory ex: text2
    """
    resource = boto3.resource('s3')
    bucket = resource.Bucket(bucket_name)
    for key in bucket.objects.all():
        path = key.key # this is the file path string
        path_array = path.split('/')
        if(path_array[0] == directory):
            new_path = path_array[0]
            for i in range(len(path_array)-2):
                new_path = os.path.join(new_path, path_array[i+1])
            if (os.path.exists(new_path) == False):
                os.makedirs(new_path)
            resource.meta.client.download_file(bucket_name, path, path)
            print("Created: " + path)

# ------------------- run code ------------
if __name__ == '__main__':
    # bucket name hard coded, please change the name as bucket names are unique
    BUCKET_NAME = "npovey2"
    if(len(sys.argv) > 2):
        print("EX: python3 program3/Restore.py text2")
        sys.exit(0)
    directory_name = sys.argv[1]
    main(directory_name, BUCKET_NAME)
