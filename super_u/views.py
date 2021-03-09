from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from post.models import *
from post.forms import *
from django.contrib.auth.models import User

# Create your views here.
#if not request.user.is_authenticated
#return redirect 

# def CreatePost(request):
#   form = PostForm()
#   if request.method == "POST":
#     form  = PostForm(request.POST)
#     if form.is_valid():
#       instance = form.save(commit=False)
#       postImage = request.Files['image']
#       author   = request.user
#       form.save()
#       return redirect('super_u:create_post')
#   context = {'form':form}
#   return render(request,'super_u/index.html',context)


def CreatePost(request):
  user = User 
  form = PostForm()
  if request.user.is_superuser:

   if request.method== 'POST':
     post = Post(
       title = request.POST['title'],
       body  = request.POST['body'],
       postImage = request.FILES['postImage'],
       author = request.user
     )
     post.save()
     return redirect('super_u:create_post')
  else:
    return redirect('post:home')
  context = {'form':form}

  return render(request,'super_u/index.html',context)

def listPosts(request):
   if request.user.is_superuser:

     posts = Post.objects.filter(author=request.user)
     context = {'posts':posts}
   else:
    return redirect('post:home')


   return render(request,'super_u/posts.html',context)


def EditPost(request, id):
  if request.user.is_superuser:

   post = get_object_or_404(Post, id=id)
   updateForm = PostForm(request.POST or None, instance=post)
   if updateForm.is_valid():
     updateForm.save()
     return redirect('super_u:super_posts')
   context = {'updateForm':updateForm}
  else:
    return redirect('post:home')

  return render(request,'super_u/update.html',context)

def PostDelete(request, id):
  if request.user.is_superuser:

   post = get_object_or_404(Post, id=id)
   if request.method == 'POST':
     post.delete()
    # return HttpResponse('super_u/posts.html')
     return redirect('super_u:super_posts')
  else:
    return redirect('post:home')

  return render(request,'super_u/posts.html')