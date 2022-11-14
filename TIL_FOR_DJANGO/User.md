## django.contrib.auth
- 기본 유저 모델 제공
- 상속받아서 쓸 수 있는 유저 모델 제공

유저 모델을 선택하는데는 3가지 선택지가 있다.
- 기본 유저 모델 : User
- 상속받아서 쓸 수 있는 유저 모델 : AbstractUser(필드가 다 정해져있음)
- 상속받아서 쓸 수 있는 유저 모델 : AbstractBaseUser(필드를 다 정의해줘야함 커스텀필요)<br>

1. 유저 모델을 정의할 때는 `User`, `AbstractUser`, `AbstractBaseUser` 세 가지 옵션이 있다.
2.`AbstractUser`에는 username, email, password 같은 기본 필드들이 다 있고, 추가로 필요한 필드만 추가해 주면 된다.
3. `AbstractBaseUser`는 유저를 만들기 위한 틀만 제공하기 때문에 모든 필드를 직접 정의해 줘야 한다.<br>

![1](./User/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20092353.png)

(유저 모델 정의하고 settings에서 AUTH_USER_MODEL하고 난 뒤에 마이그레이션 해줘야 안꼬인다.)


## 유저모델 어드민 페이지에 등록하기 

![2](./User/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20092612.png)

## Allauth 셋업
pip install django-allauth
settings.py에 django와 allauth 백엔드를 같이 포함시켜줘야 한다.
![3](./User/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20093253.png)

![4](./User/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20093419.png)

django.contrib.sites 는 어떤 기능을 여러 웹사이트에서 사용할 수 있게 해준다. 비슷한 컨텐츠나 기능을 갖고 있는 웹사이트가 여러개 필요할때는 django.contrib.sties를 사용해서 프로젝트 하나로 여러 웹사이트를 운영할 수 있다. 그래서 여기 있는 SITE_ID가 각각의 사이트의 ID라고 생각하면 된다. 웹사이트를 하나 만들거니까 SITE_ID 를 1로 설정하면 된다.

그 후 urls에 가서 
![5](./User/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20100834.png)

그다음 settings로 가서

![6](./User/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20100845.png) <br>
allauth가 제공하는 이메일 인증기능 같은것들을 활용하려면 이메일을 보내야 하는데 이메일을 어떻게 보낼지를 설정하는 기능 (지금은 콘솔로 보내는걸로 설정해놓음)

이 설정 이후 python manage.py migrate 해야 된다!!

1. django-allauth는 django 프레임워크에 포함되지 않기 때문에 따로 설치를 해줘야 한다.
2. django-allauth는 유저 기능 구현에 필요한 URL 패턴, 뷰, 폼 등을 제공하지만 유저 모델은 제공하지 않는다.
3. django-allauth는 이메일 인증, 소셜 로그인 등 django.contrib.auth에 포함되지 않는 기능을 제공한다.