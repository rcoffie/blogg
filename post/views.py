from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from account .models import *
from django.contrib.auth.models import User
user = User
from django.db.models import Q





# Create your views here.
def Home(request):
  posts = Post.objects.all()
  context = {'posts':posts}
  return render(request,'post/index.html',context)





def PostDetail(request, id):
  post = Post.objects.get(id=id)
  comments = Comment.objects.filter(post=post).order_by('-id')
  likes    = post.likes.count()
  context = {'post':post,'comments':comments,'likes':likes}
  user_id = request.user.id
  if request.method == 'POST':
    if user_id is None:
      return redirect('account:login')
    else:
     content = request.POST['content']
     comment = Comment.objects.create(content=content,user=request.user,post=post)
     comment.save()
     return redirect('/detail/'+str(post.id))
  
      

  return render(request,'post/detail.html',context)



# def likes(request, pk):
#   post = get_object_or_404(Post, id=request.POST.get('post_id'))
  
#   if post.likes.filter(id=request.user.id).exists():
#     post.likes.remove(request.user)
#   else:
#     post.likes.add(request.user)

#   return redirect('/detail/'+str(post.id))


def likes(request, pk):
  post = get_object_or_404(Post, id=request.POST.get('post_id'))

  user_id = request.user.id
  if user_id is None:
    return redirect('account:login')
  else:
    if post.likes.filter(id=request.user.id).exists():
      post.likes.remove(request.user)
    else:
      post.likes.add(request.user)
  return redirect('/detail/'+str(post.id))





def Search(request):
  posts = Post.objects.all()
  query = request.GET.get('q')
  if query:
    posts = Post.filter(title__icontains=query)
  context = {
    'posts':posts,
  }

  return render(request,'post/search.html')