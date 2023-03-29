from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='home',),
    path("about/", views.about, name='about',),
    path("contact/", views.contact, name='contact',),
    # path("post/", views.post, name='post',),
    # path("service/", views.post, name='service',),
    path("post/", views.addpost, name='post',),
    path("blog/", views.addblog, name='blog',),
    path("service/", views.addservice, name='service',),
    path("login/", views.loginuser, name='login',),
    
]