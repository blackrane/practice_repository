#django import
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
import json

#App import
from account.forms import LoginForm
from account.views import login_func

class BoardListView(View):
    model = None
    login_form = None
    success_url= None
    template_name = None
    create_url = ''
    read_url=''
    context={}
    title = None
    permission = None

    def get_permission(self):
        if self.permission is None:
            return True
        if self.request.user.code == self.permission:
            return True
        return False

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name

    #get 요청일때
    def get(self, *args, **kwargs):
        self.context['post_list'] = self.model.objects.all()
        self.context['form'] = self.login_form()
        self.context['boardtitle'] = self.title
        self.context['url']= reverse(self.create_url)
        self.context['read_url'] = self.read_url
        self.context['permission'] = self.get_permission()
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        self.context['post_list'] = self.model.objects.all()
        self.context['error'] = login_func(self.request)
        self.context['boardtitle'] = self.title
        self.context['permission'] = self.get_permission()
        return render(self.request, self.get_template_name(), self.context)

class BoardCreateView(View):
    model = None
    form_class = None
    template_name = None
    context={}
    title = None

    @method_decorator(login_required(login_url='/free/'))
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
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            return redirect(post.get_absolute_url())
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

        #접근주소 가변처리
        self.context['like_url'] =  reverse(self.like_url)
        self.context['dislike_url'] = reverse(self.dislike_url)
        self.context['update_url'] = self.update_url
        self.context['destroy_url'] = self.destroy_url
        self.context['comment_url'] = reverse(self.comment_url)
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        self.context['post'] = get_object_or_404(self.model, id= self.kwargs['pk'])
        self.context['error'] = login_func(self.request)
        self.context['boardtitle'] = self.title
        return render(self.request, self.get_template_name(), self.context)

#게시글 수정 뷰
class BoardUpdateView(View):
    model = None
    form_class = None
    success_url= None
    template_name = None
    title = None
    context={}
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
        return render(self.request, self.get_template_name(), self.context)
    
    #post 요청일때
    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            return redirect(post.get_absolute_url())
        return render(self.request, self.get_template_name(), self.get_context_data(form=form))

class BoardDestroyView(View):
    pass


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

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name
    
    #get 요청일때
    def get(self, *args, **kwargs):
        #self.context['post_list'] = self.model.objects.all()
        self.context['form'] = self.form_class()
        self.context['boardtitle'] = self.title
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        #self.context['post_list'] = self.model.objects.all()
        self.context['error'] = login_func(self.request)
        self.context['boardtitle'] = self.title
        return render(self.request, self.get_template_name(), self.context)
