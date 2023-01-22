from django.shortcuts import render


def index(request):
    return render(request, 'main_pages/index.html')


def regist(request):
    return render(request, 'main_pages/regist.html')


def login(request):
    return render(request, 'main_pages/login.html')


def ide(request):
    return render(request, 'main_pages/ide.html')

