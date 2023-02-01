from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.http import HttpResponse


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("home_page")


def regist(request):
    form = CustomUserForm(request.POST if request.POST else None)
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    context = {
        'form': form
    }
    return render(request, 'main_pages/regist.html', context)


def index(request):
    return render(request, 'main_pages/index.html')


def ide(request):
    return render(request, 'main_pages/ide.html')


def course(request):
    return render(request, 'main_pages/course.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home_page')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main_pages/login.html', {'form': form})
