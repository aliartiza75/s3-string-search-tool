import os
import boto3
import atexit

# GLOBAL VARS
LOCAL_FILE_NAME = "local_file.txt"


def search_str_in_file(file_path, word):
    """
    It will be used to search a string in a file
    """
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:

            return True, content.count(word)

        else:
            return False, 0


def download_file(s3_client, bucket_name, file_path, local_file_name=LOCAL_FILE_NAME):
    """
    It will be used to download the file
    """
    s3_client.download_file(bucket_name, file_path, local_file_name)


def traverse_s3_bucket(bucket_name, search_str):
    """
    Recursively list all objects in an S3 bucket with a given prefix.

    :param bucket_name: The name of the S3 bucket.
    :param prefix: The prefix (folder path) to start from.
    """
    s3_client = boto3.client('s3')

    # List objects in the specified bucket with the given prefix
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    # Iterate over the objects
    for obj in response.get('Contents', []):
        # Print the object's key (S3 path)
        if "txt" in obj['Key']:
            download_file(s3_client, bucket_name,file_path=obj['Key'])
            word_exists, number_of_occurances = search_str_in_file(LOCAL_FILE_NAME, search_str)

            if word_exists:
                print("file path: " + obj['Key'] + ". Number of occurances: " + str(number_of_occurances))
            else:
                # print("NOT FOUND")
                pass

def traverse_s3_buckets(buckets_name_list):
    """
    It will be used to iterate on all the buckets provided by the user one by one.
    """
    print("\n\n\n")
    for bucket_name in buckets_name_list:
        print("Processing bucket: " + bucket_name)
        traverse_s3_bucket(str(bucket_name), str(search_string))

        print("\n\n\n")


def onExitApp():
    """
    It will be called at the end of the execution and remove the local file
    """
    os.remove(LOCAL_FILE_NAME)


if __name__ == "__main__":

    atexit.register(onExitApp)
    buckets_name = input("Enter the bucket name. Multiple buckets name can be provided seperate by , (comma). i.e bucket-1,bucket-2. : ").split(",")
    search_string = input("Enter the search string = <search_string>: ")


    traverse_s3_buckets(buckets_name)