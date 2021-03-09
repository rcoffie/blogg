from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.conf import settings

app_name = 'account'

urlpatterns = [
  path('',views.registration,name='registration'),
  path('login/',views.UserLogin,name='login'),
  path('logout/',views.logout ,name='logout'),


  # password reset
  path('reset_password/',auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),name="reset_password"),
  path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), name="password_reset_done"),
  path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name=('account/password_rest_form.html')),name="password_rest_confirm"),
  path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='account/password_rest_done.html'),name='password_rest_complete')

]
 