from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    #회원목록
    path("index/", views.index, name='index'),
    #회원상세목록
    # path("<int:pk>/", views.detail, name="detail"),
    # #회원정보수정
    # path("edit/", views.edit, name="edit"),
    # #회원가입
    # path("signup/", views.signup, name="signup"),
    # #회원탈퇴
    # path("delete/", views.delete, name="delete"),
    # #로그아웃
    # path("logout/", views.logout, name="logout"),
    # #비밀번호변경
    # path("password_change/", views.password_change, name="password_change"),
]