from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUpUser(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('main_pages/index.html')
    template_name = 'main_pages/test_regist.html'


def index(request):
    return render(request, 'main_pages/index.html')


def login(request):
    return render(request, 'main_pages/login.html')


def ide(request):
    return render(request, 'main_pages/ide.html')
