# View와 Template 활용하기
* view에서 food로 받은 인자를 활용하기 위해선,
* context 변수를 빈 사전으로 만들어준다.
* food가 chicken이라면, name이라는 key에 이름을 넣고, description이라는 key에 설명을 넣고, price라는 key에 가격을 넣어준다.
![1](./template_and_view.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20195315.jpg)


# {% get_static_prefix %}
* 먼저 이미지는 정적경로를 이용한다. 
```python
{% load static %}
```
* 탬플릿 태그 안에 템플릿 변수를 중첩해서 사용할 수 없다.
```python
<img src = {% static {{img_path}} %}/>
```
* get_static_prefix
```python
<img src = {% get_static_prefix %}{{img_path}}/>
```
![2](./template_and_view.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20195735.jpg)