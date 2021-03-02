from django.urls import path
from . import views 

app_name = 'post'

urlpatterns = [
  path('',views.Home,name='home'),
  path('serach',views.Search,name='search'),
  path('detail/<int:id>/',views.PostDetail,name='detail'),
  path('likes/<int:pk>',views.likes,name="likes")
  
]
 