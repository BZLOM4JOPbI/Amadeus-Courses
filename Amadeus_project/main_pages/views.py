from django.shortcuts import render, redirect
from main_pages.forms import *
from django.contrib.auth import authenticate, login, logout
from main_pages.services import *
import json


def logout_user(request):
    logout(request)
    return redirect("home_page")


def home(request):
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
    msg = False

    if form.is_valid():
        msg = True
        user = user_create_and_save_account_in_bd(form)
        login(request, user)
        get_user_id(user.username)
        return redirect('home_page')
    
    context = {
        'form': form,
        'msg': msg,
    }

    return render(request, 'main_pages/regist.html', context)


def task_handler(request, task_number=1, special_task=1):
    print(id)
    
    if isinstance(id, int):
    
        user = CustomUser.objects.all()[id]
        add_complete_task(request, task_number, user)
        return render(request, f'main_pages/task{task_number}.html') # для тестов потом уберем

    else:
        return redirect('login')

    # if task_number == special_task:
    #     form = None
    #     context = handle_special_task(form)
    #     if context:
    #         return render(request, f'main_pages/task{special_task}.html', context)
    #     else:
    #         return redirect('login')
    # else:
    #     return render(request, f'main_pages/task{task_number}.html')


# костыль конечно но пока так
# потом перепишем
def add_complete_task(request, task, my_user):
    token = data_fill(request)
    
    if token:
        if token['complete'] == 'yes':
            task_view = f'.{token["task"]}. '

            if task_view not in my_user.progress:
                my_user.progress += task_view
                my_user.save()
    
# # парсинг json
# def data_fill(request):
#     try:
#         data = json.loads(request.body.decode("utf-8-sig"))  # Загрузка JSON
#         return data
#     except ValueError:
#         print('угу')
id = -1.0
def get_user_id(your_username):
    global id
    id = CustomUser.objects.get(username=your_username).get_id()

