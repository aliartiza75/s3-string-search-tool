[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-black.svg)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_s3-string-search-tool&metric=bugs)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_s3-string-search-tool&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_s3-string-search-tool&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_s3-string-search-tool&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)

# AWS S3 String Search Tool
It contains the code base for a python script that traverse s3 buckets and search for a string. In output it will show the s3 object path that contains the string and the number of occurrences.


# Details

Follow the process given below to run this script on AWS.

1. Create an IAM Policy.

2. Create an IAM Group.

3. Attach the Policy created above with IAM Group.

4. Create an IAM user.

5. Attach the IAM user to IAM Group.

6. Generate IAM Access Key and Secret.

7. Configure IAM creds on your system.

8. Install the requirements.
```bash
pip3 install -r requirements.txt
```

9. The script can be customized with following environment variables
| Variable Name | Description | Possible Values |
|--------|-------|-------|
| LOCAL_FILE_NAME | It will be used as temporary storage for the content of an S3 file | <anything>.txt |
| SEARCH_TYPE | It will be use to change the search type of search string in a file. If it is LOOSE then the script will loosely match the string, i.e. if we searching for cook in a file, but instead of cook, cooked is written in the file. In case of loose matching it will match the string. In case of STRICT match it will use regex to match the exact work | LOOSE or STRICT|




10.
