from . import views
from django.urls import path
# Я Добавил
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import cache_control
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home_page'),
    path('regist.html', views.regist, name='regist_user'),
    path('ide.html', views.ide, name='ide'),
    path('login.html', views.login, name='login'),
    path('course.html', views.course, name='course')
]


# И это тоже я добавил
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))

# И там еще в manage добавил