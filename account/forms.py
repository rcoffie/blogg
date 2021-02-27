from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth import authenticate,login


class RegistrationForm(UserCreationForm):
  username = forms.CharField()
  email    = forms.EmailField()
  password1  = forms.CharField(label='Enter Password',widget=forms.PasswordInput)
  password2    = forms.CharField(label='Enter Password',widget=forms.PasswordInput)


  class Meta:
    model = Account
    fields = ('username','email','password1','password2')

  def cleaned_email(self):
    email = self.cleaned_data['email']
    try:
      account = Account.objects.get(email=email)
    except Exception as e:
      return email 
    raise forms.ValidationError(f'email {email} has alrealdy been taken')

  def cleaned_username(self):
    username = self.cleaned_data['username']
    try:
       account = Account.objects.get(username=username)
    except Exception as e:
      raise forms.ValidationError(f'username {username} alreay exists try a new username')
  
class AccountLoginForm(forms.ModelForm):
  password = forms.CharField(label="password",widget=forms.PasswordInput)
  class Meta:
    model = Account
    fields = ('email','password')

  def clean(self):
    if self.is_valid():
      email = self.cleaned_data['email']
      password = self.cleaned_data['password']
      if not authenticate(email=email,password=password):
        raise forms.ValidationError('invalid login')

 
  
