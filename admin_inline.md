# 어드민 사이트 Inline 사용

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