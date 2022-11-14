# 파이썬 함수 사용 팁

# 함수를 정의하는 네가지 방법

## 1. 매개변수와 반환 값이 없는 형태(기본형태)
* 호출할 때는 함수명()을 이용해서 호출한다.

```python
def 함수명():
    로직 ...

#example
def greetings():
    print("Hello!")
```

## 2. 매개변수는 없지만 반환 값은 있는 형태
* 호출할 때는 함수명()을 이용해서 호출한다.

```python
def 함수명():
    return 반환 값

#example
def get_pi():
    pi = 3.141592
    return pi
```

## 3. 매개변수는 있지만 반환 값이 없는 형태

호출할 때는 전달 인자를 넣어서 함수명(전달 인자) 형태로 호출

```python
def 함수명(매개변수1, 매개변수2, ...):
    로직 ...

#example
def display(name, age):
    print("Name: ", name, "Age: ", age)
```

## 4. 매개변수와 반환 값이 모두 있는 형태

가장 많이 쓰이는 형태: 
호출할 때는 전달 인자를 넣어서 함수명(전달 인자) 형태로 호출합니다.

```python
def 함수명(매개변수1, 매개변수2, ...):
    로직 ...
    return 반환 값

#example
def index_view(request):
    return render(request, "<h1>템플릿 입니다.</h1>")
```

# 인자를 전달하는 두가지 방법

## 위치 전달 인자(Positional Arguments)

* 즉 매개변수가 정의된 위치에 맞게 인자가 전달되는 방식.

```python
# 함수 정의
def calc(a, b, c):
   result = 100 * a + 10 * b + c
   print(result)
   return result

# 함수 호출
calc(1, 2, 3)

# 결과
123
```

## 키워드 전달 인자(Keyword Arguments)

```python
# 함수 정의 (위와 동일해요)
def calc(a, b, c):
   result = 100 * a + 10 * b + c
   print(result)
   return result

# 함수 호출
calc(a=1, b=2, c=3)

# 결과
123
```

```python
# 함수 호출
calc(c=1, a=2, b=3)

# 결과
231
```

