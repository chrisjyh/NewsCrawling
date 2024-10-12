from datetime import datetime

from utill.collectNews import NaverNewsFetcher
from utill.sendEmail import EmailSender

# 전체 적인 실행 정리
def ActionMain(selected_card, emails):
    print(f"입력 받은 값 {selected_card}"
          f""
          f"이메일 {emails}")

    # 입력받은 문자열 배열로 변환
    keywords = [card.strip() for card in selected_card.split(',')]
    fetcher = NaverNewsFetcher(keywords)
    all_news = fetcher.fetch_all_news()

    newxContent = ""
    # 결과 출력
    for keyword, news in all_news.items():
        newxContent += f"\n-------{keyword} 뉴스-----------\n"
        for article in news:
            newxContent += (f"\n제목: {article['title']}\n"
                            f"링크: {article['link']}\n"
                            # f"작성일: {article['pubDate']}\n"
                            f"요약: {article['description']}\n")

    setTitle = f"{datetime.now().strftime("%y.%m.%d")}일자 뉴스 스크립트"\

    print(setTitle)

    # 이메일 전송
    for email in emails:

        email_sender = EmailSender(
            subject=setTitle,
            body=newxContent,
            receiver_email=email
        )
        email_sender.send_email()
