from django.shortcuts import render
from . models import *

# Create your views here.
def Home(request):
  posts = Post.objects.all()
  context = {'posts':posts}
  return render(request,'post/index.html',context)