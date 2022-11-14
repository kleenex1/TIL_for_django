# 마이그레이션이란?

* 장고 데이터 베이스 변경에 대한 버전컨트롤 시스템
* 변경사항을 저장해둔 목록
* 개발자가 모델을 생성하거나 변경했을때 migration을 하나씩 만들고 실제 데이터베이스에 적용하는것이 migrate이다.

![1](./migration.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20203653.jpg)

## 현재 생성되어 있는 migration 목록 보기

```python
python manage.py showmigrations
```

* [X]로 되어있는것은 Django에 이미반영되어있다는 의미
![2](./migration.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20204042.jpg)

## 어떻게 적용되어 있는지 확인해보는법
```python
python manage.py sqlmigrate foods 0001
```
![3](./migration.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20204301.jpg)



## makemigrations

```shell
python manage.py makemigrations
```

모델의 변경 사항을 인식해서 새로운 마이그레이션을 만듭니다. 이때 마이그레이션은 각 앱 디렉토리 내 migrations 디렉토리 안쪽에 생성된다.

## migrate

```shell
python manage.py migrate
```
만약 이전 마이그레이션으로 되돌리고 싶다면 python manage.py migrate {앱 이름} {되돌릴 마이그레이션 번호}를 사용할 수 있다.

## showmigrations

```shell
python manage.py showmigrations
```

현재 django 프로젝트의 모든 마이그레이션과 반영 상태를 나타냅니다. 만약 특정 앱에 대한 것만 보고 싶다면 python manage.py showmigrations {앱 이름}을 사용할 수 있다.

## sqlmigrate

```shell
python manage.py sqlmigrate {앱 이름} {마이그레이션}
```

인수로 넘겨준 마이그레이션이 ORM을 통해 변경된 SQL문을 출력합니다. sqlmigrate를 통해 모델이 의도한 대로 SQL문으로 변경되어 데이터베이스에 반영되었는지 확인할 수 있다.