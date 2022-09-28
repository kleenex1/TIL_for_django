![스샷](../../screenshot/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-28%20200655.png)

# 할일 메모 앱


# 해당 장고 프로젝트를 하기 위해
1.  template은 하나의 html 페이지로 해결하였다. (글 상세 작성 창이 필요 없는 간단한 메모 앱) 
2. Table/button/input 들은 부트스트랩을 이용하였다. (CRUD 연습 초점)

# URL 구조를 먼저 만들었다.
```python
urlpatterns = [

    path("", views.index),
    path("create/", views.todo_create),
    path("delete/<int:todo_id>", views.todo_delete),
    path("edit/<int:todo_id>", views.todo_update),

]
```
* 프로젝트 urls 에서 각 App으로 include를 이용하여 url 배분을 하였다.
* 해당 App(Todos)에서 urls.py 파일에 새로 url들을 분류해주었다.
* index 페이지에서는 DB에서 계속 목록을 불러올 것이며
* create/ 에서는 DB 생성 후 redirect를 통해 index화면으로 돌아가게 하며
* delete/<int:todo_id> 에서는 todo_id 인자를 받아 삭제 후 redirect를 통해 index화면으로 돌아가게 하며
* edit/<int:todo_id> 에서는 todo_id 인자를 받아 템플릿 언어를 통해 글자에 부트스트랩 \<del>을 통해 할일을 끝냈는지 유무를 표시한다.

# 모델을 만들었다.
```python
class Todo(models.Model):

    content = models.CharField(max_length=80)
    priority = models.IntegerField(default=3)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
```

* 메모를 위해 들어갈 내용은 length 80 길이 제한을 위해 CharField를 이용
* 우선순위는 Integer가 들어가며 기본값 설정
* completed는 할일의 완성을 체크 하기 위해 Boolean형으로 설정
* created_at 은 datefield로 auto_now_add를 통해 처음 생성될 때 시간을 자동적으로 저장 추후 변경 없음.
* deadline 은 null값을 허용하도록 하였다.

# 처음 DB에 값을 몇개 임의로 넣어주었다.
```shell
python manage.py shell
from todos.models import Todo
Todo.obejcts.create(content='책읽기', priority=5)
```
* index 화면에서 바로 출력 될 수 있도록 view함수를 먼저 정의한다.

# View 함수 정의
```python
from django.shortcuts import render, redirect
from .models import Todo
 
# Create your views here.
  
def index(request):
    todos = Todo.objects.all().order_by("priority")
    context = {"todos": todos}
    return render(request, "todos/index.html", context)
```
* index 화면에서 우선순위에 따라 화면에 보여주기 위해 view에서 먼저 데이터를 priority 오름차순 정렬해두었다.

# Template 정의

<details>
<summary>접기/펼치기</summary>

```html
{% load static %}

<!DOCTYPE html>

<html lang="en">


<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static 'todos/css/styles.css' %}">
  <title>오늘의 할일</title>

  <!--부트스트랩 먹일곳-->
  {% block css %}
  {% endblock css %}
</head>
  
<body>
  <h1>기록을 해보자 ~</h1>

  <!--할일/우선순위/마감기한 입력할곳-->
  <div class="create_content">
    {% block create_content %}
    {% endblock create_content %}
  </div>
 
  <!--본문 내용 할일 리스트 나올곳-->
  <div class="content">
    {% block content %}
    {% endblock content %}
  </div>
</body>
</html>
```

</details>
* 기본적으로 틀을 만들어놓을 base.html을 생성하여 css / content가 들어갈 내용들을 장고 템플릿언어를 사용하여 미리 짜놓는다. 

<details>
<summary>접기/펼치기</summary>

```html
{% extends './base.html' %}
  
<!--나중에 따로 부트스트랩 적용할 것-->
{% block css %}
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
  integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
  integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
{% endblock css %}

{% block create_content %}
<div>
  <form action="create/">
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">할 일</span>
      <input type="text" name="content" class="form-control">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">우선 순위</span>
      <select name="priority" class="form-select">
        <optgroup label="우선순위">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
        </optgroup>
      </select>
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">마감 기한</span>
      <input type="date" name="deadline" class="form-control">
    </div>
    <div class="d-grid gap-2">
      <button type="submit" class="btn btn-outline-primary">할 일 추가</button>
    </div>
  </form>

  
</div>
{% endblock create_content %}
{% block content %}

<div>
  <table class="table my-5">
    <thead>
      <tr>
        <th scope="col">우선 순위</th>
        <th scope="col">할 일</th>
        <th scope="col">생성 날짜</th>
        <th scope="col">마감 기한</th>
        <th scope="col">진행 상태</th>
        <th scope="col">상태 변경</th>
        <th scope="col">삭제</th>
      </tr>
    </thead>
    <tbody>
      {% for todo in todos %}
      {% if todo.completed %}
      <tr>
        <td><del>{{todo.priority}}</del></td>
        <td><del>{{todo.content}}</del></td>
        <td><del>{{todo.created_at}}</del></td>
        <td><del>{{todo.deadline}}</del></td>
        <td><del>{{todo.completed}}</del></td>
        <td><a href="edit/{{todo.id}}"><button type="button" class="btn btn-primary">변경</button></a></td>
        <td><a href="delete/{{todo.id}}"><button type="button" class="btn btn-danger">삭제</button></a></td>
      </tr>
      {% else %}
      <tr>
        <td>{{todo.priority}}</td>
        <td>{{todo.content}}</td>
        <td>{{todo.created_at}}</td>
        <td>{{todo.deadline}}</td>
        <td>{{todo.completed}}</td>
        <td><a href="edit/{{todo.id}}"><button type="button" class="btn btn-primary">변경</button></a></td>
        <td><a href="delete/{{todo.id}}"><button type="button" class="btn btn-danger">삭제</button></a></td>
      </tr>
      {% endif %}
      {% endfor %}
  </table>
</div>
{% endblock content %}
```

</details>
* index 페이지에서 해당 내용만 채운다.

# 할일 목록 만들기
```python
def todo_create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect("/todos")
```
* 서버에 민감한 데이터가 URL에 노출되면 안되지만 간단한 실습용으로 GET을 이용하였다. 
> 이런 문제를 방지하기 위해서는 form에서 **POST 방식**으로 데이터를 보내어 `todo_create`함수에서는 POST일 때만이라는 조건으로 데이터를 처리해야한다. 
> 또한 form 처리를 할때는 장고에서 제공하는 `{%  csrf_token %}` 보안기술을 사용하여아 하는데, 이는 좀 더 기능을 이해하고 활용할 예정이다.

* 크로스 사이트 요청 위조라는 것은 유저가 보안이 취약한 사이트에서 로그인 후, 로그아웃을 하지 않은채 악성 사이트로 이동하게되면 (보통 우리 로그인상태에서 다른 사이트를 많이 들어갈때 처럼) 악성 사이트에서 유저의 정보를 탈취 할 수 있도록 요청을 시도하는데 요청을 보낼 때 유저의 정보도 함께 서버로 전송하게 된다.
* 장고의 CSRF 방지 기능을 기본으로 제공하는데 form 태그 옆에 사용하면 된다.
```html
<form action="/user" method="post">{% csrf_token %}
    ...
</form>
```
# 삭제하기, 업데이트하기
```python
def todo_delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect("/todos")

    
def todo_update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo.completed:
        todo.completed = False
        todo.save()
    else:
        todo.completed = True
        todo.save()
    return redirect("/todos")
```

* 삭제하기는 받아온 id를 그대로 delete를 해주었으며
* 업데이트는 해당 템플릿에서 a태그를 통해 인자가 넘어오면 해당되는 레코드를 False, True로만 바꾸는 로직을 적용하였다.


# 보충할 점
* redirect에서 하드코딩한 부분
* template 내에 경로 하드코딩한 부분
* FORM method 방식 변경
* 만들기 전에 큰 설계를 그릴것