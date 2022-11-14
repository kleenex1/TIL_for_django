# 메시지 & 이메일 오버라이딩 
![1](./message_emailoverriding/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20150532.png)

* email을 오버라이딩 하여 내용을 수정할 수 있다. 

![2](./message_emailoverriding/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20150721.png)
* 장고 allauth를 사용하면 로그인이나 어떤 기능들을 할 때마다 메시지가 쌓이게 되는데 admin사이트를 들어갈 때 한번에 출력되게 된다.
* 그러므로 모든 메시지들을 빈 파일로 오버라이딩 한다.

![3](./message_emailoverriding/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20150925.png)
* 빈문자열로 하는 이유는, 어카운트 이메일에 앞에 붙는 문자열을 빈문자열로 만들어주는 세팅
* allauth가 발송하는 이메일은 커스터마이징으로 오버라이딩을 해도 항상 웹사이트에 도메인이 붙게 된다. 그러므로 제거해주는 세팅.

# 정리

allauth의 템플릿 파일을 오버라이드하려면 allauth의 템플릿 파일과 똑같은 이름을 가진 파일을 app_name/templates/account/ 폴더 안에 넣어주시면 됩니다. 그리고 settings.py 파일의 `INSTALLED_APPS` 목록에서 `app_name`은 `allauth`보다 위에 와야 합니다.

# HTML 템플릿

커스텀 템플릿을 app_name/templates/account/ 폴더 안에 넣어주시면 됩니다.

(예: coplate/templates/account/signup.html)

![4](./message_emailoverriding/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20151331.png)

예: signup.html
![5](./message_emailoverriding/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20151444.png)

# 이메일 템플릿

커스텀 템플릿을 app_name/templates/account/email/ 폴더 안에 넣어주시면 됩니다.

(예: coplate/templates/account/email/email_confirmation_signup_subject.txt)
![6](./message_emailoverriding/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20151503.png)

필요할 경우 위 테이블에 있는 템플릿 변수를 활용해서 이메일 내용을 작성하시면 됩니다.

예: password_reset_key_message.txt

```
안녕하세요 {{ user }} 회원님,

아래 링크를 통해 계정의 비밀번호를 재설정하실 수 있습니다.

{{ password_reset_url }}

감사합니다.

Plates
```

그리고 이메일 제목은 템플릿을 오버라이딩해도 제목 앞에 웹사이트 도메인이 붙는데, 이걸 제거하려면 `ACCOUNT_EMAIL_SUBJECT_PREFIX`를 설정해 주시면 됩니다.

```python
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
```

`ACCOUNT_EMAIL_SUBJECT_PREFIX`의 디폴트 값은 웹사이트 도메인 이름입니다.
# 메시지 템플릿
메시지를 사용하지 않기 때문에 빈 메시지 템플릿을 사용했습니다

![7](./message_emailoverriding/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20151654.png)<br>
메시지 템플릿은 app_name/templates/account/messages/ 폴더 안에 넣어주시면 됩니다.

만약 메시지 내용을 실제로 오버라이드하고, 웹사이트 내에서 사용하고 싶으시다면 메시지를 디스플레이해 줘야 하는데요. 메시지를 디스플레이하는 방법은 [여기](https://docs.djangoproject.com/en/2.2/ref/contrib/messages/#displaying-messages)서 확인하실 수 있습니다.