# Seeding 시딩
## JSON , XML 파일로 만들 수 있다. 
### JSON 파일
데이터 하나를 표본으로 하나 만들고 
![1](./seeding/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-09%20131428.png)<br>
> 데이터 만들기
python manage.py dumpdata 앱이름 > 파일이름.json
python manage.py dumpdata 앱이름 --indent=2 > 파일이름.json
(아래로 입력하면 좀 더 읽기 쉬워진다.)

> 데이터 불러오기
> python manage.py loaddata 파일이름.json

# 장고 seed 
pip install django-seed

> python manage.py seed 앱이름 --number=50
> (임의의 데이터 생성)

* 유효성 검사를 거치지 않았기 때문에 일반적인 문자열은 장고 seed를 이용하더라도 별도로 관리가 필요한 데이터는 다르게 처리해야 한다.
