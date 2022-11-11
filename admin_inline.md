# 어드민 사이트 Inline 사용

# Inline 추가(1:N)
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import User, Review

UserAdmin.fieldsets += ('Custom fields', {'fields': ('nickname', 'profile_pic', 'intro',)}),

admin.site.register(User, UserAdmin)

admin.site.register(Review, ReviewAdmin)

admin.site.register(Comment, CommentAdmin)

# 어드민 사이트에서 추가할 모델의 인라인을 설정
class CommentInline(admin.StackedInline):
    model = Comment

# Like 모델은 generic 관계이므로 StackedInline을 쓰는 것이 아닌 GenericStackedInline사용
class LiKeInline(admin.GenericStackedInline):
    model = Like

class ReviewAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
        LikeInline,
    )

class CommentAdmin(admin.ModelAdmin):
    inlines = (
        LikeInline,
    )

```


## MaynToManyField 
```python
# ManyToManyField와 Inline (Follower예시) 
class UserInline(admin.StackedInline):
    # 다대다 관계로 연결된 모델을 인라인으로 수정하려면 model.ManyToManyField.through로 설정
    # self관계인 경우에는 foreign key name도 설정해줘야 한다.
    # manytomanyfield가 가리키는 object를 inline으로 수정하고 싶으면 from_<model>
    # manytomanyfield의 역관계를 수정하고 싶다면 to_<model>로 수정하면된다.
    # following의 역관계 follower를 수정하고 싶은거니까 to_user로 쓴다.
    model = User.Following.through 
    fk_name = 'to_user'
    # admin 페이지에서 의미있는 이름으로 사용하도록 설정해준 것 . 없으면 admin페이지에 이름이 이상하게 설정됨.
    verbose_name = 'Follower'
    verbose_name_plural = 'Followers' 

UserAdmin.fieldsets += ('Custom fields', {'fields': ('nickname', 'profile_pic', 'intro',)}),
UserAdmin.inlines = (UserInline)
```