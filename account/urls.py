from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns = [
    path('', views.index, name='index'),                                            #메인
    path('signup/', views.signup, name="signup"),                                   #회원가입                                   #
    path('logout/', auth_views.logout, name='logout',kwargs={'next_page':'/'}),     #로그아웃

    path('info/',views.myPage, name="my_page"),                                     #회원정보
    path('info/write/',views.myWrite, name="my_write"),
    
]