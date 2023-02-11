from django.shortcuts import render, redirect
from main_pages.forms import *
from django.contrib.auth import authenticate, login, logout
from main_pages.services import *
import json


def logout_user(request):
    global id
    id = None
    logout(request)
    return redirect("home_page")


def home(request):
    return render(request, 'main_pages/index.html')


def ide(request):
    return render(request, 'main_pages/ide.html')


def course(request):
    return render(request, 'main_pages/course.html')


def user_login(request):

    form = LoginForm(request.POST if request.POST else None)

    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                get_user_id(user.username)
                login(request, user)
                return redirect('home_page')
        else:
            form.message = 'Неверный логин или пароль.'
    else:
        form = LoginForm()
    
    return render(request, 'main_pages/login.html', {'form': form})


def regist(request):
    form = CustomUserForm(request.POST if request.POST else None)

    if form.is_valid():
        user = user_create_and_save_account_in_bd(form)
        login(request, user)
        get_user_id(user.username)
        return redirect('home_page')
    
    context = {
        'form': form,
    }

    return render(request, 'main_pages/regist.html', context)


def task_handler(request, task_number=1, special_task=None):

    msg = add_complete_task(request, task_number) or ''

    context = {
        'msg': msg,
        }

    return render(request, f'main_pages/task{task_number}.html', context)



# костыль конечно но пока так
# потом перепишем
def add_complete_task(request, task):
    token = data_fill(request)
    msg = None

    if isinstance(id, int):
        user = CustomUser.objects.all()[id]
        if token:
            if token['complete'] == 'yes':
                task_view = f'.{token["task"]}. '
                if task_view not in user.progress:
                    user.progress += task_view
                    user.save()
    else:
        msg = 'Не-не-не, не спеши, сначала зарегистрируйся!!!'

    return msg


def get_user_id(your_username):
    global id
    id = CustomUser.objects.get(username=your_username).get_id()


def data_fill(request):
    try:
        data = json.loads(request.body.decode("utf-8-sig"))  # Загрузка JSON
        return data
    except ValueError:
        pass
