from django.urls import path
from . import views 

app_name = 'account'

urlpatterns = [
  path('',views.registration,name='registration'),
  path('login/',views.UserLogin,name='login')
]
 