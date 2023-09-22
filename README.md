[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-black.svg)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_s3-string-search-tool&metric=bugs)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_s3-string-search-tool&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_s3-string-search-tool&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_s3-string-search-tool&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_s3-string-search-tool)

# AWS S3 String Search Tool
It contains the code base for a python script that traverse s3 buckets and search for a string. In output it will show the s3 object path that contains the string and the number of occurrences.


# Details

Follow the process given below to run this script on AWS.

## How to run the script

1. Create an IAM Policy.
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListAllMyBuckets",
                "s3:ListBucket"
            ],
            "Resource": "*"
        }
    ]
}
```
In this policy, i have used wildcard because i want the script to search a string in all S3 buckets.


2. At this step, it depends where we want to execute the script. If execution env is an EC2 instance, we can use an IAM role. If we want to run locally then we need to create an IAM user.


To run it locally:

&nbsp; a. Attach the Policy created above with IAM Group.

&nbsp; b. Create an IAM user.

&nbsp; c. Attach the IAM user to IAM Group.

&nbsp; d. Generate IAM Access Key and Secret.

&nbsp; e. Configure IAM creds on your system.

To run it on EC2:

&nbsp; a. Create an IAM role.

&nbsp; b. Attach the policy created above with the role.

&nbsp; c. Attach the role to EC2 instance.

8. Install the requirements.
```bash
pip3 install -r requirements.txt
```

9. The script can be customized with following environment variables

| Variable Name | Description | Possible Values |
|--------|-------|-------|
| LOCAL_FILE_NAME | It will be used as temporary storage for the content of an S3 file, i.e, <anything>.txt. It will be deleted at the end of script execution. |
| SEARCH_TYPE | It will be use to change the search type of search string in a file. If it is LOOSE then the script will loosely match the string, i.e. if we searching for cook in a file, but instead of cook, cooked is written in the file. In case of loose matching it will match the string. In case of STRICT match it will use regex to match the exact work | LOOSE or STRICT|

In order change the values rename `.env.example` to `.env`, and run this command to create the env vars:

```
source .env
```


10. To run the script:

```
python3 s3-string-search-tool.py
```


## How to commit the changes

1. Once the changes are made, run linting:

```
pycodestyle s3-string-search-tool.py
```

2. When doing the commit make sure to add the branch name:

Manually

```bash
git commit -m "[<branch-name>] add files"
```

In order to add the branch name automatically follow this [tutorial](https://medium.com/@aliartiza75/add-git-branch-name-to-each-commit-3acb60ab6bc9). It will also enable branch restriction on the code base, details are available in the tutorial.
