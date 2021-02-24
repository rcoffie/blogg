from django.db import models
from account.models import Account

# Create your models here.
class Post(models.Model):
  status_choices=(
    ('draft','draft'),
    ('published','published'),
  )
  category=(
    ('technology','technology'),
    ('entertainment','entertainment'),
    ('lifestyle','lifestyle'),
    ('other','other')
  )
  title    = models.CharField(max_length=100)
  author   = models.ForeignKey(Account, on_delete=models.CASCADE)
  body     = models.TextField()
  postImage     = models.ImageField(upload_to='photos/%Y/%m/%d') 
  likes         = models.ManyToManyField(Account,related_name='blog_post', blank=True)
  created       = models.DateTimeField(auto_now_add=True) 
  updated       = models.DateTimeField(auto_now=True)  
  category      = models.CharField(max_length=15,choices=category,default='other',blank=True)
  status        = models.CharField(max_length=15, choices=status_choices,default='draft')


  def __str__(self):
    return self.title


class Comment(models.Model):
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
  user = models.ForeignKey(Account,on_delete=models.CASCADE)
  content = models.TextField(max_length=400)
  created  = models.DateTimeField(auto_now_add=True)

