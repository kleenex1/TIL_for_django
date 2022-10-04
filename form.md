# Form이 처리되는 과정
## 1
* 사용자가 폼을 작성하기 위해서 서버에 Form 양식을 요청한다.
* 처음 요청할때는 서버로부터 Form 양식을 조회하는 것이므로 GET 방식을 사용한다.
* Form이 있는 페이지를 처음 요청할때는 서버로부터 해당 페이지를 단순히 조회 하는 것이므로 GET방식을 사용한다.
* 그리고 서버가 처음 제공하는 Form을 언바운드폼(Unbound form)이라고 한다. 아직 데이터가 Form에 묶여져 있지 않은 상태.
## 2
* 사용자가 데이터를 입력하고 서버에 전송한다. Form method에 명시되어 있는 POST방식으로 action에 해당하는 url로 데이터를 전달한다. 데이터를 전달한다는 것은 form에 데이터와 함께 POST방식으로 서버에 요청하는 것이다.
## 3
* 서버에서 입력된 데이터와 폼을 합쳐 하나의 형태로 만든다. 이 과정을 바인딩이라고 하며 이렇게 데이터와 합쳐진 폼을 바인딩 폼이라고 한다.
## 4
* 바운드폼에서 가져온 데이터, 즉 입력된 데이터가 올바르지 않다면 유효하지 않은 잘못된 데이터이므로 사용자에게 다시 폼을 입력하도록 한다. 폼 데이터가 유효할때까지 계속 반복된다. 
## 5
* 입력된 데이터가 유효하다면 서버에서 지정한 로직을 수행한다. 입력된 데이터를 가공, 수정, 저장하는 등에 작업을 진행한다.
## 6
* 작업이 끝나면 새로운 페이지를 사용자에게 응답으로 돌려준다.

## HTML Form

### label & input
```html
<form>
    <label>이름</label>
    <input type="text">
</form>
```
![[Pasted image 20221004152338.png]]

### for & id
각각의 input태그와 label태그를 묶어주기 위해 label 태그에는 for속성, input태그에는 id가 사용된다. 
```html
<form>
    <label for="title">제목</label>
    <input type="text" id="title">
</form>
```
만약 for, id속성을 적어주고 싶지 않으면 label태그 안에 input 태그를 감싸면 된다.
```html
<form>
    <label>제목
        <input type="text">
    </label>
</form>
```

### name
name은 입력된 데이터를 서버로 보낼때, 서버에서 각각의 데이터를 구분하기 위한 속성으로 name 속성이 있는 양식 요소만 값이 서버로 전달된다.
```html
<form>
    <label for="title">제목</label>
    <input type="text" id="title" name="title">
</form>
```

### type
type에 따라 브라우저에서 값을 입력하는 형식인 위젯이 달라진다.
* email
```html
<label for="email">이메일</label>
<input type="email" id="email" name="email">
```
* password
```html
<label for="pwd">비밀번호</label>
<input type="password" id="pwd" name="pwd">
```
* button
```html
<input type="button" value="버튼입니다">
```
-   radio
```html
<input type="radio" id="male" name="gender" value="male">
<label for="male">남자</label><br>
<input type="radio" id="female" name="gender" value="female">
<label for="female">여자</label><br>
<input type="radio" id="other" name="gender" value="other">
<label for="other">기타</label>
```
-   checkbox
```html
<input type="checkbox" id="lang1" name="lang1" value="Python">
<label for="lang1">파이썬(Python)</label><br>
<input type="checkbox" id="lang2" name="lang2" value="JAVA">
<label for="lang2">자바(JAVA)</label><br>
<input type="checkbox" id="lang3" name="lang3" value="Go">
<label for="lang3">고(Go)</label><br>
```
-   date
```html
<label for="birthday">생년월일</label>
<input type="date" id="birthday" name="birthday">
```
-   file
```html
<label for="userfiles">파일선택</label>
<input type="file" id="userfiles" name="userfiles" multiple>
```
-   submit
```html
<input type="submit" value="전송하기"> 
```

## Django Form
* forms.py에서 model을 작성하는 것처럼 정의
```python
from django import forms
class PostForm(forms.Form):
	title = forms.CharField(max_length=50, label="제목")
	content = forms.CharField(label="내용", widget=forms.Textarea)
```
내가 원하는 데이터에 따라 form 필드를 작성, 이렇게 작성한 form을 views.py에서 template에 넘겨주고 template에서 사용한다.
* Views.py
```python
def post_create(request):
	post_form = PostForm()
	return render(request, "posts/post_form.html", {"form": post_form})
```
* template
```html
<form>
	{{form.as_ul}}
	<input type="submit" value="전송">
</form>
```

form 처리를 할때는 \{% csrf_token %} 교차 사이트 위조 검증, 탬플릿 태그를 활용한다. 내가 하지 않은 요청을 내가 한것처럼 위조하는 것을 방지하기 위한 보안기술

* Views.py
```python
def post_create(request):
	if request.method == "POST":
		title = request.POST["title"]
		content = request.POST["content"]
		new_post = Post(title=title, content=content)
		new_post.save()
		return redirect("post-detail", post_id=new_post.id)
	else:
		post_form = PostForm()
		return render(request, "posts/post_form.html", {"form": post_form})
```
if request.method == POST라면, 전송을 눌렸을때 title, content라고 변수명을 지은 곳에 request.POST로 받은 값을 넘겨주고, form 클래스를 가져와서 new_post라는 변수명에 title & content를 넣고 new_post.ave()한다. redirect를 통해 url과 넘겨줄 인자를 돌려준다.



[https://docs.djangoproject.com/en/3.2/ref/forms/fields/#built-in-field-classes](https://docs.djangoproject.com/en/3.2/ref/forms/fields/#built-in-field-classes)
[https://docs.djangoproject.com/en/3.2/ref/forms/widgets/](https://docs.djangoproject.com/en/3.2/ref/forms/widgets/)


## Model Form

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = '__all__'
		fields = ['title', 'content']
```

```python
def post_create(request):
	if request.method == "POST":
		post_form = PostForm(request.POST)
		new_post = post_form.save()
		return redirect("post-detail", post_id=new_post.id)
	else:
		post_form = PostForm()
		return render(request, "posts/post_form.html", {"form": post_form})
```

