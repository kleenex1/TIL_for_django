## 페이지네이션 구현하기

![1](./pagination/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-09%20134608.png)

![2](./pagination/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-09%20140807.png)

## Django의 페이지네이션

Django는 페이지네이션을 쉽게 구현할 수 있도록 하는 Paginator를 제공합니다. Paginator는 총 두 개의 파라미터만 넘겨주면 쉽게 정의할 수 있는데 첫 번째 파라미터는 각각의 페이지로 나뉘게 될 데이터의 목록, 두 번째 파라미터는 한 페이지에 보여줄 데이터의 수입니다.

```python
from django.core.paginator import Paginator # Django의 Paginator
from .models import Post # 작성한 모델 클래스

posts = Post.object.all() # 모든 데이터를 가져와서
paginator = Paginator(posts, 6) 
# 첫 번째 파라미터 : 페이지로 나뉘게 될 데이터의 목록
# 두 번째 파라미터 :  한 페이지에 보여줄 데이터의 수
```

이렇게 만들어진 Paginator는 자동으로 데이터를 개수에 따라 페이지를 나누어서 갖고 있고 우리는 페이지의 번호를 이용해서 Paginator로부터 페이지를 가져와서 제공하는 여러 기능을 사용하면 됩니다. Paginator와 각각의 Page가 가지고 있는 기능 중 자주 사용하는 것은 아래와 같습니다.

![3](./pagination/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-09%20140848.png)


### View 작성하기

Django 페이지네이션은 Paginator를 이용해서 구현합니다.

```python
from django.core.paginator import Paginator
```

먼저 페이지네이션을 구현하려면 데이터를 가져와야겠죠? 모델(Model)을 이용해서 가져오면 됩니다.

```python
def post_list(request):
    posts = Post.object.all() # 모든 Post 데이터를 가져옵니다.
```

그 다음은 Django의 Paginator에 페이지네이션을 구현할 데이터 목록과 각 페이지마다 보여줄 데이터의 개수를 전달합니다.

```python
def post_list(request):
    posts = Post.object.all() 
    paginator = Paginator(posts, 8) # Post를 한 페이지에 8개씩 할당합니다.
```

이제 Template으로 넘겨주기 위한 페이지를 Paginator로 부터 가져와야 합니다. 이때 가져올 페이지의 번호는 URL의 쿼리스트링에 있는 데이터를 이용하겠습니다.

```python
def post_list(request):
    posts = Post.object.all() 
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page') # 쿼리 스트링으로 부터 페이지 번호 조회
```

그 후 .page(num) 메소드를 이용해서 페이지를 가져온 후 Template으로 넘겨줍니다.

```python
def post_list(request):
    posts = Post.object.all() 
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.page(page_number) # 페이지 번호에 해당하는 페이지를 가져옴
    return render(request, 'post_list.html', {'page_obj': page_obj})
```

### Template 작성하기

Template에서는 View에서 넘어온 Page를 이용해서 화면을 구성하면 됩니다. 먼저 페이지의 모든 데이터를 표시할 때는 아래와 같이 for 템플릿 태그를 이용해서 작성할 수 있습니다.

```html
...

{% for post in page_obj.object_list %}
    <p>post로 부터 조회한 데이터</p>
    <p>{{ post.title }}</p>
{% endfor %}

...
```

그리고 이전 페이지, 다음 페이지로 가는 오브젝트들도 Page가 제공하는 메소드를 이용하면 쉽게 구현할 수 있습니다.

```html
...

{% if page_obj.has_previous %} <!-- 만약 현재 페이지의 이전 페이지가 있다면 -->
    <a href="?page=1"> first</a>
    <a href="?page={{ page_obj.previous_page_number }}">prev</a> <!-- 이전 페이지 번호 -->
{% endif %}

<span>
    Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
    <!-- page_obj.number : 페이지(page_obj)의 번호 -->
    <!-- page_obj.paginator.num_pages : 페이지를 관리하는 Paginator가 가지고 있는 전체 페이지 수 -->
</span>

{% if page_obj.has_next %} <!-- 만약 현재 페이지의 다음 페이지가 있다면 -->
    <a href="?page={{ page_obj.next_page_number }}">next</a> <!-- 다음 페이지 번호 -->
    <a href="?page={{ page_obj.paginator.num_pages }}">last </a> <!-- 전체 페이지의 개수 = 마지막 페이지 번호 -->
{% endif %}

...
```

 Django의 Pagination 공식문서 [https://docs.djangoproject.com/en/3.2/topics/pagination/](https://docs.djangoproject.com/en/3.2/topics/pagination/)