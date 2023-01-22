from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('test_regist.html', views.SignUpUser.as_view()),
    path('ide.html', views.ide),
    path('login.html', views.login),
]
