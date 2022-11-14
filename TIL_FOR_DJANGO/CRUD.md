# Shell
```shell
python manage.py shell
```
* 사용자의 명령어를 받아서 해석한 다음 프로그램을 실행해준다.

# 메뉴 불러오기(가장먼저해야 할것!!)
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

* 두가지 방법으로 데이터를 저장할 수 있다.
### Create

먼저 Create는 데이터 객체를 생성하고 데이터베이스에 반영하는 과정을 한 번에 할 수 있다.

```python
data_model = {model}.objects.create( {field_name}=value, ... )
# example
# food = Food.objects.create(price=10000)
```

### Save

save를 이용하면 데이터 객체를 생성하는 타이밍과 실제로 데이터베이스에 반영하는 과정을 분리할 수 있다. 아래 코드는 위에서 사용한 Create와 똑같은 기능을 수행한다.

```python
data_model = {model}( {field_name}=value, ... )
data_model.save()
# example 
# food = Food(price=10000)
#   food.save()
```

# 데이터 조회하기(READ)
* 데이터를 데이터베이스로 부터 읽어오는 것은 Django Model Manager인 objects를 통해서 할 수 있다.
* 읽어 온 데이터는 Queryset 이라고 하는 데이터 결과 객체에 들어가며 Queryset은 파이썬의 리스트처럼 사용할 수 있다.


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
>>> 두 개 이상의 필드를 함께 사용해서 정렬할 수 있으며 '-'를 사용해서 내림차순으로 정렬할 수 있다.
>>> Menu.objects.order_by('field1','-field2')
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

* 데이터의 개수를 셀 때는 count()
```python
rows = {model}.objects.count()
```

* 특정 조건을 제외한 데이터를 조회할때 exclude()
```python
data = {model}.objects.exclude(field=value)
```

* 체인으로 연결해서 조회하기
```python
data = {model}.objects.filter(price=10000).order_by('name')
# 가격(price)이 10,000원인 데이터를 이름(name)으로 정렬해서 조회.
```

```python
data = {model}.objects.filter(price=10000)
data = data.order_by('name')
# 이렇게 적어도 위와 똑같음. 
```
### 조건 키워드

* 모든 데이터 조회는 조건 키워드를 함께 사용하여 조회할 수 있으며 **{field_name}__{keyword}={condition}** 형태로 사용.

* __exact는 대소문자를 구분해서 조건과 정확히 일치 하는지를 체크
* __iexact는 대소문자를 구분 하지 않고 일치하는 지를 체크합니다.

```python
data = {model}.objects.filter(name__iexact='chicken')
# 음식의 이름(name)이 'chicken'인 데이터를 모두 조회합니다.
# 단, 대소문자를 구분하지 않습니다.
```

* __contains, __icontains 

```python
data = {model}.objects.filter(name__contains='chicken')
# 음식의 이름(name)에 'chicken'이 포함된 모든 데이터를 조회합니다.
# 단, 대소문자를 구분합니다. (__contains)
```

* **__range**

날짜, 숫자 문자 등 모든 데이터의 범위를 사용할 수 있으며 파이썬의 range와 비슷합니다.

```python
data = {model}.objects.filter(price__range=(1000,5000))
# 가격(price)이 1000원~5000원인 모든 데이터를 조회합니다.
```
```python
import datetime
start_date = datetime.date(2020,8,12)
end_date = datetime.date(2020,9,12)
data = {model}.objects.filter(pub_date__range=(start_date,end_date))
# 생성일(pub_date)이 2020-08-12~2020-09-12인 모든 데이터를 조회합니다.
```

* **__lt , __gt, __lte, __gte**

미만 (less-than), 초과 (greater-than) 이하 (less-than-or-equal), 이상(greater-than-or-equal)인 데이터를 조회.

```python
data = {model}.objects.filter(age__gt=25)
```

* **__in**

주어진 리스트 안에 존재하는 자료를 조회.

```python
data = {model}.objects.filter(age__in=[21,25,27])
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

[장고문서](https://docs.djangoproject.com/en/3.2/topics/db/queries/)