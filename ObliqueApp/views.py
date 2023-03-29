from django.shortcuts import render

from ObliqueApp.forms import BlogForm

# Create your views here.
def home(request):
    return render(request,'index.html') 

def about(request):
    return render(request,'about.html') 

def contact(request):
    return render(request,'contact.html') 


def addpost(request):
    form = BlogForm()
    return render(request,'addpost.html', {'forms': form}) 

def addblog(request):
    form = BlogForm()
    return render(request,'addblog.html', {'forms': form}) 

def addservice(request):
    form = BlogForm()
    return render(request,'addservice.html', {'forms': form}) 


def loginuser(request):
    return render(request,'login.html') 