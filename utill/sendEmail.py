import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from utill.common import log
from utill.getKey import KeyConfig


## 이메일 전송 클레스
class EmailSender:
    def __init__(self, subject, body, receiver_email):
        self.sender_email = KeyConfig.SENDER_ID
        self.password = KeyConfig.SENDER_PW
        self.receiver_email = receiver_email
        self.subject = subject
        self.body = body

    def send_email(self):

        # 메일 생성
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = self.subject

        # 내용 추가
        msg.attach(MIMEText(self.body, 'plain'))

        try:
            # Set up the server
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail 사용
            server.starttls()  # 보안 연결
            server.login(self.sender_email, self.password)  # 로그인

            # 이메일 전송
            server.sendmail(self.sender_email, self.receiver_email, msg.as_string())
            log("success", f"Email sent successfully!")
        except Exception as e:
            log("error", f"Email Sent Error: {e}")
        finally:
            server.quit()


# Example usage
if __name__ == "__main__":
    email_sender = EmailSender(
        subject="Your Subject Here",
        body="This is the body of the email.",
        receiver_email="chrisjyh@naver.com"
    )
    email_sender.send_email()
