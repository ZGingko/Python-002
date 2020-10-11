from django.shortcuts import render

# Create your views here.
from .form import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("Hello Django!")


def mylogin(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return render(request, 'index.html', {'form': login_form}) # HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')
    
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})
