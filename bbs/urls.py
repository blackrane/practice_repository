from django.urls import path
from . import views

app_name='bbs'

#자유게시판 주소
urlpatterns = [
    path('free/', views.freeList, name="free_list"),
    path('free/create/', views.freeCreate , name="free_create"),
    path('free/<int:pk>/', views.freeRead , name="free_read"),
    path('free/edit/<int:pk>/', views.freeUpdate, name="free_update"),
    path('free/destroy/<int:pk>/', views.freeDestroy, name="free_destroy"),
    path('free/like/', views.freeLike, name="free_like"),
    path('free/dislike/', views.freeDisLike, name="free_dislike"),
    path('free/comment/', views.freeComment, name="free_comment"),
]

#시황분석 게시판 주소
urlpatterns += [
    path('analysis/', views.normalAnalysisList, name="analysis_list"),                          #목록
    path('analysis/create/', views.normalAnalysisCreate , name="analysis_create"),              #쓰기
    path('analysis/<int:pk>/', views.normalAnalysisRead , name="analysis_read"),                #읽기
    path('analysis/edit/<int:pk>/', views.normalAnalysisUpdate, name="analysis_update"),        #수정
    path('analysis/destroy/<int:pk>/', views.normalAnalysisDestroy, name="analysis_destroy"),   #삭제
    path('analysis/like/', views.normalAnalysisLike, name="analysis_like"),                     #추천
    path('analysis/dislike/', views.normalAnalysisDisLike, name="analysis_dislike"),            #비추천
    path('analysis/comment/', views.normalAnalysisComment, name="analysis_comment"),            #댓글
]

#포럼게시판 주소
urlpatterns += [
    path('forum/', views.forumlist, name="forum_list"),
]

#학회 게시판 주소
urlpatterns += [
    path('society/', views.societylist, name="society_list"),
]