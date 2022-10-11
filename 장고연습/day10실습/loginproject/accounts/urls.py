from django.urls import path
from . import views
urlpatterns = [
    path('', views.button, name='button'),
    path('accounts/', views.index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/<int:pk>/', views.detail, name='detail'),
]