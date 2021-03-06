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
  if request.method== 'POST':
    post = Post(
      title = request.POST['title'],
      body  = request.POST['body'],
      postImage = request.FILES['postImage'],
      author = request.user
    )
    post.save()
    return redirect('super_u:create_post')
  context = {'form':form}

  return render(request,'super_u/index.html',context)

def listPosts(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts':posts}


    return render(request,'super_u/posts.html',context)


def EditPost(request, id):
  post = get_object_or_404(Post, id=id)
  updateForm = PostForm(request.POST or None, instance=post)
  if updateForm.is_valid():
    updateForm.save()
    return redirect('/super_u/posts.html')
  context = {'updateForm':updateForm}

  return render(request,'super_u/update.html',context)

def PostDelete(request, id):
  post = get_object_or_404(Post, id=id)
  if request.method == 'POST':
    post.delete()
    # return HttpResponse('super_u/posts.html')
    return redirect('/super_u/post.html')

  return render(request,'super_u/posts.html')