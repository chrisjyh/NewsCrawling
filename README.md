# 실행
### 코드 발급 필요
- .env 파일을 생성하여 아래의 내용 작성 
```
SENDER_ID="gmail이메일 작성"
SENDER_PW="google 비밀 번호 코드"
NAVER_CLIENT_ID='네이버 api 아이디'  # 본인의 CLIENT_ID
NAVER_CLIENT_SECRET='네이버 api 시크릿 코드'  # 본인의 CLIENT_SECRET
```
- SENDER_ID
  - 키를 발급한 gmail 아이디
- SENDER_PW
  - google > 우측상단 본인 아이콘 클릭 > 구글 계정 관리 > 
    보안 > 2단계 인증 > 앱 비밀번호 > 앱이름 작성 > 코드 복사
- NAVER_CLIENT_ID
  - https://developers.naver.com/main/
    - Application > 애플리 케이션 등록 > 애플리케이션 이름 , 사용 api : 검색 선택 
    - 등록 
    - 내 애플리케이션 > application 목록 > 해당 이름 클릭 > 
    - client id
- NAVER_CLIENT_SECRET
  - client secret 보기 버튼 누르고 복사


### 사전 실행 내용
- 가상 환경이 실행 되어 있어야 함
  - Anaconda 추천
  - 파이참을 이용하면 가상 환경 자동 생성

### 실행 파일 만들기
- 실행 파일 만들기 
```
pyinstaller qtextbrowser_advanced.py
```
- 콘솔창 없애기
```
pyinstaller -w qtextbrowser_advanced.py
```
- 실행 파일 하나만 만들기 
```
pyinstaller -w -F qtextbrowser_advanced.py
```
dist 폴더 이동시 실행파일 있음
