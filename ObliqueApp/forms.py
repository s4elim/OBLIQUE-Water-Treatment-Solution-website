from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
      class Meta:
        model = Blog
        fields = ('title','post','img')
        labels = {
            'title': 'Your post title',
            'post' : 'Write your post here..'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control-sm'}),
        }


