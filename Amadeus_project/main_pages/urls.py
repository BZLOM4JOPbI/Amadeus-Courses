from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home_page'),
    path('test_regist.html', views.SignUpUser.as_view(), name='regist_user'),
    path('ide.html', views.ide, name='ide'),
    path('login.html', views.login, name='login'),
]
