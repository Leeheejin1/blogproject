from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .form import Postform
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator

def home(request):
    post = Post.objects.all().order_by('-id')
    blogs = Post.objects
    blog_list = Post.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'home.html',{'post':post, 'blogs':blogs, 'posts':posts})

def write(request):
    return render(request,'write.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('home')

def updatemodify(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':  
        form = Postform(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('home')
    else:
        form = Postform()
        return render(request,'modify.html',{'form':form})

def delete(request,post_id):
    post = get_object_or_404(Post, id = post_id)
    post.delete()
    return redirect('home')

def signup(request):
        if request.method == 'POST':
                if request.POST['password1'] == request.POST['password2']:
                        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                        auth.login(request,user)
                        return redirect('home')
        return render(request,'signup.html')

def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(request,username=username, password=password)
                if user is not None:
                        auth.login(request,user)
                        return redirect('home')
                else:
                        return render(request,'login.html',{'error':'username or password is incorrect'})
        else:
                return render(request,'login.html')

def logout(request):
        if request.method=="POST":
                auth.logout(request)
                return redirect('home')
        else:
                return render(request,'login.html')