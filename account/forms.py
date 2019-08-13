from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=50,widget=forms.TextInput())
    password = forms.CharField(max_length=200,widget=forms.PasswordInput())
    password_check = forms.CharField(max_length=200,widget=forms.PasswordInput())
    field_order = ['username','password','password2'] # field 가 화면에 보이는 순서를 정의한다.
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username','password']

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=200,widget=forms.TextInput())
    password = forms.CharField(max_length=200,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','password']


