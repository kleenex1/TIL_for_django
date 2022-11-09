# 제네릭 뷰를 사용함으로써 아래 2줄은 사용하지 않아도 됨
# from django.shortcuts import render, redirect, get_object_or_404
# from django.core.paginator import Paginator


# from django.http import Http404
from .models import Post
from .forms import PostForm
# 클래스형 뷰를 위한 View클래스를 상속받아쓴다
from django.views import View
# 제네릭 뷰를 상속 받는다
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
    )
# reverse
from django.urls import reverse
# Create your views here.


# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 6)
#     curr_page_number = request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     return render(request, 'posts/post_list.html', {'page': page})
#     # context = {"posts": posts}
#     # return render(request, "posts/post_list.html", context)

class PostListView(ListView):
    model = Post
    # template_name = 'posts/post_list.html'
    # 템플릿 명은 기본적으로 모델명_list를 사용하여 쓰고 있어서 
    # 자동으로 찾아주기 때문에 template_name을 안써줘도 된다.
    # context_object_name = 'posts'
    # 안 적어줘도 object_list형태로 넘어간다.. 이부분은 다시(15.더 빠르게 더 간단하게I)
    ordering = ['-dt_created']
    paginate_by = 6
    # page_kwarg = 'page'
    # 현재 페이지에 해당하는 내용을 가져오기위한 키워드를 적어주는 부분 
    # page_kwarg의 기본값은 page이다 쿼리스트링에 page라는 키워드로 현재페이지에 대한 
    # 번호가 있으니까 가져와서 pagination을 사용한다. 


# def post_detail(request, post_id):
#     post = Post.objects.get(id=post_id)
#     context = {"post": post}
#     return render(request, "posts/post_detail.html", context)

# def post_detail(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         raise Http404()
    
#     context = {'post': post}
#     return render(request, 'posts/post_detail.html', context)

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     context = {'post': post}
#     return render(request, 'posts/post_detail.html', context)


class PostDetailView(DetailView):
    model = Post
    # template_name = 'posts/post_detail.html' 
    # 템플릿 이름을 그대로 쓰고 있기때문에 모델명_detail.html 생략가능
    # pk_url_kwarg ='post_id'
    # 기본값은 pk 이기 때문에 url에서 pk로 바꿔준다.
    # pk_url_kwarg = pk -> url 에서 posts/<int:pk>
    # context_object_name = 'post'
    # context_object_name은 디테일뷰에서 하나의 데이터를
    # 컨텍스트로 넘겨줄때는 object라는 키워드와 모델명을 소문자로적은
    # post라는 키워드가 기본적으로 사용된다. 지금 이미 post라고 쓰고
    # 있기 때문에 따로 안적어도 기본적으로 작동한다.





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
#         return render(request, 'posts/post_form.html', {'form': post_form})

## 제네릭 뷰로 변환
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # CreateView는 사용자의 입력을 받아야 하는 부분이다
    # form_class변수에 Createview에서 사용할 Form 클래스를 써주면된다.
    # 이 폼은 자동으로 Form이라는 키워드로 템플릿에 컨텍스트가 전달된다.
    # Form이라는 키워드를 이용해서 Form 요소에 접근할 수 있게 되는것.
    # -> post_form에 템플릿 변수로 form을 쓰고있음.
    # template_name = 'posts/post_form.html'

    def get_success_url(self):
        # return reverse('post-detail', kwargs={'post_id': self.object.id})
        # detail view에서 아까 pk로 바꿨기 때문에 pk로 바꿔줘야함!
        return reverse('post-detail', kwargs={'pk': self.object.id})



# def post_update(request, post_id):
#     # post = Post.objects.get(id=post_id)
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post.id)
#     else:
#         post_form = PostForm(instance=post)
#     return render(request, 'posts/post_form.html', {'form': post_form})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'
    # pk_url_kwarg = 'post_id'
    # pk_url_kwarg = 'pk' 위 클래스들과 같음
    
    def get_success_url(self):
        # return reverse('post-detail', kwargs={'post_id':self.object.id})
        return reverse('post-detail', kwargs={'pk':self.object.id})


# def post_delete(request, post_id):
#     # post = Post.objects.get(id=post_id)
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post-list')
#     else:
#         return render(request, 'posts/post_confirm_delete.html', {'post':post})

class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'posts/post_confirm_delete.html'
    # pk_url_kwarg = 'post_id'
    # pk_url_kwarg = 'pk'
    # context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-list')

# def index(request):
#     return redirect('post-list')

class IndexRedirectView(RedirectView):
    pattern_name = "post-list"