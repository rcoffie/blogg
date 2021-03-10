from django.shortcuts import render,redirect
from .models import *
from . forms import *
from django.contrib import messages,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.



def registration(request):
  if request.method== 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'account created successfully')
      return redirect('post:home')
  else:
    form = RegistrationForm()
  context = {'form':form}
  return render(request, 'account/register.html',context)




def UserLogout(request):
  logout(request)
  return redirect('post:home')
  
 



 
def UserLogin(request):
  form = AccountLoginForm()
  if request.POST:
    form = AccountLoginForm(request.POST)
    if form.is_valid():
     email = request.POST['email']
     password = request.POST['password']
     user = authenticate(email=email,password=password)
     if user:
       login(request, user)
       return redirect('post:home')
     else:
       forms.ValidationError("incorrect email or password")
  context = {'form':form}
  return render(request,'account/login.html',context)
   


# def UserLogin(request):
#   form = AccountLoginForm()

#   return render(request,'account/login.html')