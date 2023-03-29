from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300)
    post = models.TextField()
    img = models.ImageField(upload_to='media/blog')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    img = models.ImageField(upload_to='media/about')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title