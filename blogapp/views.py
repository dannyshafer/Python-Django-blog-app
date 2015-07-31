from django.shortcuts import render
from django.http import HttpResponse
from models import BlogArticle
# Create your views here.
from django.contrib.auth import authenticate, login

def index(request):
  blogs = BlogArticle.objects.all()
  if request.method == 'POST':
    usname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(username=usname, password=pwd)
    if user is not None:
      login(request, user)
      return render(request, "home.html", {'testvar': 'Test string 2!', 'blogs':blogs, 'user':user})
  return render(request, "home.html", {'testvar': 'Test string 2!', 'blogs':blogs, 'user':None})

def createBlog(request):
  newBlog = BlogArticle()
  newBlog.title = request.POST['title']
  newBlog.blog_content = request.POST['blog_content']
  newBlog.author = request.user
  newBlog.save()
  return render(request, "home.html", {'testvar': 'Test string 2!', 'blogs':blogs, 'user':request.user})
