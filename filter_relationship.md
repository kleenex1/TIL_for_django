```python
Review.objects.filter(author=some_user) # Review모델에 author라는 FK가 있다면,
Review.objects.filter(author__id=1)
Review.objects.filter(author__nickname="django")

# 더블 언더바(__)를 사용하면 관계와 필드를 계속 타고 들어갈 수 있다.
Review.objects.filter(author__email__endswith='aaa.com')

# 이메일이 aaa.com으로 끝나는 유저가 작성한 리뷰들에 달려 있는 코멘트들
# == 코멘트가 있는 리뷰의 작성자의 이메일이 aaa.com으로 끝남
Comment.objects.filter(review__author__email__endswith='aaa.com')

```
 > 다양한 방법이 있을 때는 현재 상황에서 어떤 것이 이미 주어져 있는지
 > 생각해보고 구현하기 쉬운 방법을 선택하도록 한다.
https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups


# 예시 views.py
```python
class ProfileView(DetailVeiw):
	model = User
	template_name = 'coplate/profile.html'
	pk_url_kwarg = 'user_id'
	context_object_name = 'profile_user'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user_reviews'] = Review.objects.filter(author__id=self.kwargs.get('user_id'))[:4]
		return context
```
* 만약 id가 아닌 실제 유저를 사용했다면?
	먼저 id에 해당하는 유저를 가져온다음 그 유저를 필터에 사용해야 했을 것.
	아래 코드가 더 복잡해졌다.
```python
... context = super().get_context_data(**kwargs)
-->추가 profile_user = User.objects.get(id=kwargs.get('user_id'))
	context['user_reviews'] = Review.objects.filter(authorr=profile_user)[:4]
	...
```

# fk는 하나의 오브젝트만 가리켰다.
```python
Review.objects.filter(author__id=1) # 작성자의 아이디가 1인 리뷰들
```

# ManyToManyField인 경우
```python
# following에 있는 유저들 중 id가 1인 유저가 하나라도 있다.
# 즉, id 1을 가진 유저를 팔로우하는 유저들을 필터한다.
User.objects.filter(following__id=1)

# 맥도날드에 리뷰를 하나라도 남긴 유저 필터
User.objects.filter(reviews__restaurant_name='맥도날드')
```

# Generic ForiegnKey로는 필터를 할 수 없다.
```python
class Comment(models.Model):
...
	likes = GenericRelation('Like')

class Review(models.Model):
...
	likes = GenericRelation('Like')

class Like(models.Model):
	dt_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	liked_object = GenericForeignKey()
```

```python
# liked_object가 어떤 종류의 오브젝트인지 알 수 없다
Like.objects.filter(liked_object__id=1)
Like.objects.filter(liked_obejct=review) 
```

# related_query_name 추가하기
```python
class Comment(models.Model):
...
	likes = GenericRelation('Like', related_query_name='comment')

class Review(models.Model):
...
	likes = GenericRelation('Like', related_query_name='review')

class Like(models.Model):
	dt_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	liked_object = GenericForeignKey()
```

```python
# related_query_name 추가 후 접근 가능
Like.objects.filter(review=review)
Like.objects.filter(review__id=1)
Like.objects.filter(comment=comment)
Like.objects.filter(comment__id=1)

# 하지만 like.review나 like.comment처럼은 접근불가 NO!
# like.liked_object로 접근은 가능 OK!
```

