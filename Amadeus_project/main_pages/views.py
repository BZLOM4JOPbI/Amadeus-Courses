from django.shortcuts import render, redirect
from .forms import CustomUserForm


# class SignUpUser(CreateView):

#     form_class = CustomUserForm
#     success_url = reverse_lazy('main_pages/index.html')
#     template_name = 'main_pages/test_regist.html'

def regist(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home_page')
    form = CustomUserForm
    context = {
        'form': form
    }
    return render(request, 'main_pages/regist.html', context)


def index(request):
    return render(request, 'main_pages/index.html')


def login(request):
    return render(request, 'main_pages/login.html')


def ide(request):
    return render(request, 'main_pages/ide.html')
