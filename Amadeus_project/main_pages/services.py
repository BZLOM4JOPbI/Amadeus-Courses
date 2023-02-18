'''
Файл с дополнительными функциями
'''
from typing import Optional
from django.core.exceptions import ValidationError
from main_pages.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import json


def check_username_chars(username: str) -> None:
    # в перспективе можно заменить регуляркой
    error_msg = 'Используйте латинские буквы, цифры от 0-9, "_" и "-"!'
    for char in set(username):
        if 'a' <= char.lower() <= 'z':
            continue
        elif char in '_-' or char.isdigit():  
            continue     
        else:    
            raise ValidationError(error_msg)

def check_password_correct(password: str, confirm_password: str) -> None:

    MIN_PASSWORD_LENGTH = 12
    PASSWORD_COMPLEXITY = 5
    error_message = ''

    if password != confirm_password:
        error_message = 'Пароли не совпадают!'

    elif len(password) < MIN_PASSWORD_LENGTH:
        error_message = 'Слишком короткий пароль!'
    
    elif len(set(password)) < PASSWORD_COMPLEXITY:
       error_message = 'Пароль слишком простой!'
    
    elif password.isalpha() or password.isdigit():
        error = ['Цифры от 0-9', 'минимум одну сточную и одну заглавную букву', ]
        error_message = f'Пароль должен содеражать {error[password.isdigit()]}'
        
    elif not is_password_contains_upper_lower_letters(password):
        error = ['строчную', 'заглавную', ]
        # error[test_arg.index(0)] очень не читаемо, переделать логику
        error_message = f'пароль должен соджержать {error[0]} и {error[1]} букву'  
        
    if error_message:
        raise ValidationError(error_message)
    

def is_password_contains_upper_lower_letters(password: str) -> bool:

    test_arg = [0, 0]

    for char in set(password):
        if 'a' <= char.lower() <= 'z':
            if char.isupper():
                test_arg[1] = 1
            else:
                test_arg[0] = 1

    return sum(test_arg) == 2


def user_registration(request, form):

    if form.is_valid():
        user = user_create_and_save_account_in_bd(form)
        login(request, user)
        get_user_id(user.username)
        return True

    context = {
        'form': form,
    }

    return context


def user_create_and_save_account_in_bd(form):
    
    user = form.save()
    user.set_password(user.password)
    user.confirm_password = ''
    user.completed_tasks = '_'
    user.code_of_completed_tasks = ''
    user.position_in_db = len(CustomUser.objects.all()) - 1
    user.save()
    return user

def user_authorization(request, form):

    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                get_user_id(user.username)
                login(request, user)
                return True
        else:
            form.message = 'Неверный логин или пароль.'
    
    return form


def get_user_id(your_username):

    global id
    id = CustomUser.objects.get(username=your_username).get_id()


def task_handler(request, task_number):
    
    global task_n
    task_n = task_number
    msg = 'Не спеши, как нам отслеживать твой прогресс?' if not isinstance(id, int) else ''

    context = {
        'msg': msg,
        }

    return context


def add_complete_task(request, task_number):

    token = parse_json_from_GET_requests(request)

    if isinstance(id, int):
        user = CustomUser.objects.all()[id]
        if token:
            if token['complete'] == 'yes':
                task_number = str(token["task"])
                code_completed_task = token['ideValue']
                if task_number not in user.completed_tasks.split('_'):
                    add_number_completed_task_and_solution_in_bd(user, task_number, code_completed_task)
                else:
                    replace_solution_in_db(user, task_number, code_completed_task)


def add_number_completed_task_and_solution_in_bd(user, task_number, solution_task='ff'):
    user.completed_tasks += f'{task_number}_'
    user.code_of_completed_tasks += f'{solution_task}___'
    user.save()


def replace_solution_in_db(user, task_number, solution_task):
    
    index_solution_in_db = user.completed_tasks[1:].split('_').index(str(task_number))
    solution_tasks = user.code_of_completed_tasks.split('___')
    solution_tasks[index_solution_in_db] = solution_task
    user.code_of_completed_tasks = '___'.join(solution_tasks)
    user.save() 


def return_task_solution(request, task=1):

    if isinstance(id, int):
        user = CustomUser.objects.all()[id]
        task_view_in_bd = str(task)
        if task_view_in_bd in user.completed_tasks:
            task_number = user.completed_tasks[1:].split('_').index(task_view_in_bd)
            return user.code_of_completed_tasks.split('___')[task_number]

def return_response(request):

    if request.method == 'GET':
        code = return_task_solution(request, task_n)
        context= {
            'code': code, 
            }
        return HttpResponse(json.dumps(context))
    elif request.method == 'POST':
        add_complete_task(request, task_n)
        return HttpResponse(json.dumps({}))


def parse_json_from_GET_requests(request):

    try:
        parsed_json = json.loads(request.body.decode("utf-8-sig"))
        return parsed_json
    except ValueError:
        pass