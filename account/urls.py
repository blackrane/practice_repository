from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('', views.index, name="first_page"),
    path('', views.index, name="favorable"),
    path('info/<int:pk>/',views.myPage, name="my_page"),
    path('logout/', auth_views.logout, name='logout',kwargs={'next_page':'/'}),

]