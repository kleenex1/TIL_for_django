# 제공하지 않는 url에 접근했을 때
1. Http 404를 불러온다.
```python
from django.http import Http404
```

2. if else구문을 통해 raise 에러를 실행시킨다.
```python
raise Http404("잘못된 경로입니다!")
```
![1](./error_pages.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20200636.jpg)