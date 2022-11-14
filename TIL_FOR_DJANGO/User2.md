# 홈페이지 설정
Allauth에서 urls를 제공하기 때문에, signup url로 들어가서 회원가입을 하면 콘솔에서 메일이 날라온다. (현재 콘솔로 메일 보내라고 설정해놨기때문에 ) 

![1](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20103436.png)

![2](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20103453.png)<br>
* 현재 allauth가 설정되어 있는 url에 따르면 로그인 후 profile페이지로 넘어가게 되는데 redirect 하는 경로 설정을 settings에서 바꿔 줄 수 있다.
![[Pasted image 20221002173422.png]]

[설정할 수 있는 항목들](https://django-allauth.readthedocs.io/en/latest/configuration.html)


# 현재 유저는 request.user로 접근할 수 있다.

View에서는 `request.user` Template에는 `{{user}}`로 접근할 수 있다.



현재 asdf로 로그인 된것을 볼수 있다. 현재 asdf는 유저 asdf의 name 필드 유저모델의 str 메소드는 유저네임을 리턴하기때문에 지금처럼 유저를 출력하면 유저가 나온다. 
request.user를 이용하면 현재 유저에대한 모든 필드를 접근할 수 있다. request.user.email을 쓰면 email을 출력 할 수 있다.
![3](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20103704.png)


![4](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20103833.png)
.is_authenticated 라고 하면 유저의 로그인 여부를 알 수 있다. 


![5](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20103854.png)
![6](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20104029.png)
settings에서 관련 세팅 추가하기
![7](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20104218.png)
[장고 allauth urls참고](https://github.com/pennersr/django-allauth/blob/master/allauth/account/urls.py)

# 이메일로 로그인하기

![8](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20110045.png)
회원가입시 email은 필수로하고 username은 필수로 안해도 되는 것으로 설정.
## 변경전
![9](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20110058.png)
## 변경후
![10](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20110106.png)

이렇게 세팅 몇가지만으로 설정을 바꿀수 있는게 allauth의 큰 장점이다.
모델에서 바꾸면
![11](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20110115.png)
템플릿의 유저 {{user}} 부분이 email로 나오게 된다
![12](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20110127.png)
![13](./User2/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20110134.png)
