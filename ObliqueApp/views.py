from django.shortcuts import redirect, render
from django.contrib.auth import logout as authlogout, authenticate,login as authlogin

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
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            authlogin(request, user)
        else:
            print(username, password)
    return render(request,'login.html') 

def logout(request):
    authlogout(request)
    return redirect('home') 