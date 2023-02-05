from . import views
from django.urls import path
# Я Добавил
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import cache_control
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home_page'),
    path('regist', views.regist, name='regist_user'),
    path('ide', views.ide, name='ide'),
    path('course', views.course, name='course'),
    path('login', views.user_login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('task1', views.task_one, name='task_one'),
    path('task2', views.task_two, name='task_two'),
    path('task3', views.task_three, name='task_three'),
    path('task4', views.task_four, name='task_four'),
]


# И это тоже я добавил
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))

# И там еще в manage добавил