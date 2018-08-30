#django
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, get_user_model, authenticate, update_session_auth_hash
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger , EmptyPage

#app
from bbs import models
from bk_bbs import models as bk_models
from .forms import LoginForm, UserCreationForm
from bbs.models import FreeBoard

#Python 
from itertools import chain
from operator import attrgetter

def get_pagination(model_list, bundle, page):
        #페이지 네이션
    paginator = Paginator(model_list, bundle) #15개씩 묶어 페이지 생성 선언

    try:
        paginator = paginator.page(page)
    except PageNotAnInteger:
        paginator = paginator.page(1)
    except EmptyPage:
        paginator = paginator.page(paginator.num_pages)

    return paginator

def get_my_post(pk):
    board = models.FreeBoard.objects.filter(author=pk)          #자유게시판
    na = models.NormalAnalysis.objects.filter(author=pk)        #시황분석
    ht = models.HoneyTip.objects.filter(author=pk)              #꿀팁
    fb = models.ForumBitCoin.objects.filter(author=pk)          #포럼 비트코인
    gb = models.Gallery.objects.filter(author=pk)               #갤러리
    uc = models.UserColumn.objects.filter(author=pk)            #유저칼럼
    
    mk = bk_models.MarketBoard.objects.filter(author=pk)        #판매게시판
    ev = bk_models.Event.objects.filter(author=pk)              #이벤트게시판
    ca = bk_models.CoinAnalysis.objects.filter(author=pk)       #bk코인분석
    ab = bk_models.Analysis.objects.filter(author=pk)           #bk시황분석
    vb = bk_models.Video.objects.filter(author=pk)              #동영상게시판
    nb = bk_models.News.objects.filter(author=pk)               #뉴스게시판
    ic = bk_models.ICORating.objects.filter(author=pk)          #ico게시판

    #chain함수로 모든 쿼리셋을 하나로 합치면서 views 내림차순으로 정렬하여 리턴
    all_board = sorted(chain(board, na,ht,fb,gb,uc,mk,ev,ca,ab,vb,nb,ic), key=attrgetter('created_at'), reverse=True)
    return all_board

def get_my_comment(pk):
    na = models.NormalAnalysisComment.objects.filter(author=pk)
    ht = models.HoneyTipComment.objects.filter(author=pk)
    fb = models.ForumBitCoinComment.objects.filter(author=pk)
    gb = models.GalleryComment.objects.filter(author=pk)
    uc= models.UserColumnComment.objects.filter(author=pk)
    su = models.SeoulUnvComment.objects.filter(author=pk)
    board =models.FreeBoardComment.objects.filter(author=pk)

    icbk = bk_models.ICORatingBkComment.objects.filter(author=pk)
    nb =bk_models.NewsComment.objects.filter(author=pk)
    mb = bk_models.MarketBoardComment.objects.filter(author=pk)
    eb = bk_models.EventComment.objects.filter(author=pk)
    ca = bk_models.CoinAnalysisComment.objects.filter(author=pk)
    ab = bk_models.AnalysisComment.objects.filter(author=pk)
    vb = bk_models.VideoComment.objects.filter(author=pk)
    ic = bk_models.ICORatingComment.objects.filter(author=pk)
    all_com = sorted(chain(board, na,ht,fb,gb,uc,su,mb,ca,ab,vb,nb,ic,icbk,eb), key=attrgetter('created_date'), reverse=True)
    return all_com

def login_func(request):
    username = request.POST['username']
    password = request.POST['password']
    user= authenticate(request, username=username,password=password)
    if user is not None:
        login(request, user)
        user = get_user_model().objects.get(pk=request.user.id)
        user.last_login=timezone.now

        return ''
    else:
        return '아이디/비밀번호가 틀렸습니다.'

from coinsense import bbs
def index(request,context={}):
    if request.method == "POST":        
        form = LoginForm(request.POST)
        context['error']= login_func(request)
    form = LoginForm()
    context['form'] = form
    context['post_list'] = FreeBoard.objects.all().order_by('-id')
    context['notice'] = models.Notice.objects.all()
    context['ranking_list']= bbs.get_ranking()
    return render(request, 'account/index.html', context)

def signup(request,context={}):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            login_func(request)
            print("로그인완료?")
            return redirect('account:index')
        else:
            print("로그인실패?")
            context['form'] = form

    if request.method =="GET":
        form = UserCreationForm()
        context['form']=form

    return render(request, 'account/signup.html', context)

def myPage(request):
    context={}
    context['notice'] = models.Notice.objects.all()
    context['ranking_list']= bbs.get_ranking()
    return render(request, 'account/my_page.html',context)

#내가쓴글
def myWrite(request):
    post_list = get_my_post(request.user.pk)
    page = request.GET.get('page', 1)
    post_list = get_pagination(post_list, 5 , page)
    context={'post_list':post_list}
    return render(request, 'account/my_page_mypost.html',context)

#내가 작성한 댓글
def myComments(request):
    comment_list = get_my_comment(request.user.pk)
    page = request.GET.get('page',1 )
    comment_list = get_pagination(comment_list, 5, page)
    context={'comment_list': comment_list}
    return render(request, 'account/my_page_mycomment.html',context)

#마이페이지 ajax
def myPageAjax(request):
    context={}
    return render(request, 'account/my_page_ajax.html',context)



#글저장함
def MyPostSave(request):
    context={}
    return render(request, 'account/my_page_postsave.html', context)

#쪽지함
def myMessage(request):
    context={}
    return render(request, 'account/my_page_message.html', context)

#알림목록
def myNotice(request):
    context={}
    return render(request, 'account/my_page_Notice.html', context)
