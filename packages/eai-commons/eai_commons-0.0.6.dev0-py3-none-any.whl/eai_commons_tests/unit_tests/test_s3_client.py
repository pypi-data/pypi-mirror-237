import os
import shutil

from eai_commons.s3_client import S3Client
from eai_commons.utils.file import file_relative_path

client = S3Client(
    os.getenv("S3_ENDPOINT"),
    False,
    os.getenv("S3_ACCESS_KEY_ID"),
    os.getenv("S3_ACCESS_KEY_SECRET"),
    os.getenv("S3_HDY_BUCKET_NAME"),
)


def test_s3_client_crud():
    local_file = file_relative_path(__file__, "../resources/csv_file.csv")
    s3_file_suff_path = "eai_common_test/csv_file.csv"
    download_dir = file_relative_path(__file__, "../resources/test")
    with open(local_file, "rb") as file:
        bytes_ = file.read()
        client.upload_s3_object(bytes_, s3_file_suff_path)

    files_ = client.list_s3_files("/eai_common_test")
    assert s3_file_suff_path in files_

    client.download_s3_files_local([s3_file_suff_path], download_dir)

    client.delete_file(s3_file_suff_path)
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)
