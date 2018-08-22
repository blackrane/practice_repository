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