from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home_page'),
    path('regist.html', views.regist, name='regist_user'),
    path('ide.html', views.ide, name='ide'),
    path('login.html', views.login, name='login'),
]
