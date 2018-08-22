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

#코인분석 
coinAnalysisList = bbs.BoardListView.as_view(
    model= models.CoinAnalysis,
    login_form = LoginForm ,
    success_url ='/coinanalysis/',
    template_name = "Board_List.html",
    create_url = 'bk:coinanalysis_create',
    read_url='bk:coinanalysis_read',
    title="코인분석 게시판",
    permission = 'BK',
)

coinAnalysisCreate = bbs.BoardCreateView.as_view(
    model = models.CoinAnalysis,
    form_class = forms.CoinAnalysisCreationForm,
    template_name='Board_Create.html',
    title ="코인분석 작성",
    pass_condition="BK",
)
coinAnalysisRead = bbs.BoardReadView.as_view(
    model = models.CoinAnalysis,
    comment_model = models.CoinAnalysisComment,
    comment_Form_class = forms.CoinAnalysisCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="코인분석",
    like_url='bk:coinanalysis_like',
    dislike_url='bk:coinanalysis_dislike',
    update_url='bk:coinanalysis_update',
    destroy_url= 'bk:coinanalysis_destroy',
    comment_url= 'bk:coinanalysis_comment',
)

coinAnalysisUpdate = bbs.BoardUpdateView.as_view(
    model = models.CoinAnalysis,
    form_class= forms.CoinAnalysisCreationForm,
    template_name='Board_Create.html',
    title ="코인분석 수정",
)

coinAnalysisDestroy = bbs.BoardDestroyView.as_view(
    
)

coinAnalysisLike = bbs.LikeView.as_view(
    model = models.CoinAnalysis
)

coinAnalysisDisLike = bbs.DisLikeView.as_view(
    model = models.CoinAnalysis
)

coinAnalysisComment = bbs.CommentView.as_view(
    model = models.CoinAnalysis,
    form_class = forms.CoinAnalysisCommentForm,
    template_name="Comment.html",
)

#시황분석
analysisList = bbs.BoardListView.as_view(
    model= models.Analysis,
    login_form = LoginForm ,
    success_url ='/analysis/',
    template_name = "Board_List.html",
    create_url = 'bk:analysis_create',
    read_url='bk:analysis_read',
    title="시황분석 게시판",
    permission = 'BK',
)

analysisCreate = bbs.BoardCreateView.as_view(
    model = models.Analysis,
    form_class = forms.AnalysisCreationForm,
    template_name='Board_Create.html',
    title ="시황분석 작성",
    pass_condition="BK",
)
analysisRead = bbs.BoardReadView.as_view(
    model = models.Analysis,
    comment_model = models.AnalysisComment,
    comment_Form_class = forms.AnalysisCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="시황분석",
    like_url='bk:analysis_like',
    dislike_url='bk:analysis_dislike',
    update_url='bk:analysis_update',
    destroy_url= 'bk:analysis_destroy',
    comment_url= 'bk:analysis_comment',
)

analysisUpdate = bbs.BoardUpdateView.as_view(
    model = models.Analysis,
    form_class= forms.AnalysisCreationForm,
    template_name='Board_Create.html',
    title ="시황분석 수정",
)

analysisDestroy = bbs.BoardDestroyView.as_view(
    
)

analysisLike = bbs.LikeView.as_view(
    model = models.Analysis
)

analysisDisLike = bbs.DisLikeView.as_view(
    model = models.Analysis
)

analysisComment = bbs.CommentView.as_view(
    model = models.Analysis,
    form_class = forms.AnalysisCommentForm,
    template_name="Comment.html",
)

#비디오컨텐츠
videoList = bbs.BoardListView.as_view(
    model= models.Video,
    login_form = LoginForm ,
    success_url ='/Video/',
    template_name = "Board_List.html",
    create_url = 'bk:video_create',
    read_url='bk:video_read',
    title="비디오컨텐츠 게시판",
    permission = 'BK',
)

videoCreate = bbs.BoardCreateView.as_view(
    model = models.Video,
    form_class = forms.VideoCreationForm,
    template_name='Board_Create.html',
    title ="비디오컨텐츠 작성",
    pass_condition="BK",
)
videoRead = bbs.BoardReadView.as_view(
    model = models.Video,
    comment_model = models.VideoComment,
    comment_Form_class = forms.VideoCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="비디오컨텐츠",
    like_url='bk:video_like',
    dislike_url='bk:video_dislike',
    update_url='bk:video_update',
    destroy_url= 'bk:video_destroy',
    comment_url= 'bk:video_comment',
)

videoUpdate = bbs.BoardUpdateView.as_view(
    model = models.Video,
    form_class= forms.VideoCreationForm,
    template_name='Board_Create.html',
    title ="비디오컨텐츠 수정",
)

videoDestroy = bbs.BoardDestroyView.as_view(
    
)

videoLike = bbs.LikeView.as_view(
    model = models.Video
)

videoDisLike = bbs.DisLikeView.as_view(
    model = models.Video
)

videoComment = bbs.CommentView.as_view(
    model = models.Video,
    form_class = forms.VideoCommentForm,
    template_name="Comment.html",
)