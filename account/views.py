#django
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, get_user_model, authenticate, update_session_auth_hash
from django.utils import timezone
from bbs import models
#app
from .forms import LoginForm, UserCreationForm
from bbs.models import FreeBoard

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

def index(request,context={}):
    if request.method == "POST":        
        form = LoginForm(request.POST)
        context['error']= login_func(request)
    form = LoginForm()
    context['form'] = form
    context['post_list'] = FreeBoard.objects.all().order_by('-id')
    context['notice'] = models.Notice.objects.all()
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
    return render(request, 'account/my_page.html',context)

def myWrite(request):
    if request.user.code == 'Z0':
        a = request.user.freeboard_set
    print(a)
    a=0
    context={'a':a}
    context['notice'] = models.Notice.objects.all()
    return render(request, 'account/my_page.html',context)

def myComments(request):
    context={}
    context['notice'] = models.Notice.objects.all()
    return render(request, 'account/my_page.html',context)