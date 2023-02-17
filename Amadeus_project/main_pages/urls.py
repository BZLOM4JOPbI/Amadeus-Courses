from . import views
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import cache_control
from django.conf import settings
from main_pages import services


urlpatterns = [
    path('', views.home, name='home_page'),
    path('regist', views.regist, name='regist_user'),
    path('ide', views.ide, name='ide'),
    path('course', views.course, name='course'),
    path('login', views.user_login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('task/<int:task_number>/', views.task, name='task'),
    path('Amadeus_project/main_pages/views', services.return_response)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))
