from django import forms
from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
     class Meta:
         model = Post
         fields = ['title', 'body', 'postImage', 'status']

# class CreateForm(ModelForm):
#   class Meta:
#     model : Post
#     fields = ['title','body','postImage','status']