import datetime
import time

import requests

import smtplib
from email.mime.text import MIMEText

TO_SEND_EMAILS = []
SENDER_EMAIL = ""
SENDER_PASSWORD = ""

RESERVATION_DATE = "2025.01.13"
# TIME1 : 05:00 ~ 08:00
# TIME2 : 08:01 ~ 10:00
# TIME3 : 10:00 ~ 11:20
RESERVATION_TIME = "TIME1"
# 242 : 성판악 코드
# 244 : 관음사 코드
COURSE = 242


def send_emails():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    for email in TO_SEND_EMAILS:
        msg = MIMEText("https://visithalla.jeju.go.kr/main/main.do#")
        msg["Subject"] = "한라산 가자~"
        msg["From"] = SENDER_EMAIL
        msg["To"] = email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, email, msg.as_string())
            print(f"Email sent to {email}")


def send_mails_if_available_reservation(url, payload, headers, retry_delay=5):
    attempt = 0

    while True:
        try:
            response = requests.post(url, data=payload, headers=headers)
            print(f"{datetime.datetime.now()} Attempt {attempt + 1}: Status Code = {response.status_code}")

            response_json = response.json()
            reserve_cnt = response_json['coursePerson']['reserveCnt']
            limit_cnt = response_json['coursePerson']['limitCnt']

            if limit_cnt > reserve_cnt:
                send_emails()
                print("Success:", response_json)
                return response_json
            else:
                attempt += 1
                time.sleep(retry_delay)
        except requests.exceptions.RequestException as e:
            print(f"Request Failed: {e}")
            attempt += 1
            time.sleep(retry_delay)

            return


if __name__ == "__main__":
    url = f'https://visithalla.jeju.go.kr/reservation/coursePersonAjax.do?courseSeq={COURSE}&visitDt={RESERVATION_DATE}&visitTm={RESERVATION_TIME}'

    payload = {
        "courseSeq": COURSE,
        "visitDt": RESERVATION_DATE,
        "visitTm": RESERVATION_TIME
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=UTF-8",
    }

    response = send_mails_if_available_reservation(url, payload, headers)

    if response:
        print("Final Response:", response)
    else:
        print("Failed to get a successful response after retries.")
