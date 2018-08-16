from django.urls import path
from . import views

app_name='bbs'

urlpatterns = [
    path('free/', views.freeList, name="free_list"),
    path('free/create/', views.freeCreate , name="free_create"),
    path('free/<int:pk>/', views.freeRead , name="free_read"),
    path('free/edit/<int:pk>/', views.freeUpdate, name="free_update"),
    path('free/destroy/<int:pk>/', views.freeDetail, name="free_destroy"),
    path('free/like/', views.freeLike, name="free_like"),
    path('free/dislike/', views.freeDisLike, name="free_dislike"),
    
    path('free/comment/', views.freeComment, name="free_comment"),

]