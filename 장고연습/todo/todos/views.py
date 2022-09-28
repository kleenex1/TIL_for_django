from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all().order_by("priority")
    context = {"todos": todos}
    return render(request, "todos/index.html", context)


def todo_create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect("/todos")


def todo_delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect("/todos")


def todo_update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo.completed:
        todo.completed = False
        todo.save()
    else:
        todo.completed = True
        todo.save()
    return redirect("/todos")
