from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("create/", views.todo_create),
    path("delete/<int:todo_id>", views.todo_delete),
    path("edit/<int:todo_id>", views.todo_update),
]
