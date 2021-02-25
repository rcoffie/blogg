from django.urls import path
from . import views 

app_name = 'post'

urlpatterns = [
  path('',views.Home,name='home'),
  path('detail/<int:id>/',views.PostDetail,name='detail')
  
]
 