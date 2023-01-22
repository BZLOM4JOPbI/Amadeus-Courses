from . import views
from django.urls import path

urlpatterns = [
    path('index.html', views.index),
    path('regist.html', views.regist),
    path('ide.html', views.ide),
    path('login.html', views.login),
]
