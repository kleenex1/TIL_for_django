# 템플릿 파일 관리
![0](./sandwitches.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20181746.jpg)
* 샌드위치 구조를 해야 django가 url을 찾을때 같은 이름의 html일지라도 경로를 잘 찾아 갈 수 있다.

## 샌드위치 구조를 하는 이유
![1](./sandwitches.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20180905.jpg)

* 각각의 앱에 템플릿츠 디렉토리가 있으니까 템플릿을 찾을때 거기서 찾으라고 설정해준 것.

![2](./sandwitches.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20181017.jpg)
![3](./sandwitches.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20181156.jpg)
A,B 등록된 순서대로 찾게 된다. index.html을 찾아라고 했을때 
![4](./sandwitches.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20181212.jpg)
![5](./sandwitches.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20181310.jpg)
![6](./sandwitches.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20181346.jpg)

* 그러므로 샌드위치 구조를 통해서 해당하는 index.html의 App이름을 폴더로 추가 해주면 이름이 중복될 일이 없다.

* 정적파일도 샌드위치 구조를 쓰는데 이유가 한가지 더 있다.
* 개발 사이트를 배포할 때 정적파일을 하나의 디렉토리로 묶어서 사용하게 된다. 그래서 같은 파일의 이름이 있으면 충돌이 생긴다. 그래서 App별로 묶어준다.

# 정적파일 관리

![static](./sandwitches.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-24%20182148.jpg)

* html 최상단에 static 파일을 쓰겠다고 선언한다.
```python
{% load static %}
```

* 경로가 들아갈 곳에 `{% static '경로'%}` 입력
```python
경로 = {% static 'css/image/fonts등의 경로' %}
```
