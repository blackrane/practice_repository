from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test

#App 
from coinsense.bbs import BoardCreateview, BoardListView, BoardReadView, BoardUpdateView, BoardDestroyView, LikeView, DisLikeView, CommentView, ForumListView
from .models import FreeBoard, FreeBoardComment
from bbs.forms import FreeBoardCreationForm, FreeBoardCommentForm
from account.forms import LoginForm

# Create your views here.
freeList = BoardListView.as_view(
    model = FreeBoard,
    form_class = LoginForm ,
    success_url = '/free/',
    template_name='Board_List.html',
    title ="자유게시판"
)

freeCreate = BoardCreateview.as_view(
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
    title ="자유게시판"
)

freeUpdate = BoardUpdateView.as_view(
    model = FreeBoard,
    form_class= FreeBoardCreationForm,
    success_url = '/free/',
    template_name='Board_Create.html',
    title ="자유게시판 게시글 수정"
)

freeDetail = BoardDestroyView.as_view()

freeLike = LikeView.as_view(
    model=FreeBoard
)

freeDisLike = DisLikeView.as_view(
    model=FreeBoard
)

freeComment = CommentView.as_view(
    model = FreeBoard,
    form_class = FreeBoardCommentForm,
    template_name="Comment.html",
)

forumlist = ForumListView.as_view(
    #model = ,
    form_class = LoginForm ,
    success_url = '/forum/',
    template_name='Forum_List.html',
    title ="코인별 포럼"
)

societylist = ForumListView.as_view(
    #model = ,
    form_class = LoginForm ,
    success_url = '/forum/',
    template_name='Society_List.html',
    title ="학회게시판"
)