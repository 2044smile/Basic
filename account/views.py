from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return render(request, 'books/index.html')
        else:
            return render(request, 'account/login.html',{'form': LoginForm(), 'test':'username or password is incorrect'})
    else:
        return render(request, 'account/login.html',{'form': LoginForm()})

def logout(request):
    dj_logout(request)
    return render(request, 'books/index.html',{'logout':True})

def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password_check"]:
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password"]
            )
            dj_login(request,user)
            return redirect('index') # 회원가입 완료 시 index.html 로 이동
        return render(request, 'account/signup.html',{'error':'password Not matched!!', 'form':SignupForm})
    return render(request, 'account/signup.html', {'form': SignupForm})

