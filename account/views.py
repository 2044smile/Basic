from django.urls.base import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout


def login(request):
    if request.method == "GET":
        return render(request, 'account/login.html', {'form':LoginForm})
    # 여기서 회원가입을 하면 POST로 전달한다 그래서 아래 POST if 문을 정의
    elif request.method == "POST":
        form = LoginForm(request.POST) # 로그인 한 정보를 form에 담아라
        id = request.POST['username']
        pw = request.POST['password']
        user = authenticate(username=id,password=pw)
        # authenticate를 통해 DB의 username과 password를 클라이언트가 요청한 값과 비교
        # 만약 같으면 해당 객체를 반환하고(user) 아니라면 none 반환한다.

        if user:
            dj_login(request, user) # user 객체로 로그인해라
            return render(request, 'books/index.html',{'b_list':user})
        else:
            return render(request, 'account/login.html',{'form':form, 'error':'ID or Password Not Matched!!'})


def logout(request):
    dj_logout(request)
    return render(request, 'books/index.html',{'logout':True})

def signup(request):
    if request.method == "GET": # 회원가입 form을 띄우게끔 설정
        return render(request, 'account/signup.html', {'form':SignupForm})

    elif request.method == "POST":
        form = SignupForm(request.POST) # Signupform 에 입력 된 값을 form 에 저장
        if form.is_valid(): # 입력 된 form 이 문제가 없으면
            if form.cleaned_data['password'] == form.cleaned_data['password_check']: # password 와 password2 가 같으면 유저를 생성해라
                new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['password'])
                new_user.save()
                return render(request, 'books/index.html',{'user': new_user})
            else:
                return render(request, 'account/signup.html',{'form':form, 'error':'Password, Password Not Matched!!'})

        else:

            return render(request, 'account/signup.html', {'form':form})
