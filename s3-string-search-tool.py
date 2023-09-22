import os
import re
import boto3
import atexit
from dotenv import load_dotenv

load_dotenv()

# GLOBAL VARS
LOCAL_FILE_NAME = os.getenv('LOCAL_FILE_NAME')
SEARCH_TYPE = os.getenv('SEARCH_TYPE')


def search_str_in_file(file_path, search_str):
    """
    It will be used to search a string in a file. It has two modes of search STRICT and LOOSE.
    It will be use to change the search type of search string in a file. If it is LOOSE then the script will loosely match the string, i.e.
    if we searching for cook in a file, but instead of cook, cooked is written in the file. In case of loose matching it will match the string.
    In case of STRICT match it will use regex to match the exact work

    :param file_path    [str]: path for the file
    :param search_str   [str]: the string that needs to be searched
    """
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()

        # this method will use string match feature to do partial match
        if SEARCH_TYPE == "LOOSE":
            # check if string present in a file
            if search_str in content:

                return True, content.count(search_str)

            else:
                return False, 0

        # this method will use regex to do the exact match
        elif SEARCH_TYPE == "STRICT":

            if re.search(r"\b" + re.escape(search_str) + r"\b", content):
                return True, 1
            else:
                return False, 0
        else:
            print("Provided SEARCH_TYPE is not correct. Possible values are STRICT or LOOSE")
            exit()


def download_file(s3_client, bucket_name, file_path, local_file_name=LOCAL_FILE_NAME):
    """
    It will be used to download the file

    :param s3_client            [object]: A S3 client object.
    :param bucket_name          [str]: S3 bucket name, that will be searched for the string.
    :param file_path            [str]: Path of the S3 file, it will be used to download it.
    :param local_file_name      [str]: Path of the local file, where the content of s3 file we be stored temporarily.
    """
    s3_client.download_file(bucket_name, file_path, local_file_name)


def traverse_s3_bucket(bucket_name, search_str):
    """
    List all objects in an S3 bucket with a given prefix.

    :param bucket_name      [str]: S3 bucket name, that will be searched for the string.
    :param search_str   [str]: the string that needs to be searched
    """
    s3_client = boto3.client('s3')

    response = s3_client.list_objects_v2(Bucket=bucket_name)

    # Iterate over the objects
    for obj in response.get('Contents', []):
        # Print the object's key (S3 path)

        # checkinf if the object has txt as extension
        if ".txt" in obj['Key']:
            download_file(s3_client, bucket_name, file_path=obj['Key'])
            word_exists, number_of_occurances = search_str_in_file(LOCAL_FILE_NAME, search_str)

            if word_exists:
                print("file path: " + obj['Key'] + ". Number of occurances: " + str(number_of_occurances))
            else:
                # print("NOT FOUND")
                pass


def traverse_s3_buckets(buckets_name_list):
    """
    It will be used to iterate on all the buckets provided by the user one by one.

    :param buckets_name_list        [list]: It contains name of the buckets that need to be searched for the string.
    """
    print("\n\n\n")
    for bucket_name in buckets_name_list:
        print("Processing bucket: " + bucket_name)
        try:
            traverse_s3_bucket(str(bucket_name), str(search_string))
        except Exception as e:
            print("S3 Client issue", str(e))
            exit()

        # registering an code exit method. It will be executed when the
        atexit.register(onExitApp)

        print("\n\n\n")


def onExitApp():
    """
    It will be called at the end of the execution and remove the local file that will store the content of the file
    """
    if os.path.isfile(LOCAL_FILE_NAME):
        os.remove(LOCAL_FILE_NAME)


if __name__ == "__main__":

    buckets_name = input("Enter the bucket name. Multiple buckets name can be provided seperate by , (comma). i.e bucket-1,bucket-2. : ").split(",")
    search_string = input("Enter the search string = <search_string>: ")

    traverse_s3_buckets(buckets_name)
