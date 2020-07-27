# S3 Python Uploader
## Configuration file
```json
{
	"aws_access_key_id": "aws_access_key_id",
	"aws_secret_access_key": "aws_secret_access_key",
	"endpoint_url": "https://s3.fr-par.scw.cloud",
	"region": "fr-par"
}
```

## Python code
```python
import json
import boto3
from os import listdir
from os.path import isfile, join
from botocore.exceptions import ClientError

settings = json.load(open(f"scaleway_s3.json"))
s3 = boto3.client('s3',
                  region_name=settings["region"],
                  endpoint_url=settings["endpoint_url"],
                  aws_access_key_id=settings["aws_access_key_id"],
                  aws_secret_access_key=settings["aws_secret_access_key"]
                  )
BUCKET = "agile-radiolab-shared"
PREFIX = "data/latency-210720"

folders = {
    "/home/epc1/dev/GoProjects/src/github.com/igorskh/zmq-latency/bin/scenario1_auto": "scenario1",
    "/home/epc1/dev/GoProjects/src/github.com/igorskh/zmq-latency/bin/scenario2_auto": "scenario2"
}

remote_objects = s3.list_objects(Bucket=BUCKET, Prefix=PREFIX)
searchable_objects = [obj["Key"].split("/")[-1]
                      for obj in remote_objects["Contents"]]


def upload_file(fpath, bucket, object_name):
    try:
        s3.upload_file(fpath, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def process_file(path, folder_id):
    if not path[1] in searchable_objects:
        full_path = f"{path[0]}/{path[1]}"
        object_path = f"{PREFIX}/{folder_id}/{path[1]}"
        print(f"Uploading... {path[1]} to {folder_id}")
        upload_file(full_path, BUCKET, object_path)


def process_folder(path, folder_id):
    print(f"Checking {path}...")
    files = [(path, f) for f in listdir(path) if isfile(join(path, f))]
    for f in files:
        process_file(f, folder_id)


def main():
    for path in folders:
        process_folder(path, folders[path])


if __name__ == "__main__":
    main()
```