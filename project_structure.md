# 장고 프로젝트의 구조
![1](./project_structure.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20165641.jpg)

`django_practice` : Project Root: django 프로젝트의 모든 파일이 담겨 있는 최상위 디렉토리

`manage.py` : django 프로젝트 관리를 위한 명렁어 지원, 앱생성, 데이터베이스 관련명령, 개발서버 실행 등
  
`db.sqlite3` : 프로젝트에서 사용하는 데이터베이스 파일

하위 `django_pratice` : Project App, 가장 중심이 되는 App

`__init__.py` : 디렉토리를 하나의 파이썬 패키지로 인식되게 하는 역할, python3.3부터는 이 파일이 없어도 python 패키지로 인식(하위버전 호환용)

`asgi.py` : Asynchronous Server Gateway interface, Django가 비동기식 웹서버와 연결 및 소통하는 것을 도움

`settings.py` : 프로젝트의 시간대설정, 데이터베이스 설정, 경로 설정, 전반적인 설정 담당

`urls.py` : url을 보고 알맞은 페이지로 연결해주는 역할

`wsgi.py` : Web Server Gateway Interface, 웹서버와 python 어플레케이션인 Django가 소통하는데 필요한 일종의 프로토콜

# 장고 어플리케이션 구조
![2](./project_structure.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20170512.jpg)

`migrations` : 데이터베이스 변경사항 히스토리 누적

`admin.py` : 앱을 django 관리자와 연동하기 위해 필요한 설정파일

`apps.py` : 앱에 대한 설정

`models.py` : django app에서 사용할 데이터 모델 정의, 데이터베이스 연동과 관련된 파일

`tests.py` : 테스트 코드 작성하는 곳

`views.py` : 중요. django app의 메인 로직 처리와 관련된 파일