from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .services import handle_special_task


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
                    print(user.username)
                    global id
                    id = get_user_id(user.username)
                    login(request, user)
                    print(id)
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
        global id
        id = get_user_id(user.username)
        return redirect('home_page')
    
    context = {
        'form': form
    }

    return render(request, 'main_pages/regist.html', context)


def task_handler(request, task_number, special_task=1):
 
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


def get_user_id(your_username):
    return CustomUser.objects.get(username=your_username).get_id()


# костыль конечно но пока так
# потом перепишем
def add_complete_task(request, task, my_user):
    token = request.POST.get('access_token')
    if token == None:
        task_view = f'.{task}. '

        if task_view not in my_user.progress:
            my_user.progress += task_view
            my_user.save()
    

def user_create_and_save_account_in_bd(form):
    user = form.save()
    user.set_password(user.password)
    user.confirm_password = ''
    user.progress = ''
    user.pos = len(CustomUser.objects.all()) - 1
    user.save()
    return user