#  SNU_AIAM
서울대학교 UX연구실의 AI Article Mining Tool 입니다.

## 1. 프로그램 소개
본 프로그램은 서울대학교 UX연구실에서 연구목적으로 제작한 Article Mining Tool입니다.

IBM Watson의 AlchemyAPI를 사용하였습니다.

## 2. 사용환경
본 프로그램을 사용하시기 위해서는 Python3.5.2가 설치되어 있어야 합니다.

## 3. 사용법
### 3.1.  API KEY 발급
1. IBM**[bluemix](http://console.ng.bluemix.net/)** 에서 회원가입을 합니다.
2. AlchemyAPI 앱을 추가 하고 신임 정보에서 Key를 확인합니다

### 3.2. 프로그램 사용
1. 본 프로그램을 다운로드하거나 복제합니다.
2. alchemyapi.py 파일 149행의 key값에 bluemix에서 받은 key값을 입력합니다.
3. concept_url2.py를 실행합니다.
4. 없는 모듈들은 pip 등을 이용해 설치합니다.
