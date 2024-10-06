from datetime import datetime

from utill.collectNews import NaverNewsFetcher
from utill.sendEmail import EmailSender


def main():
    keywords = ["현대카드", "국민카드"]
    fetcher = NaverNewsFetcher(keywords)
    all_news = fetcher.fetch_all_news()

    newxContent = ""
    # 결과 출력
    for keyword, news in all_news.items():
        newxContent += f"\n-------{keyword} 뉴스-----\n"
        for article in news:
            newxContent += (f"\n제목: {article['title']}\n"
                            f"링크: {article['link']}\n"
                            f"작성일: {article['pubDate']}\n"
                            f"요약: {article['description']}\n")

    setTitle = f"{datetime.now().strftime("%y.%m.%d")}일자 뉴스 스크립트"

    email_sender = EmailSender(
        subject=setTitle,
        body=newxContent,
        receiver_email="chrisjyh@naver.com"
    )
    email_sender.send_email()


if __name__ == "__main__":
    main()
