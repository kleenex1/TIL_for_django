from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# from .models 
# Create your views here.

def index(request):
    return render(request, "accounts/index")


@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)

    return render(request, 'accounts/detail.html', {"user":user})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('index')

@login_required
def edit(request, pk):
    user = get_user_model.objects.get(pk=pk)
    if request.user == user:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('detail', request.user.pk)
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/update.html', context)
    else:
        return HttpResponseForbidden()

@login_required
def password_change(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('index')