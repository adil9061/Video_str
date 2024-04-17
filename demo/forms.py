from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from demo.models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'video_file')