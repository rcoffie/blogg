from django.shortcuts import render,redirect,get_object_or_404
from . models import *

# Create your views here.
def Home(request):
  posts = Post.objects.all()
  context = {'posts':posts}
  return render(request,'post/index.html',context)





def PostDetail(request, id):
  post = Post.objects.get(id=id)
  context = {'post':post,}

  return render(request,'post/detail.html',context)