# 한라산 예약 가능 메일 전송 스크립트
- 탐방인원이 예약 인원 미만일 경우 이메일을 발송합니다.

![reservation](/images/readme1.png)

## 스크립트 수정 시 편집
1. `TO_SEND_EMAILS` 에 보내고자 하는 메일을 리스트 형태로 추가합니다.
    예시) ["1234@naver.com", "1111@google.com"]
2. `SENDER_EMAIL` 을 메일을 보내려는 메일 주소로 수정합니다.
3. `SENDER_PASSWORD` 을 `SENDER_EMAIL`의 비밀번호로 수정합니다.
4. `RESERVATION_DATE` 를 한라산 탐방을 하고자하는 날짜 `yyyy.MM.dd` 형태로 수정합니다.
5. `RESERVATION_TIME` 를 첫번째 타임은 `TIME1`으로, 두번째 타임은 `TIME2` 로, 세번째 타임은 `TIME3` 로 변경합니다.
6. `COURSE` 는 `242` 는 성판악, `244` 는 관음사로 변경합니다.
