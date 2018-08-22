from django.urls import path
from . import views
app_name='bk'

#판매게시판
urlpatterns = [
    path('market/', views.marketBoardList, name="market_list"),                          #목록
    path('market/create/', views.marketBoardCreate , name="market_create"),              #쓰기
    path('market/<int:pk>/', views.marketBoardRead , name="market_read"),                #읽기
    path('market/edit/<int:pk>/', views.marketBoardUpdate, name="market_update"),        #수정
    path('market/destroy/<int:pk>/', views.marketBoardDestroy, name="market_destroy"),   #삭제
    path('market/like/', views.marketBoardLike, name="market_like"),                     #추천
    path('market/dislike/', views.marketBoardDisLike, name="market_dislike"),            #비추천
    path('market/comment/', views.marketBoardComment, name="market_comment"),            #댓글
]

#이벤트 게시판
urlpatterns += [
    path('event/', views.eventList, name="event_list"),                          #목록
    path('event/create/', views.eventCreate , name="event_create"),              #쓰기
    path('event/<int:pk>/', views.eventRead , name="event_read"),                #읽기
    path('event/edit/<int:pk>/', views.eventUpdate, name="event_update"),        #수정
    path('event/destroy/<int:pk>/', views.eventDestroy, name="event_destroy"),   #삭제
    path('event/like/', views.eventLike, name="event_like"),                     #추천
    path('event/dislike/', views.eventDisLike, name="event_dislike"),            #비추천
    path('event/comment/', views.eventComment, name="event_comment"),            #댓글
]