from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# UserCreationForm: 기본적으로 유저 이름, 패스워드
class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    class Meta:
        model = User
        fields = ('username', 'email')