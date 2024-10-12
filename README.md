# 실행
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