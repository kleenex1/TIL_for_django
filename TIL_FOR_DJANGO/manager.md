# 매니저와 역관계

# Reverse Relationship

```python
<Model>.objects.all()
<Model>.objects.get()
<Model>.objects.filter()
<Model>.objects.count()
```
* Manager (objects)
	* 장고 모델과 데이터베이스를 연결해 주는 인터페이스
	* 매니저를 통해 모델에 대한 ORM 연산을 수행할 수 있다
	* 베이스(Base) 또는 기본 쿼리셋이 숨어있다

### objects

```python
QuerySet <[
	obj1,
	obj2,
	obj3,
]>
```

1. '숨겨진 쿼리셋'을 일반 쿼리셋처럼 사용할 수 없음
```python
for review in Review.objects : # 오류
for review in Review.objects.all() : # 실행
```
2. 매니저에 CRUD 연산을 하면 '숨겨진 쿼리셋'이 사용됨
```python
<Model>.objects.order_by : # .all()없이도 실행됨
```

### 역관계
* Review와  Comment의 관계를 만들면서 ForeignKey를 만들어주면 장고에서는 역관계도 생성해준다. 
![1](./manager/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-11%20161934.png)

### OneToOneField
![2](./manager/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-11%20162007.png)

### ManyToManyField
![3](./manager/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-11-11%20162017.png)
* Django에서는 역관계의 이름을 원하는 이름으로 바꿀 수 있다.
* `related_name=followers`로 역관계의 이름을 정할 수 있다. 

### 예시
```python

class Comment(models.Model):
...
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments') # user.comments로 접근가능!
	review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments') # review.comments로 접근가능!
```

### 역관계가 필요 없을 경우
```python
... , related_name='+') # +로 설정한다.
```

### Generic FK 역관계
```python
class Like(models.Model):
...
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	liked_object = GenericForeignKey() 

	def __str__(self):
	return f"({self.user}, {self.liked_object})

# review.like_set이나 comment.like_set과 같이 접근할 수 없다.
```

### 역관계를 추가하고 싶은 모델에 GenericRelation 을 추가한다.
```python
from django.contrib.contenttypes.fields import GenericRelation

class Comment(models.Model):
...
	likes = GenericRelation('Like')
class Review(models.Model):
...
	likes = GenericRelation('Like')

# 이제 review.likes, comment.likes로 접근 할 수 있다. 
# review.likes, comment.likes도 매니저다.
# GenericRelation 필드를 추가함으로써 CASCADE효과도 생긴다.
```
