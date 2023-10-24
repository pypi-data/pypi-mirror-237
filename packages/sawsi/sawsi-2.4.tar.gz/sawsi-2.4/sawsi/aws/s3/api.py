from sawsi.aws import shared
from sawsi.aws.s3 import wrapper
from secrets import token_urlsafe
import json


class S3API:
    """
    S3 를 활용하는 커스텀 ORM 클래스
    """
    def __init__(self, bucket_name, credentials=None, region=shared.DEFAULT_REGION):
        """
        :param bucket_name:
        :param credentials: {
            "aws_access_key_id": "str",
            "aws_secret_access_key": "str",
            "region_name": "str",
            "profile_name": "str",
        }
        """
        self.boto3_session = shared.get_boto_session(credentials)
        self.cache = {}
        self.bucket_name = bucket_name
        self.s3 = wrapper.S3(self.boto3_session, region=region)

    def init_s3_bucket(self, acl='private'):
        """
        실제 버킷 생성
        :return:
        """
        return self.s3.init_bucket(self.bucket_name, acl)

    def upload_binary(self, file_name, binary):
        return self.s3.upload_binary(self.bucket_name, file_name, binary)

    def delete_binary(self, file_name):
        return self.s3.delete_binary(self.bucket_name, file_name)

    def download_binary(self, file_name):
        return self.s3.download_binary(self.bucket_name, file_name)

    def upload_file_and_return_url(self, file_bytes, extension, content_type, use_accelerate=False):
        """
        파일을 업로드하고 URL 을 반환합니다.
        만천하에 공개되기 때문에 공개해도 괜찮은 파일만 사용해야 함.
        :param file_bytes:
        :param extension:
        :param content_type:
        :param use_accelerate:
        :return:
        """
        if use_accelerate:
            base_url = f'https://{self.bucket_name}.s3-accelerate.amazonaws.com/'  # 전송 가속화
        else:
            base_url = f'https://{self.bucket_name}.s3.{self.s3.region}.amazonaws.com/'
        file_id = f'{token_urlsafe(32)}.{extension}'
        response = self.s3.upload_file(self.bucket_name, file_bytes, file_id, content_type, 'public-read')
        return base_url + file_id

    def upload_items_for_select(self, file_name: str, item_list: [dict]):
        """
        Select Query 를 위해서 JSON LIST 로 만들어서 업로드합니다.
        :param file_name:
        :param item_list: [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35}
        ]
        :return:
        """
        # item_list의 타입을 확인하여 리스트인지 확인
        if not isinstance(item_list, list):
            raise ValueError("item_list은 리스트 타입이어야 합니다.")

        # item_list의 각 항목이 딕셔너리인지 확인
        for item in item_list:
            if not isinstance(item, dict):
                raise ValueError("item_list의 각 항목은 딕셔너리 타입이어야 합니다.")

        json_string = '\n'.join([json.dumps(item) for item in item_list])
        response = self.upload_binary(file_name, json_string.encode('utf-8'))
        return response

    def select(self, file_name, query):
        """
        S3 Select 를 이용해 파일에서 쿼리합니다.
        :param file_name:
        :param query: SQL
        :return: [
            {
                key: value, ...
            }, ...
        ]
        """
        input_serialization = {'JSON': {'Type': 'DOCUMENT'}}
        output_serialization = {'JSON': {}}
        response = self.s3.select_object_content(
            self.bucket_name, file_name, query, input_serialization, output_serialization
        )
        for event in response['Payload']:
            if 'Records' in event:
                # 결과 데이터 처리
                records = event['Records']['Payload'].decode('utf-8')
                items = records.split('\n')
                items = [json.loads(item) for item in items if item]
                return items
            elif 'Progress' in event:
                print('S,', event)
        return []
