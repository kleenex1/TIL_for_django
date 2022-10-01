from django.shortcuts import render, redirect, get_object_or_404
# from django.http import Http404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
# 클래스형 뷰를 위한 View클래스를 상속받아쓴다
from django.views import View
# 제네릭 뷰를 상속 받는다
from django.views.generic import CreateView
# reverse
from django.urls import reverse
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    curr_page_number = request.GET.get('page')
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number)
    return render(request, 'posts/post_list.html', {'page': page})
    # context = {"posts": posts}
    # return render(request, "posts/post_list.html", context)

# def post_detail(request, post_id):
#     post = Post.objects.get(id=post_id)
#     context = {"post": post}
#     return render(request, "posts/post_detail.html", context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'posts/post_detail.html', context)

# def post_detail(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         raise Http404()
    
#     context = {'post': post}
#     return render(request, 'posts/post_detail.html', context)

# def post_create(request):
#     if request.method == "POST":
#         title = request.POST["title"]
#         content = request.POST["content"]
#         new_post = Post(title=title, content=content)
#         new_post.save()
#         return redirect("post-detail", post_id=new_post.id)
#     else:
#         post_form = PostForm()
#         return render(request, "posts/post_form.html", {"form": post_form})

## 폼 함수 적용

# def post_create(request):
#     if request.method == "POST":
#         post_form = PostForm(request.POST) # 폼과 데이터를 바인딩해준다.
#         if post_form.is_valid():
#             new_post = post_form.save() 
#         # 바인딩된 내용을 세이브해주면 데이터베이스에 
#         # 저장해줄수 있는데, 모델폼이 가지고있는 세이브 함수는 
#         # 바운드폼으로부터 가저온데이터로 모델인스턴스를 만들고 
#         # 인스턴스를 데이터베이스에 처리하는 과정을 진행해준다.
#             return redirect("post-detail", post_id=new_post.id)
#     else:
#         post_form = PostForm()
#     return render(request, "posts/post_form.html", {"form": post_form})

## 클래스형 뷰로 변환

# class PostCreateView(View):
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, "posts/post_form.html", {"form": post_form})

#     def post(self, request):
#         post_form = PostForm(request.POST) 
#         if post_form.is_valid():
#             new_post = post_form.save() 
#             return redirect("post-detail", post_id=new_post.id)

## 제네릭 뷰로 변환
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})


def post_update(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail', post_id=post.id)
    else:
        post_form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': post_form})

def post_delete(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'posts/post_confirm_delete.html', {'post':post})

def index(request):
    return redirect('post-list')