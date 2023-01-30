"""
S3関連のユーティリティ
"""
from typing import Optional
import logging
import boto3
from consts import CSV_EOL


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


def s3_select(bucket: str, s3_key: str, query: str) -> Optional[str]:
    """
    S3 Selectによりレコードを取得

    Args:
        bucket (str): アップロード先のS3バケット
        s3_key (str): アップロード先のS3キー
        query (str): 実行するSQLクエリ
    Returns:
        PokemonTranslation | None: 見つかったレコードのJSON文字列、見つからなかった場合はNone
    """
    client = boto3.client("s3")
    response = client.select_object_content(
        Bucket=bucket,
        Key=s3_key,
        ExpressionType="SQL",
        Expression=query,
        RequestProgress={"Enabled": True},
        InputSerialization={
            "CSV": {
                "FileHeaderInfo": "USE",
                "RecordDelimiter": CSV_EOL,
                "FieldDelimiter": ",",
            },
            "CompressionType": "NONE",
        },
        OutputSerialization={"JSON": {"RecordDelimiter": ","}},
    )

    if "Payload" not in response.keys():
        logging.info("not found")
        return None

    # 取得した結果のサイズによっては分割されるので連結する
    event_stream = response["Payload"]
    # 分割の箇所によってはUTF8と認識できない文字コードとなるため、一旦バイナリに格納する
    payload = b""
    for event in event_stream:
        if "Records" in event.keys():
            record = event["Records"]["Payload"]
            payload += record
    return payload.decode("utf-8").removesuffix(",") if len(payload) != 0 else None
