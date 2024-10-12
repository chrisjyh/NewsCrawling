from dotenv import load_dotenv
import os

# load .env
load_dotenv()

# 키값 관리 함수
class KeyConfig:
    SENDER_ID = os.environ.get('SENDER_ID')
    SENDER_PW = os.environ.get('SENDER_PW')
    NAVER_CLIENT_ID = os.environ.get('NAVER_CLIENT_ID')
    NAVER_CLIENT_SECRET = os.environ.get('NAVER_CLIENT_SECRET')

    # 없는 키 감지
    @staticmethod
    def validate():
        required_vars = ['SENDER_ID', 'SENDER_PW', 'NAVER_CLIENT_ID', 'NAVER_CLIENT_SECRET']
        missing_vars = [var for var in required_vars if os.environ.get(var) is None]
        if missing_vars:
            raise ValueError(f"Missing variables: {', '.join(missing_vars)}")
