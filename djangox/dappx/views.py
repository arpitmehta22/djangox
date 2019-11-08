# dappx/views.py
from django.shortcuts import render
from dappx.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return render(request,'dappx/index.html')
def about(request):
    return render(request,'dappx/about.html')
def blog(request):
    return render(request,'dappx/blog.html')
def candidates(request):
    return render(request,'dappx/candidates.html')
def blog_single(request):
    return render(request,'dappx/blog-single.html')
def contact(request):
    return render(request,'dappx/contact.html')
def job_post(request):
    return render(request,'dappx/job-post.html')
def new_post(request):
    return render(request,'dappx/new-post.html')
