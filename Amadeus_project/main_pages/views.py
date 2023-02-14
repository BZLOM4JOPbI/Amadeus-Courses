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

    msg = 'Не спеши, как нам отслеживать твой прогресс?' if not isinstance(id, int) else ''
    code = ''

    if request.method == 'GET':
        code = return_task_solution(request, task_number) or ''
    else:
        add_complete_task(request)

    context = {
        'msg': msg,
        'code': code,
        }


    return render(request, f'main_pages/task{task_number}.html', context)



# костыль конечно но пока так
# потом перепишем
def add_complete_task(request):
    token = data_fill(request)

    if isinstance(id, int):
        user = CustomUser.objects.all()[id]
        if token:
            if token['complete'] == 'yes':
                task_number = str(token["task"])
                code_complete_task = token['ideValue']
                print(user.completed_tasks)
                if task_number not in user.completed_tasks.split('_'):
                    user.completed_tasks += f'{task_number}_'
                    user.code_of_completed_tasks += f'{code_complete_task}___'
                    user.save()
                else:
                    index_solution_in_db = user.completed_tasks[1:].split('_').index(str(task_number))
                    solution_tasks = user.code_of_completed_tasks.split('___')
                    solution_tasks[index_solution_in_db] = code_complete_task
                    user.code_of_completed_tasks = '___'.join(solution_tasks)
                    user.save() 

    return


def get_user_id(your_username):
    global id
    id = CustomUser.objects.get(username=your_username).get_id()


def data_fill(request):
    try:
        data = json.loads(request.body.decode("utf-8-sig"))  # Загрузка JSON
        return data
    except ValueError:
        pass



def return_task_solution(request, task):

    if isinstance(id, int):
        user = CustomUser.objects.all()[id]
        task_view_in_bd = str(task)
        if task_view_in_bd in user.completed_tasks:
            print(user.completed_tasks[1:].split('_'))
            task_number = user.completed_tasks[1:].split('_').index(task_view_in_bd)
            return user.code_of_completed_tasks.split('___')[task_number]
