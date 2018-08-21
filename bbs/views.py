from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test

#App 
from coinsense.bbs import BoardCreateView, BoardListView, BoardReadView, BoardUpdateView, BoardDestroyView, LikeView, DisLikeView, CommentView, ForumListView
from .models import FreeBoard, FreeBoardComment

from bbs.forms import FreeBoardCreationForm, FreeBoardCommentForm, NormalAnalysisCreationForm, NormalAnalysisCommentForm
from account.forms import LoginForm

# 게시판 필요 View 
# BoardCreateview, BoardListView, BoardReadView, BoardUpdateView, 
# BoardDestroyView, LikeView, DisLikeView, CommentView 총 8개

#자유게시판
freeList = BoardListView.as_view(
    model = FreeBoard,
    login_form = LoginForm ,
    success_url = '/free/',
    template_name='Board_List.html',
    create_url = 'bbs:free_create',
    read_url='bbs:free_read',
    title ="자유게시판"
)

freeCreate = BoardCreateView.as_view(
    model = FreeBoard,
    form_class = FreeBoardCreationForm,
    template_name='Board_Create.html',
    title ="자유게시판 게시글 작성"
)

freeRead = BoardReadView.as_view(
    model = FreeBoard,
    comment_model = FreeBoardComment,
    comment_Form_class = FreeBoardCommentForm,
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
    model = FreeBoard,
    form_class= FreeBoardCreationForm,
    success_url = '/free/',
    template_name='Board_Create.html',
    title ="자유게시판 게시글 수정"
)

freeDestroy = BoardDestroyView.as_view()

freeLike = LikeView.as_view(
    model = FreeBoard
)

freeDisLike = DisLikeView.as_view(
    model = FreeBoard
)

freeComment = CommentView.as_view(
    model = FreeBoard,
    form_class = FreeBoardCommentForm,
    template_name="Comment.html",
)

#일반시황분석
from .models import NormalAnalysis, NormalAnalysisComment
normalAnalysisList = BoardListView.as_view(
    model= NormalAnalysis,
    login_form = LoginForm ,
    success_url ='/analysis/',
    template_name = "Board_List.html",
    create_url = 'bbs:analysis_create',
    read_url='bbs:analysis_read',
    title="시황분석공유",
)

normalAnalysisCreate = BoardCreateView.as_view(
    model = NormalAnalysis,
    form_class = NormalAnalysisCreationForm,
    template_name='Board_Create.html',
    title ="시황분석 게시글 작성"
)
normalAnalysisRead = BoardReadView.as_view(
    model = NormalAnalysis,
    comment_model = NormalAnalysisComment,
    comment_Form_class = NormalAnalysisCommentForm,
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
    model = NormalAnalysis,
    form_class= NormalAnalysisCreationForm,
    success_url = '/free/',
    template_name='Board_Create.html',
    title ="시황분석공유 게시글 수정",
)

normalAnalysisDestroy = BoardDestroyView.as_view(
    
)

normalAnalysisLike = LikeView.as_view(
    model = NormalAnalysis
)

normalAnalysisDisLike = DisLikeView.as_view(
    model = NormalAnalysis
)

normalAnalysisComment = CommentView.as_view(
    model = NormalAnalysis,
    form_class = NormalAnalysisCommentForm,
    template_name="Comment.html",
)


#갤러리
galleryList = BoardListView.as_view(
    model= NormalAnalysis,
    login_form = LoginForm ,
    success_url ='/analysis/',
    template_name = "Board_List.html",
    create_url = 'bbs:analysis_create',
    title="시황분석공유",
)
galleryCreate = BoardCreateView.as_view(

)
galleryRead = BoardReadView.as_view(

)
galleryUpdate = BoardUpdateView.as_view(

)

galleryDestroy = BoardDestroyView.as_view(

)

galleryLike = LikeView.as_view(

)

galleryDisLike = DisLikeView.as_view(

)

galleryComment = CommentView.as_view(

)
##################################################################################
#정보/꿀팁
from .models import HoneyTip,HoneyTipComment
from .forms import HoneyTipCommentForm, HoneyTipCreationForm

honeyTipList = BoardListView.as_view(
    model= HoneyTip,
    login_form = LoginForm ,
    success_url ='/honeytip/',
    template_name = "Board_List.html",
    create_url = 'bbs:honeytip_create',
    read_url='bbs:honeytip_read',
    title="꿀팁 게시판",
)

honeyTipCreate = BoardCreateView.as_view(
    model = HoneyTip,
    form_class = HoneyTipCreationForm,
    template_name='Board_Create.html',
    title ="꿀팁 작성"
)
honeyTipRead = BoardReadView.as_view(
    model = HoneyTip,
    comment_model = HoneyTipComment,
    comment_Form_class = HoneyTipCommentForm,
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
    model = HoneyTip,
    form_class= HoneyTipCreationForm,
    success_url = '/honeytip/',
    template_name='Board_Create.html',
    title ="꿀팁 수정",
)

honeyTipDestroy = BoardDestroyView.as_view(
    
)

honeyTipLike = LikeView.as_view(
    model = HoneyTip
)

honeyTipDisLike = DisLikeView.as_view(
    model = HoneyTip
)

honeyTipComment = CommentView.as_view(
    model = HoneyTip,
    form_class = HoneyTipCommentForm,
    template_name="Comment.html",
)

####################################################################
#포럼
forumlist = ForumListView.as_view(
    #model = ,
    form_class = LoginForm ,
    success_url = '/forum/',
    template_name='Forum_List.html',
    title ="코인별 포럼"
)

forumList = BoardListView.as_view(

)
forumCreate = BoardCreateView.as_view(

)
forumRead = BoardReadView.as_view(

)
forumUpdate = BoardUpdateView.as_view(

)

forumDestroy = BoardDestroyView.as_view(

)

forumLike = LikeView.as_view(

)

forumDisLike = DisLikeView.as_view(

)

forumComment = CommentView.as_view(

)

#학회 게시판
societylist = ForumListView.as_view(
    #model = ,
    form_class = LoginForm ,
    success_url = '/forum/',
    template_name='Society_List.html',
    title ="학회게시판"
)

#제휴 게시판

#제휴 문의 게시판

