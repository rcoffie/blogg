from django.urls import path
from . import views 


app_name = 'super_u'

urlpatterns = [
  
 path('',views.CreatePost,name="create_post"),
 path('posts/',views.listPosts,name="super_posts"),
 path('update/<id>/',views.EditPost,name='super_edit'),
 path('<id>/delete',views.PostDelete,name="super_delete")

]
 