from django.db import models
from django.contrib.auth import get_user_model
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
from django.urls import reverse



###############################################################################################################################
#  시황분석 모델들
class MarketBoard(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='MBlike_user_set',
                                           through='MarketBoardLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='MBdislike_user_set',
                                           through='MarketBoardDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:marketboard_read', args=[self.id])

class MarketBoardComment(models.Model):
    post = models.ForeignKey(MarketBoard, verbose_name="Free Board", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class MarketBoardLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(MarketBoard, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MarketBoardDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(MarketBoard, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#############################################################################################
# 이벤트 모델
class Event(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Elike_user_set',
                                           through='EventLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Edislike_user_set',
                                           through='EventDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:event_read', args=[self.id])

class EventComment(models.Model):
    post = models.ForeignKey(Event, verbose_name="event", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class EventLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Event, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EventDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)