from django.shortcuts import render
from account.forms import LoginForm

from coinsense import bbs
from . import models
from . import forms

#갤러리
marketBoardList = bbs.BoardListView.as_view(
    model= models.MarketBoard,
    login_form = LoginForm ,
    success_url ='/MarketBoard/',
    template_name = "Board_List.html",
    create_url = 'bk:market_create',
    read_url='bk:market_read',
    title="판매 게시판",
    permission = 'BK',
)

marketBoardCreate = bbs.BoardCreateView.as_view(
    model = models.MarketBoard,
    form_class = forms.MarketBoardCreationForm,
    template_name='Board_Create.html',
    title ="판매게시글 작성",
    pass_condition="BK",
)
marketBoardRead = bbs.BoardReadView.as_view(
    model = models.MarketBoard,
    comment_model = models.MarketBoardComment,
    comment_Form_class = forms.MarketBoardCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="판매게시판",
    like_url='bk:market_like',
    dislike_url='bk:market_dislike',
    update_url='bk:market_update',
    destroy_url= 'bk:market_destroy',
    comment_url= 'bk:market_comment',
)

marketBoardUpdate = bbs.BoardUpdateView.as_view(
    model = models.MarketBoard,
    form_class= forms.MarketBoardCreationForm,
    template_name='Board_Create.html',
    title ="갤러리 수정",
)

marketBoardDestroy = bbs.BoardDestroyView.as_view(
    
)

marketBoardLike = bbs.LikeView.as_view(
    model = models.MarketBoard
)

marketBoardDisLike = bbs.DisLikeView.as_view(
    model = models.MarketBoard
)

marketBoardComment = bbs.CommentView.as_view(
    model = models.MarketBoard,
    form_class = forms.MarketBoardCommentForm,
    template_name="Comment.html",
)

#이벤트
eventList = bbs.BoardListView.as_view(
    model= models.Event,
    login_form = LoginForm ,
    success_url ='/event/',
    template_name = "Board_List.html",
    create_url = 'bk:event_create',
    read_url='bk:event_read',
    title="판매 게시판",
    permission = 'BK',
)

eventCreate = bbs.BoardCreateView.as_view(
    model = models.Event,
    form_class = forms.EventCreationForm,
    template_name='Board_Create.html',
    title ="판매게시글 작성",
    pass_condition="BK",
)
eventRead = bbs.BoardReadView.as_view(
    model = models.Event,
    comment_model = models.EventComment,
    comment_Form_class = forms.EventCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="판매게시판",
    like_url='bk:event_like',
    dislike_url='bk:event_dislike',
    update_url='bk:event_update',
    destroy_url= 'bk:event_destroy',
    comment_url= 'bk:event_comment',
)

eventUpdate = bbs.BoardUpdateView.as_view(
    model = models.Event,
    form_class= forms.EventCreationForm,
    template_name='Board_Create.html',
    title ="갤러리 수정",
)

eventDestroy = bbs.BoardDestroyView.as_view(
    
)

eventLike = bbs.LikeView.as_view(
    model = models.Event
)

eventDisLike = bbs.DisLikeView.as_view(
    model = models.Event
)

eventComment = bbs.CommentView.as_view(
    model = models.Event,
    form_class = forms.EventCommentForm,
    template_name="Comment.html",
)