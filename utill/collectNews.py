import time
import requests
from datetime import datetime, timedelta

from utill.common import log
from utill.getKey import KeyConfig

# Naver API 설정
CLIENT_ID = KeyConfig.NAVER_CLIENT_ID
CLIENT_SECRET = KeyConfig.NAVER_CLIENT_SECRET


class NaverNewsFetcher:
    def __init__(self, keywords):
        self.keywords = keywords
        self.all_news = {}

    if CLIENT_ID == "":
        log("error", "Client ID is empty")
    if CLIENT_SECRET == "":
        log("error", "CLIENT_SECRET is empty")

    def get_news(self, keyword):
        url = 'https://openapi.naver.com/v1/search/news.json'
        headers = {
            'X-Naver-Client-Id': CLIENT_ID,
            'X-Naver-Client-Secret': CLIENT_SECRET,
        }

        params = {
            'query': keyword, # 검색어
            'display': 30,  # 뉴스 양
            'sort': 'sim',  # 정확도 순: sim, 날짜순 date
            'start': 1,
            'filter': 'all',
            'pd': 1,
            'related': 0,
            'sm' : 'tab_opt'
        }

        # 에러가 발생하면 재시도
        while True:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                log("success","NaverNewsFetcher: get news data")
                return data.get('items', [])
            elif response.status_code == 429:
                log("error", "Rate limit exceeded. Waiting for 1 minute...")
                time.sleep(60)  # 1분 대기 후 재시도
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return []


    def fetch_all_news(self):
        for keyword in self.keywords:
            news = self.get_news(keyword)

            if keyword not in self.all_news:
                self.all_news[keyword] = []
            self.all_news[keyword].extend(news)

        return self.all_news




