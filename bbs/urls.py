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

#꿀팁 게시판
urlpatterns += [
    path('honeytip/', views.honeyTipList, name="honeytip_list"),                          #목록
    path('honeytip/create/', views.honeyTipCreate , name="honeytip_create"),              #쓰기
    path('honeytip/<int:pk>/', views.honeyTipRead , name="honeytip_read"),                #읽기
    path('honeytip/edit/<int:pk>/', views.honeyTipUpdate, name="honeytip_update"),        #수정
    path('honeytip/destroy/<int:pk>/', views.honeyTipDestroy, name="honeytip_destroy"),   #삭제
    path('honeytip/like/', views.honeyTipLike, name="honeytip_like"),                     #추천
    path('honeytip/dislike/', views.honeyTipDisLike, name="honeytip_dislike"),            #비추천
    path('honeytip/comment/', views.honeyTipComment, name="honeytip_comment"),            #댓글
]

#갤러리 게시판
urlpatterns += [
    path('gallery/', views.galleryList, name="gallery_list"),                          #목록
    path('gallery/create/', views.galleryCreate , name="gallery_create"),              #쓰기
    path('gallery/<int:pk>/', views.galleryRead , name="gallery_read"),                #읽기
    path('gallery/edit/<int:pk>/', views.galleryUpdate, name="gallery_update"),        #수정
    path('gallery/destroy/<int:pk>/', views.galleryDestroy, name="gallery_destroy"),   #삭제
    path('gallery/like/', views.galleryLike, name="gallery_like"),                     #추천
    path('gallery/dislike/', views.galleryDisLike, name="gallery_dislike"),            #비추천
    path('gallery/comment/', views.galleryComment, name="gallery_comment"),            #댓글
]
#포럼게시판 주소
urlpatterns += [
    path('forum/', views.forumlist, name="forum_list"),
]

 #비트코인
urlpatterns += [
    path('forum/bitcoin/', views.forumBitCoinList, name="forumbitcoin_list"),                          #목록
    path('forum/bitcoin/create/', views.forumBitCoinCreate , name="forumbitcoin_create"),              #쓰기
    path('forum/bitcoin/<int:pk>/', views.forumBitCoinRead , name="forumbitcoin_read"),                #읽기
    path('forum/bitcoin/edit/<int:pk>/', views.forumBitCoinUpdate, name="forumbitcoin_update"),        #수정
    path('forum/bitcoin/destroy/<int:pk>/', views.forumBitCoinDestroy, name="forumbitcoin_destroy"),   #삭제
    path('forum/bitcoin/like/', views.forumBitCoinLike, name="forumbitcoin_like"),                     #추천
    path('forum/bitcoin/dislike/', views.forumBitCoinDisLike, name="forumbitcoin_dislike"),            #비추천
    path('forum/bitcoin/comment/', views.forumBitCoinComment, name="forumbitcoin_comment"),            #댓글
]

#학회 게시판 주소
urlpatterns += [
    path('society/', views.societylist, name="society_list"),
]

#호재게시판
urlpatterns += [
    path('favorable/', views.favorable, name="favorable"),
    path('favorable/like/', views.favorableLike, name="favorable_like")
]