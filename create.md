# Shell
```shell
python manage.py shell
```
* 사용자의 명령어를 받아서 해석한 다음 프로그램을 실행해준다.

## 메뉴 불러오기
```shell
>>> from foods.models import Menu
```

## 데이터 조회하기(READ)
```shell
>>> Menu.objects.all()
```

## 데이터 저장하기(CREATE)
```shell
>>> Menu.objects.create(name="치킨치킨",
>>> description ="치킨 값이 올랐지만 맛있다구요",
>>> price=10000,
>>> img_path="foods/images/chicken.jpg")
```
![1](./create.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20205311.jpg)

## 세부 데이터까지 보기
```shell
>>> Menu.objects.all().values()
```
![2](./create.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20205758.jpg)