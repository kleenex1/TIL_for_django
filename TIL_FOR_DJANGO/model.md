# 모델 이해하기
* 모델은 데이터의 구조를 잡아주고 정해진 구조를 기반으로 데이터베이스와 소통을 하는 역할
* 데이터의 구조 
	* 저장할 정보들의 형태
	* 레스토랑 Menu(음식이름-문자열, 설명-문자열, 가격-정수형) 구조와 각각의 형식을 정하는것을 데이터 모델링이라고 한다. 
* 데이터베이스
	* 실제로 데이터를 저장하는 곳
	* MySQL, SQLite, Oracle..
	* SQL을 통해 CRUD 를 하게된다.
* 소통
	* python을 이용해서 데이터베이스와 소통하기 위한 도구 = ORM
	* ORM을 쓰면 파이썬을 써서 데이터베이스와 소통이 가능하다. (Object-Relational Mapper)
	* 장고가 ORM을 제공한다. 

  ![1](./model.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20201825.jpg)

  # 모델 작성하기

## 작성방법
> 사용할 데이터 확인 → 데이터 모델링 → 데이터에 맞는 field 작성 → 모델 생성 or 변경 → 장고에 반영(migrate)

* model을 작성할때 models.Model을 상속받는다.
* 사용할 데이터 확인, 데이터 모델링, field작성
* 여기서는 메뉴, 설명, 가격 데이터를 사용할 것이고 그에 맞는 field를 생성한다. 
![2](./model.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20202458.jpg)

* model을 작성하고나면 Django에게 변경사항을 알려줘야한다.
* 프로젝트 루트로 이동한다음, 
```python
python manage.py makemigrations
python manage.py migrate
```

![3](./model.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20202720.jpg)

![4](./model.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20202811.jpg)

## Field Option
[참고문서](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.Field.default)