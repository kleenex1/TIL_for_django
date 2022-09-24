# MVT 구조
* `URL - View - 함수 호출 - 모델 - 데이터베이스 - View - Template - 화면`의 구조에서 마지막 `View- Template - 화면`을 만드는 과정

* View에서 로직을 만든다.

# 날짜 데이터 생성하기(동적웹페이지)
```python
from datetime import datetime
```
* datetime을 불러온다.
```python
def index(request):
    today = datetime.today()
    print(today)

    return render(request, 'foods/index.html')
```

![1](./dynamic.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20185926.jpg)
* today가 어떻게 나오는지 궁금하면 print를 이용하여 runserver를 하고 콘솔창에서 확인한다.

```python
def index(request):
    today = datetime.today().date()
    context = {"date": today}
 
    return render(request, 'foods/index.html', context=context)
```
* today라는 변수에 담고,  context 변수를 render함수의 3번째 파라미터로 넘겨준다.

# View에서 넘겨받은 값으로 변환
* 템플릿 변수를 활용한다.
![2](./dynamic.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20190551.jpg)