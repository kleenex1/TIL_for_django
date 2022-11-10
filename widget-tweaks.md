# Widget-Tweaks 활용하여 form 꾸미기

![1](./widget-tweaks/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-10%20145525.png)<br>

> pip install django_widget_tweaks 설치
> {% load widget_tweaks %}
> settings → widget_tweaks 추가


attr: 속성은 기존의 속성을 바꿔주는것
add_class : 속성을 추가



input 태그에는 여러 속성이 사용됩니다. 예를 들어 제공되는 singnup.html 템플릿에는 아래와 같은 input 태그가 있었다.

```html
<input type="email" name="email" placeholder="이메일" autocomplete="email" class="cp-input" required id="id_email">

<input type="text" name="nickname" maxlength="15" placeholder="닉네임 (Coplate에서 사용되는 이름입니다)" class="error cp-input" required id="id_nickname">

<input type="password" name="password1" placeholder="비밀번호" autocomplete="new-password" class="cp-input" required id="id_password1">
     
<input type="password" name="password2" placeholder="비밀번호 확인" class="cp-input" required id="id_password2">
```


### `type`

필드에 들어가는 데이터 유형을 뜻합니다. 모델 폼을 사용하면 모델 필드의 종류에 따라 `type` 이 설정됩니다. (예: `CharField` - `type="text"`, `URLField` - `"type=url"`, `IntegerField` - `type="number"`, `ImageField` - `type="file"`)

`type`에 따라 사용되는 HTML 폼 필드가 결정되고 입력되는 데이터에 대한 유효성 검사도 진행됩니다. 예를 들어 `"type=url"`인 경우 일반 텍스트 필드가 사용되는데, 여기에 유효한 URL을 넣지 않으면 폼을 submit(서버에 전달) 할 수 없습니다. 참고로 이런 유효성 검사는 서버 측에서 진행되는 유효성 검사와 다릅니다. 유효하지 않은 데이터는 아예 서버 쪽으로 전달되는 것을 막기 위해서 클라이언트, 즉 웹 브라우저 측에서도 어느 정도의 유효성 검사를 해 줍니다. 하지만 클라이언트 측에서 진행할 수 없는 유효성 검사도 있는데요. 예를 들어 어떤 값의 중복 여부를 확인하려면 데이터베이스에 있는 값들과 비교를 해야 하기 때문에 클라이언트 측에서 확인할 수 없습니다.

### `name`

폼 데이터가 서버로 전송될 때 사용되는 이름인데, django 폼을 사용하면 자동으로 설정됨.

### `placeholder`

HTML 폼 필드 안에 디스플레이되는 텍스트입니다. Django 폼을 사용하면 기본적으로 django 필드의 이름이 사용됩니다. (그래서 우리는 widget-tweaks 패키지를 사용해서 placeholder 속성을 바꿔주었음)

### `maxlength`

입력받는 값의 최대 길이를 제한합니다. 이것도 클라이언트 측에서 진행되는 유효성 검사의 일부라고 볼 수 있는데요. 모델 폼을 사용하면 `CharField`의 `max_length` 값에 따라 자동으로 설정됩니다.

### `autocomplete`

브라우저는 기본적으로 input 태그에 입력되는 값들을 기억합니다. autocomplete(자동완성) 기능은 HTML 폼 필드에 값을 입력할 때, 과거에 비슷한 필드에 입력했던 값을 제안해 주는 기능입니다. autocomplete 속성은 form 태그에도 있고, input 태그에도 있는데 autocomplete 속성의 디폴트 값은 "on"이고 input 태그의 autocomplete 속성이 더 우선순위가 높습니다. 그러니까 form 태그와 안에 있는 input 태그에 둘 다 autocomplete 속성이 정의돼 있으면 input 태그의 autocomplete 속성이 사용되는 거죠. (form 태그에는 autocomplete 속성이 있고 input 태그에는 없는 경우 form 태그의 autocomplete 속성이 사용됩니다.)

form 태그의 autocomplete 속성에는 "on"(자동완성 기능을 사용함), "off"(자동완성 기능을 사용하지 않음) 두 가지 옵션이 있고, input 태그의 autocomplete 속성에는 "on", "off" 외에도 많은 옵션이 있습니다. 예를 들어 위 코드를 보시면 `autocomplete="email"`, `autocomplete="new-password"`같이 다양한 값이 사용되는 걸 확인하실 수 있을 텐데요. 다양한 속성을 통해 브라우저한테 어떤 정보에 대한 자동완성을 원하는지 전달해 줄 수 있습니다. 예를 들어 `autocomplete="email"`을 사용하면 이메일 주소만 제안해 줍니다. 여러 autocomplete 옵션에 대한 설명은 이 [링크](https://developer.mozilla.org/ko/docs/Web/HTML/Attributes/autocomplete)를 참고.



### `class`

디자인 (CSS)를 위한 속성입니다. Django가 만들어 주는 input 태그에는 class 속성이 포함되지 않습니다.

### `required`

HTML 폼 필드를 비워놓을 수 없게 하는 속성입니다. 이것도 클라이언트 측에서 진행되는 유효성 검사의 일부라고 볼 수 있는데요. Django 모델/폼 필드를 필수로 정의해 주면 required 속성이 저절로 추가됩니다.

### `id`

일반적으로 id는 HTML 요소를 (CSS나 JavaScript로) 선택할 수 있게 해 줍니다. id 속성도 django 폼을 사용하면 자동으로 설정된다.

Django 폼을 렌더하는 작업은 항상 까다롭고 헷갈릴 수 있는데요. 먼저 `{{ form.field }}` 형태로 폼 필드를 렌더한 다음, 개발자 도구로 어떤 속성이 설정되는지를 파악하고 widget-tweaks를 사용해서 속성을 추가하거나 수정하면 된다.