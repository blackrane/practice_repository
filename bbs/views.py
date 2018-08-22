from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test

#App 
from coinsense.bbs import BoardCreateView, BoardListView, BoardReadView, BoardUpdateView, BoardDestroyView, LikeView, DisLikeView, CommentView, ForumListView
from . import models
from . import forms
from account.forms import LoginForm

# 게시판 필요 View 
# BoardCreateview, BoardListView, BoardReadView, BoardUpdateView, 
# BoardDestroyView, LikeView, DisLikeView, CommentView 총 8개

#자유게시판
freeList = BoardListView.as_view(
    model = models.FreeBoard,
    login_form = LoginForm ,
    success_url = '/free/',
    template_name='Board_List.html',
    create_url = 'bbs:free_create',
    read_url='bbs:free_read',
    title ="자유게시판"
)

freeCreate = BoardCreateView.as_view(
    model = models.FreeBoard,
    form_class = forms.FreeBoardCreationForm,
    template_name='Board_Create.html',
    title ="자유게시판 게시글 작성"
)

freeRead = BoardReadView.as_view(
    model = models.FreeBoard,
    comment_model = models.FreeBoardComment,
    comment_Form_class =  forms.FreeBoardCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="자유게시판",
    like_url='bbs:free_like',
    dislike_url='bbs:free_dislike',
    update_url='bbs:free_update',
    destroy_url='bbs:free_destroy',
    comment_url='bbs:free_comment',
)

freeUpdate = BoardUpdateView.as_view(
    model = models.FreeBoard,
    form_class= forms.FreeBoardCreationForm,
    success_url = '/free/',
    template_name='Board_Create.html',
    title ="자유게시판 게시글 수정"
)

freeDestroy = BoardDestroyView.as_view()

freeLike = LikeView.as_view(
    model = models.FreeBoard
)

freeDisLike = DisLikeView.as_view(
    model = models.FreeBoard
)

freeComment = CommentView.as_view(
    model = models.FreeBoard,
    form_class = forms.FreeBoardCommentForm,
    template_name="Comment.html",
)

#일반시황분석
normalAnalysisList = BoardListView.as_view(
    model= models.NormalAnalysis,
    login_form = LoginForm ,
    success_url ='/analysis/',
    template_name = "Board_List.html",
    create_url = 'bbs:analysis_create',
    read_url='bbs:analysis_read',
    title="시황분석공유",
)

normalAnalysisCreate = BoardCreateView.as_view(
    model = models.NormalAnalysis,
    form_class = forms.NormalAnalysisCreationForm,
    template_name='Board_Create.html',
    title ="시황분석 게시글 작성"
)
normalAnalysisRead = BoardReadView.as_view(
    model = models.NormalAnalysis,
    comment_model = models.NormalAnalysisComment,
    comment_Form_class = forms.NormalAnalysisCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="시황분석공유",
    like_url='bbs:analysis_like',
    dislike_url='bbs:analysis_dislike',
    update_url='bbs:analysis_update',
    destroy_url= 'bbs:analysis_destroy',
    comment_url= 'bbs:analysis_comment',
)
normalAnalysisUpdate = BoardUpdateView.as_view(
    model = models.NormalAnalysis,
    form_class= forms.NormalAnalysisCreationForm,
    success_url = '/free/',
    template_name='Board_Create.html',
    title ="시황분석공유 게시글 수정",
)

normalAnalysisDestroy = BoardDestroyView.as_view(
    
)

normalAnalysisLike = LikeView.as_view(
    model = models.NormalAnalysis
)

normalAnalysisDisLike = DisLikeView.as_view(
    model = models.NormalAnalysis
)

normalAnalysisComment = CommentView.as_view(
    model = models.NormalAnalysis,
    form_class = forms.NormalAnalysisCommentForm,
    template_name="Comment.html",
)


#갤러리
galleryList = BoardListView.as_view(
    model= models.Gallery,
    login_form = LoginForm ,
    success_url ='/gallery/',
    template_name = "Board_List.html",
    create_url = 'bbs:gallery_create',
    read_url='bbs:gallery_read',
    title="갤러리",
)

galleryCreate = BoardCreateView.as_view(
    model = models.Gallery,
    form_class = forms.GalleryCreationForm,
    template_name='Board_Create.html',
    title ="갤러리 게시글 작성"
)
galleryRead = BoardReadView.as_view(
    model = models.Gallery,
    comment_model = models.GalleryComment,
    comment_Form_class = forms.GalleryCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="갤러리",
    like_url='bbs:gallery_like',
    dislike_url='bbs:gallery_dislike',
    update_url='bbs:gallery_update',
    destroy_url= 'bbs:gallery_destroy',
    comment_url= 'bbs:gallery_comment',
)
galleryUpdate = BoardUpdateView.as_view(
    model = models.Gallery,
    form_class= forms.GalleryCreationForm,
    success_url = '/gallery/',
    template_name='Board_Create.html',
    title ="갤러리 수정",
)

galleryDestroy = BoardDestroyView.as_view(
    
)

galleryLike = LikeView.as_view(
    model = models.Gallery
)

galleryDisLike = DisLikeView.as_view(
    model = models.Gallery
)

galleryComment = CommentView.as_view(
    model = models.Gallery,
    form_class = forms.GalleryCommentForm,
    template_name="Comment.html",
)

##################################################################################
#정보/꿀팁

honeyTipList = BoardListView.as_view(
    model= models.HoneyTip,
    login_form = LoginForm ,
    success_url ='/honeytip/',
    template_name = "Board_List.html",
    create_url = 'bbs:honeytip_create',
    read_url='bbs:honeytip_read',
    title="꿀팁 게시판",
)

honeyTipCreate = BoardCreateView.as_view(
    model = models.HoneyTip,
    form_class = forms.HoneyTipCreationForm,
    template_name='Board_Create.html',
    title ="꿀팁 작성"
)
honeyTipRead = BoardReadView.as_view(
    model = models.HoneyTip,
    comment_model = models.HoneyTipComment,
    comment_Form_class = forms.HoneyTipCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="꿀팁",
    like_url='bbs:honeytip_like',
    dislike_url='bbs:honeytip_dislike',
    update_url='bbs:honeytip_update',
    destroy_url= 'bbs:honeytip_destroy',
    comment_url= 'bbs:honeytip_comment',
)
honeyTipUpdate = BoardUpdateView.as_view(
    model = models.HoneyTip,
    form_class= forms.HoneyTipCreationForm,
    success_url = '/honeytip/',
    template_name='Board_Create.html',
    title ="꿀팁 수정",
)

honeyTipDestroy = BoardDestroyView.as_view(
    
)

honeyTipLike = LikeView.as_view(
    model = models.HoneyTip
)

honeyTipDisLike = DisLikeView.as_view(
    model = models.HoneyTip
)

honeyTipComment = CommentView.as_view(
    model = models.HoneyTip,
    form_class = forms.HoneyTipCommentForm,
    template_name="Comment.html",
)

####################################################################
#포럼
forumlist = ForumListView.as_view(
    form_class = LoginForm ,
    success_url = '/forum/',
    template_name='Forum_List.html',
    title ="코인별 포럼"
)
#####################################################################
# 비트코인 포럼
forumBitCoinList = BoardListView.as_view(
    model= models.ForumBitCoin,
    login_form = LoginForm ,
    success_url ='/forum/bitcoin/',
    template_name = "Board_List.html",
    create_url = 'bbs:forumbitcoin_create',
    read_url='bbs:forumbitcoin_read',
    title="비트코인 포럼",
)

forumBitCoinCreate = BoardCreateView.as_view(
    model = models.ForumBitCoin,
    form_class = forms.ForumBitCoinCreationForm,
    template_name='Board_Create.html',
    title="비트코인 포럼",
)

forumBitCoinRead = BoardReadView.as_view(
    model = models.ForumBitCoin,
    comment_model = models.ForumBitCoinComment,
    comment_Form_class = forms.ForumBitCoinCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title="비트코인 포럼",
    like_url='bbs:forumbitcoin_like',
    dislike_url='bbs:forumbitcoin_dislike',
    update_url='bbs:forumbitcoin_update',
    destroy_url= 'bbs:forumbitcoin_destroy',
    comment_url= 'bbs:forumbitcoin_comment',
)

forumBitCoinUpdate = BoardUpdateView.as_view(
    model = models.ForumBitCoin,
    form_class= forms.ForumBitCoinCreationForm,
    success_url = '/forum/bitcoin/',
    template_name='Board_Create.html',
    title="비트코인 포럼",
)
forumBitCoinDestroy = BoardDestroyView.as_view(
    
)
forumBitCoinLike = LikeView.as_view(
    model = models.ForumBitCoin
)

forumBitCoinDisLike = DisLikeView.as_view(
    model = models.ForumBitCoin
)

forumBitCoinComment = CommentView.as_view(
    model = models.ForumBitCoin,
    form_class = forms.ForumBitCoinCommentForm,
    template_name="Comment.html",
)

#학회 게시판
societylist = ForumListView.as_view(
    form_class = LoginForm ,
    success_url = '/forum/',
    template_name='Society_List.html',
    title ="학회게시판"
)

#제휴 게시판

#제휴 문의 게시판

