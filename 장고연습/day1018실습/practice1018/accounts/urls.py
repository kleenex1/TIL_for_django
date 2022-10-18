from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/list', views.accounts_list, name='list'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/<int:pk>/detail', views.detail, name='detail'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/<int:pk>/update', views.update, name='update'),
    path('accounts/password/', views.change_password, name='change_password'),
    path('accounts/delete/', views.delete, name='delete'),
    path('create/', views.review_create, name='review-create'),
    path('update/<int:pk>', views.review_update, name='review-update'),
    path('update/<int:pk>', views.review_delete, name='review-delete'),
    path('detail/<int:pk>', views.review_detail, name='review-detail'),
    path('<int:pk>/comments/', views.comment_create, name='comment-create')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)