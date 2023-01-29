"""
S3関連のユーティリティ
"""
import boto3


def s3_upload(file_path: str, bucket: str, s3_key: str) -> None:
    """
    s3へファイルをアップロードします

    Args:
        file_path (str): アップロード対象のローカルファイル
        bucket (str): アップロード先のS3バケット
        s3_key (str): アップロード先のS3キー
    """
    client = boto3.client("s3")
    client.upload_file(file_path, bucket, s3_key)
