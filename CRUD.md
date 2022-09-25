# Shell
```shell
python manage.py shell
```
* 사용자의 명령어를 받아서 해석한 다음 프로그램을 실행해준다.

# 메뉴 불러오기
```shell
>>> from foods.models import Menu
```

# 데이터 저장하기(CREATE)
```shell
>>> Menu.objects.create(name="치킨치킨",
>>> description ="치킨 값이 올랐지만 맛있다구요",
>>> price=10000,
>>> img_path="foods/images/chicken.jpg")
```
![1](./create.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20205311.jpg)


# 데이터 조회하기(READ)

## Shell을 이용해서 조회해보기
```shell
>>> 작성한 모델 가져오기
>>> from foods.models. import Menu

>>> 전체 데이터 조회
>>> Menu.objects.all()

>>> 모든 데이터와 value를 보고 싶을때
>>> Menu.objects.all().values()

>>> 조회하고 싶은 value만 보고 싶을때 Field를 넣어준다.
>>> Menu.objects.all().values('price')

>>> 정렬하기 Order_by
>>> Menu.objects.order_by('price')
>>> Menu.objects.order_by('-price')
```


* Get을 쓸때, 데이터가 2개이상이면 오류가 나게된다. 즉 하나의 데이터를 조회할때만 사용해야 한다.(id 같은 중복되지 않는 필드 사용할때만 쓰는 것이 좋음)
```shell
>>> get : 하나의 데이터를 조회 + 조건 키워드
>>> filter : 여러 데이터를 조회 + 조건 키워드
>>>
>>> 조건 키워드
>>> 필드명__조건키워드 = '조건'
>>> ex) 필드명__contains='문자열' : 문자열이 포함된 데이터 조회
>>> ex) 필드명__range=(시작,끝) : 조건 범위 내의 데이터 조회
>>> Menu.objects.filter(name__contains='치킨')
>>> Menu.objects.filter(price__range=(2000,10000))

```
# 데이터 수정하기 & 삭제하기(Update, Delete)

* 수정하기
```shell
>>> from foods.models import Menu
>>> 변수에 데이터를 넣기
>>> data = Menu.objects.get(id=1)
>>> 데이터 확인해보기
>>> data
>>> 해당 변수의 필드값을 수정하기
>>> data.name = 후라이드 치킨
>>> 데이터 반영하기
>>> data.save()
```
* 삭제하기
```shell
>>> from foods.models import Menu
>>> 변수에 데이터를 넣기
>>> data = Menu.objects.get(id=1)
>>> 데이터 확인해보기
>>> data
>>> 삭제하기
>>> data.delete()
```
