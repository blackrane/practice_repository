#django import
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger , EmptyPage
from django.db.models import Q
import json
from bbs import models
from bk_bbs import models as bk_models
#App import
from account.forms import LoginForm
from account.views import login_func

#합치기 위해
from itertools import chain
from operator import attrgetter

#모든 게시글 합침
def get_board():
    board = models.FreeBoard.objects.all()          #자유게시판
    na = models.NormalAnalysis.objects.all()        #시황분석
    ht = models.HoneyTip.objects.all()              #꿀팁
    fb = models.ForumBitCoin.objects.all()          #포럼 비트코인
    gb = models.Gallery.objects.all()               #갤러리
    uc = models.UserColumn.objects.all()            #유저칼럼
    
    mk = bk_models.MarketBoard.objects.all()        #판매게시판
    ev = bk_models.Event.objects.all()              #이벤트게시판
    ca = bk_models.CoinAnalysis.objects.all()       #bk코인분석
    ab = bk_models.Analysis.objects.all()           #bk시황분석
    vb = bk_models.Video.objects.all()              #동영상게시판
    nb = bk_models.News.objects.all()               #뉴스게시판
    ic = bk_models.ICORating.objects.all()          #ico게시판

    all_board = sorted(chain(board, na,ht,fb,gb,uc,mk,ev,ca,ab,vb,nb,ic), key=attrgetter('views'), reverse=True)
    return all_board

#조회수 5위 게시글
def get_ranking():
    board = get_board()
    ranking = board[:5]
    return ranking

class BoardListView(UserPassesTestMixin,View):
    model = None
    login_form = None
    success_url= None
    template_name = None
    create_url = ''
    read_url=''
    context={}
    title = None
    permission = None
    notice_model = models.Notice
    access_permission=None
    approval_url= None

    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    def get_permission(self):
        #아무 권한 부여 안하면 모두에게 개방
        if self.permission is None:
            return True
        #BK이면 모두 접근할수 있음
        if self.request.user.code =="BK":
            return True
        #그외 권한설정
        if self.request.user.code == self.permission:
            return True
        return False

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name

    def context_init(self):
        self.context['post_list'] = self.model.objects.all().order_by('id')
        self.context['form'] = self.login_form()
        self.context['boardtitle'] = self.title
        self.context['url']= reverse(self.create_url)
        self.context['read_url'] = self.read_url
        self.context['permission'] = self.get_permission()
        self.context['notice'] = self.notice_model.objects.all()
        self.context['ranking_list']= get_ranking()
        if self.approval_url is not None:
            self.context['approval_list']= reverse(self.approval_url)

    def get_serach(self):
        search = self.request.GET.get('search',None) #검색 가져오기
        #검색소스
        if search is not None: #검색이 있다면 
            self.context['post_list'] = self.context['post_list'].filter(
                title__contains=search) #필터해서 적용
    
    def get_pagination(self):
         #페이지 네이션
        paginator = Paginator(self.context['post_list'], 2) #15개씩 묶어 페이지 생성 선언

        page = self.request.GET.get('page',1 )
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)

        self.context['post_list'] = paginator

    #get 요청일때
    def get(self, *args, **kwargs):
        self.context_init()
        self.get_serach()
        self.get_pagination()
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        self.context['post_list'] = self.model.objects.all()
        self.context['error'] = login_func(self.request)
        self.context['boardtitle'] = self.title
        self.context['permission'] = self.get_permission()
        self.context['notice'] = self.notice_model.objects.all()
        return render(self.request, self.get_template_name(), self.context)


class BoardCreateView(UserPassesTestMixin, View):
    model = None
    form_class = None
    template_name = None
    context={}
    title = None
    access_permission = None
    notice_model = models.Notice

    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name

    #get 요청일때
    def get(self, *args, **kwargs):
        self.context['form'] = self.form_class()
        self.context['boardtitle'] = self.title
        self.context['notice'] = self.notice_model.objects.all()
        self.context['ranking_list']= get_ranking()
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            return redirect(post)
        return render(self.request, self.get_template_name(), self.context)

#게시글 디테일 뷰
class BoardReadView(View):
    model = None #게시글 모델
    comment_model = None # 댓글 모델
    form_class = None #로그인 폼
    comment_Form_class = None #댓글 폼
    template_name = None #템플릿 
    context={}
    title = None #게시판이름
    like_url=''
    dislike_url=''
    update_url=''
    destroy_url=''
    comment_url=''
    notice_model = models.Notice

    def get_comment_form(self):
        return self.comment_Form_class

    def get_comment_model(self):
        return self.comment_model.objects.all()
    
    def get_template_name(self):
        return self.template_name

    #get 요청일때
    def get(self, *args, **kwargs):
        pk=self.kwargs['pk']
        post = get_object_or_404(self.model, id=pk )
        
        if not post.author == self.request.user:
            post.views = post.views+1
            post.save()
        
        self.context['post'] = post
        self.context['like_count'] = post.like_count
        self.context['dislike_count'] = post.dislike_count
        self.context['form'] = self.form_class 
        self.context['boardtitle'] = self.title
        self.context['comment_form'] = self.get_comment_form()
        self.context['comments'] = self.get_comment_model().filter(post=post)
        self.context['notice'] = self.notice_model.objects.all()

        #접근주소 가변처리
        self.context['like_url'] =  reverse(self.like_url)
        self.context['dislike_url'] = reverse(self.dislike_url)
        self.context['update_url'] = self.update_url
        self.context['destroy_url'] = self.destroy_url
        self.context['comment_url'] = reverse(self.comment_url)
        self.context['ranking_list']= get_ranking()
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        self.context['post'] = get_object_or_404(self.model, id= self.kwargs['pk'])
        self.context['error'] = login_func(self.request)
        self.context['boardtitle'] = self.title
        self.context['notice'] = self.notice_model.objects.all()
        return render(self.request, self.get_template_name(), self.context)

#게시글 수정 뷰
class BoardUpdateView(UserPassesTestMixin, View):
    model = None
    form_class = None
    success_url= None
    template_name = None
    title = None
    context={}
    notice_model = models.Notice

    #작성자아니면 못들어온다.
    def test_func(self):
        post = get_object_or_404(self.model, id=self.kwargs['pk'])
        if self.request.user == post.author:
            return True
        return False

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.model, id=pk)

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name

    #form 인스턴스 생성
    def get_form(self):
        form_kwargs={
            'instance':self.get_object(),
        }
        if self.request.method == 'POST':
            form_kwargs.update({
                'data':self.request.POST,
                'files': self.request.FILES,
            })
        return self.form_class(**form_kwargs)

    #context에 넘길 변수 설정
    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form']= self.get_form()
        return kwargs

    #get 요청일때
    def get(self, *args, **kwargs):
        form_kwargs={
            'instance':self.get_object(),
        }
        self.context['boardtitle']=self.title
        self.context['form'] = self.form_class(**form_kwargs)
        self.context['notice'] = self.notice_model.objects.all()
        self.context['ranking_list']= get_ranking()
        return render(self.request, self.get_template_name(), self.context)
    
    #post 요청일때
    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            return redirect(post)
        return render(self.request, self.get_template_name(), self.get_context_data(form=form))

class BoardDestroyView(UserPassesTestMixin, View):
    #작성자아니면 못들어온다.
    def test_func(self):
        post = get_object_or_404(self.model, id=self.kwargs['pk'])
        if self.request.user == post.author:
            return True
        return False


#좋아요 ajax
class LikeView(View):
    model = None
    context={}

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    #post 요청일때
    def post(self, *args, **kwargs):
        post = get_object_or_404(self.model, pk=self.request.POST.get('pk', None))

        #check_dislike 릴레이션에 해당 post 필터링 
        #필터링 결과중 첫 row를 가져온다. 못가져오면 None
        check_dislike = post.dislike_set.filter(post=post).first()
        
        # none이아니라면 즉 비추천을 적용했다면
        if check_dislike is not None:
            #아무것도하지말고 리턴
            return HttpResponse(json.dumps('no'))
        #none라면 추천 처리
        post_like, post_like_created = post.like_set.get_or_create(user=self.request.user)
        if not post_like_created:
            post_like.delete()
            message = "like_del"
        else:
            message = "like"

        context = {'like_count': post.like_count,
               'message': message,
               'username': self.request.user.nickname }
        return HttpResponse(json.dumps(context))

#싫어요 ajax
class DisLikeView(View):
    model = None
    context={}

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    #post 요청일때
    def post(self, *args, **kwargs):
        post = get_object_or_404(self.model, pk=self.request.POST.get('pk', None))
        
        #check_like 릴레이션에 해당 post 필터링 
        #필터링 결과중 첫 row를 가져온다. 못가져오면 None
        check_like = post.like_set.filter(post=post).first()
        
        # none이아니라면 즉 추천을 적용했다면
        if check_like is not None:
            #아무것도하지말고 리턴
            return HttpResponse(json.dumps('no'))
        
        post_dislike, post_dislike_created = post.dislike_set.get_or_create(user=self.request.user)
        if not post_dislike_created:
            post_dislike.delete()
            message = "dislike_del"
        else:
            message = "dislike"

        context = {'dislike_count': post.dislike_count,
               'message': message,
               'username': self.request.user.nickname }
        return HttpResponse(json.dumps(context))

#댓글생성
class CommentView(View):
    model = None
    form_class = None
    template_name=None
    context = {}
    

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    #post 요청일때
    def post(self, *args, **kwargs):
        post = get_object_or_404(self.model, pk=self.request.POST.get('pk',None))
        form = self.form_class(self.request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.author = self.request.user
            com.post = post
            com.save()
            self.context['comment'] = com
            return render(self.request, self.template_name, self.context)
        self.context['form']= form
        return render(self.request, self.template_name, self.context)

   

class ForumListView(View):
    model = None
    form_class = None
    success_url= None
    template_name = None
    context = {}
    title = None
    notice_model = models.Notice

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name
    
    #get 요청일때
    def get(self, *args, **kwargs):
        #self.context['post_list'] = self.model.objects.all()
        self.context['form'] = self.form_class()
        self.context['boardtitle'] = self.title
        self.context['notice'] = self.notice_model.objects.all()
        self.context['ranking']= get_ranking()
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        #self.context['post_list'] = self.model.objects.all()
        self.context['error'] = login_func(self.request)
        self.context['boardtitle'] = self.title
        self.context['notice'] = self.notice_model.objects.all()
        
        return render(self.request, self.get_template_name(), self.context)

#승인목록/게시글 조회 ajax View
class SocietyApprovalView(UserPassesTestMixin,View):
    model = None                    #승인 릴레이션
    template_name=None              #템플릿
    context = {}                    #프론트로 넘겨줄 데이터
    access_permission=None          #접근권한
    accept_url = None               #수락 url
    reject_url = None               #거절 url
    read_url = None                 #게시글 조회때 사용하는 읽기 url

    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    def get_pagination(self):
         #페이지 네이션
        paginator = Paginator(self.context['user_list'], 2) #15개씩 묶어 페이지 생성 선언

        page = self.request.GET.get('page',1 )
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)
            
        self.context['user_list'] = paginator

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        if self.read_url is not None:
            self.context['read_url'] = self.read_url

        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url

        return render(self.request, self.template_name, self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        if self.read_url is not None:
            self.context['read_url'] = self.read_url

        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)


#승인 ajax
class SocietyAcceptView(UserPassesTestMixin,View):
    model = None
    template_name=None
    context = {}
    access_permission=None
    accept_url = None
    reject_url = None
    code = 'Z0'
    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    def get_pagination(self):
         #페이지 네이션
        paginator = Paginator(self.context['user_list'], 2) #15개씩 묶어 페이지 생성 선언

        page = self.request.GET.get('page',1 )
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)
            
        self.context['user_list'] = paginator

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        user_list = self.model.objects.all()
        pk = self.request.POST.get('pk',None)
        if pk is not None:
            user= user_list.filter(user=pk).first()
            if user is not None:
                user.user.code= self.code
                user.user.save()
                user.delete()
                

        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)

#승인 거절 ajax
class SocietyRejectView(UserPassesTestMixin,View):
    model = None
    template_name=None
    context = {}
    access_permission=None
    accept_url = None
    reject_url = None
    code = 'Z0'
    
    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    def get_pagination(self):
         #페이지 네이션
        paginator = Paginator(self.context['user_list'], 2) #15개씩 묶어 페이지 생성 선언

        page = self.request.GET.get('page',1 )
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)
            
        self.context['user_list'] = paginator

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        user_list = self.model.objects.all()
        pk = self.request.POST.get('pk',None)
        if pk is not None:
            user= user_list.filter(user=pk).first()
            if user is not None:
                user.delete()

        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)