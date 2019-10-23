from django.shortcuts import render
from django.http import HttpResponse
from blogsite.models import Post
from blogsite.forms import PostForm  

def index(request):
    posts = Post.objects.all()
    context_dict = {'posts': posts}
    return render(request, 'index.html', context_dict)

def get_post(request, post_id):
    post=Post.objects.get(id=post_id)
    context_dict = {'post': post}
    print(post)
    return render(request, 'show_post.html', context_dict)

def create_post(request):
    if "GET" == request.method:
        post = PostForm() 
        return render(request, 'create_post.html', {'form': post })
    else:
        request.POST["title"]
        b = Post(title=request.POST["title"], content=request.POST["content"], author=request.POST["author"])
        b.save()
        return render(request, 'successful_post_creation.html', {})