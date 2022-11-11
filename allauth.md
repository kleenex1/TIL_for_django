# Allauth 

[django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html)는 유저 기능을 만들기 위한 패키지입니다.

allauth는 Django 프레임워크에 포함되지 않기 때문에 따로 설치를 해줘야 합니다. (설치 [가이드](https://django-allauth.readthedocs.io/en/latest/installation.html), 설치 [User.md](./User.md)[User2.md](./User2.md)))

allauth 패키지 안에는 유저 기능 구현에 필요한 URL 패턴, 뷰, 폼, 템플릿 등이 있고, 유저 모델은 django.contrib.auth의 유저 모델을 사용하는데요. allauth를 설치하면 안에 있는 코드를 가지고 기본적인 유저 시스템을 만들어 줍니다. 우리는 이 유저 시스템을 우리의 니즈에 맞게 바꿔주면 되는데요, 여러 부분들을 바꿔줄 수 있습니다.

# allauth URL: URL 패턴 정의

allauth의 URL은 [여기](./allauthsetting.md) 정리돼 있는데요, 처음에 allauth URL을 프로젝트에 추가할 때, 앞에 붙는 패턴을 정해줄 수 있습니다.

project/urls.py

```python
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```

이렇게 정의해 주면 모든 url 앞에 accounts/가 붙고 (예: localhost:8000/accounts/login/),

project/urls.py

```python
urlpatterns = [
    ...
    path('', include('allauth.urls')),
    ...
]
```

이렇게 정의해 주면 모든 url 앞에 아무것도 안 붙습니다 (예: localhost:8000/login/).

# allauth 주요 로직: 세팅(Configuration)

allauth의 주요 로직은 세팅(configuration)을 통해 바꿀 수 있습니다. [여기](./allauthsetting.md)서 자주 사용되는 세팅을 찾으실 수 있습니다. 리디렉션 URL, 폼에서 사용되는 필드, 링크를 클릭했을 때의 동작 등 여러 가지를 바꿀 수 있는데요. settings.py에 간단한 코드를 써주는 거만으로도 로직을 원하는 대로 바꿀 수 있다는 게 allauth의 큰 장점입니다.

# allauth 폼: 커스텀 폼

기본 유저 인증 관련 페이지들에서는 다양한 폼이 사용됩니다. 로그인 폼, 회원가입 폼, 비밀번호 변경 폼 등 다양한 폼이 있죠? 회원가입을 제외한 나머지 페이지는 거의 항상 똑같은 필드를 가지고 있기 때문에 폼을 바꿔줄 필요가 없습니다. 예를 들어 로그인은 항상 로그인 필드와 비밀번호 필드가 있고, 비밀번호 변경은 현재 비밀번호, 새 비밀번호, 새 비밀번호 확인 필드가 있죠? 하지만 회원가입은 서비스에 따라 필요한 정보가 다 다르기 때문에 폼을 커스터마이즈해야 하는 경우가 많습니다. 유저네임 필드 여부, 비밀번호 필드 여부 같은 흔한 설정은 configuration을 통해 할 수 있지만, 커스텀 정보를 입력받으려면 커스텀 폼을 사용해야 합니다.

forms.py 파일에 추가 필드에 대한 폼을 만들고, `signup(self, request, user)` 메소드를 정의해 주면 됩니다.

app/forms.py

```python
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['extra_field1', 'extra_field2', ...]

        def signup(self, request, user):
        user.extra_field1 = self.cleaned_data['extra_field1']
        user.extra_field2 = self.cleaned_data['extra_field2']
        ...
        user.save()
```

(참고로 `ModelForm` 대신 일반 `Form`을 써도 됩니다.)

그리고 `ACCOUNT_SIGNUP_FORM_CLASS`를 설정해 주면 됩니다.

project/settings.py

```python
ACCOUNT_SIGNUP_FORM_CLASS = 'app.forms.SignupForm' 
```

# 디자인: 템플릿 오버라이딩

아마 allauth가 제공하는 기본 템플릿을 그대로 사용하고 싶지는 않으실 겁니다. 템플릿을 오버라이딩 하려면 allauth가 제공하는 템플릿과 똑같은 이름을 가진 파일을 account 폴더 안에 넣어주면 되는데요. 자세한 내용은 [링크](./message_emailoverriding/)를 참고하세요.

# 뷰 오버라이딩?

뷰는 어떤 웹 페이지의 주요 로직을 담당하는 부분입니다. allauth에서 기본적으로 제공하는 뷰를 오버라이딩하면, 로직을 원하는 대로 바꿔줄 수 있지만, 그 과정은 굉장히 복잡하고 대부분의 로직은 configuration을 통해 바꿀 수 있기 때문에 뷰는 잘 오버라이딩 하지 않습니다. 유일한 예외는 비밀번호 변경 로직을 다루는 `PasswordChangeView`인데, 비밀번호 변경 후 리디렉트되는 URL을 configuration으로 설정할 수 없기 때문에 뷰를 오버라이딩해 줬습니다.

app/views.py

```python
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
```

위 코드는 리디렉트 URL을 `'index'`, 즉 홈페이지로 설정합니다. 그리고 오버라이딩한 뷰를 사용하기 위해서 URL 패턴을 바꿔주면 된다.

project/urls.py

```python
urlpatterns = [
    ...
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_password_change'),
    path('', include('allauth.urls')),
]
```
