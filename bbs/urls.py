from django.urls import path
from . import views

app_name='bbs'

urlpatterns = [
    path('free/', views.freeList, name="free_list"),
    path('free/create/', views.freeCreate , name="free_create"),
    path('free/<int:pk>/', views.freeRead , name="free_read"),
    path('free/edit/<int:pk>/', views.freeUpdate, name="free_update"),
    path('free/destroy/<int:pk>/', views.freeDestroy, name="free_destroy"),
    path('free/like/', views.freeLike, name="free_like"),
    path('free/dislike/', views.freeDisLike, name="free_dislike"),
    path('free/comment/', views.freeComment, name="free_comment"),
    path('forum/', views.forumlist, name="forum_list"),
    path('society/', views.societylist, name="society_list"),
]

urlpatterns += [
    path('analysis/', views.normalAnalysisList, name="analysis_list"),                
    path('analysis/create/', views.normalAnalysisCreate , name="analysis_create"),
    path('analysis/<int:pk>/', views.normalAnalysisRead , name="analysis_read"),
    path('analysis/edit/<int:pk>/', views.normalAnalysisUpdate, name="analysis_update"),
    path('analysis/destroy/<int:pk>/', views.normalAnalysisDestroy, name="analysis_destroy"),
    path('analysis/like/', views.normalAnalysisLike, name="analysis_like"),
    path('analysis/dislike/', views.normalAnalysisDisLike, name="analysis_dislike"),
    path('analysis/comment/', views.normalAnalysisComment, name="analysis_comment"),
]