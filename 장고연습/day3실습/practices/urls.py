from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("is-odd-even/<int:number>", views.is_odd_even),
    path("calculate/<int:num1>/<int:num2>", views.calculate),
    path("lorem/", views.lorem),
    path("lorem-page/", views.lorem_page),
    path("text/", views.print_text),
]
