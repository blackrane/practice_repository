from django.db import models
from django.contrib.auth import get_user_model
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
from django.urls import reverse

# Create your models here.
class FreeBoard(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='like_user_set',
                                           through='Like') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='dislike_user_set',
                                           through='DisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    def get_code(self):
        return 'Z0'

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:free_read', args=[self.id])

class FreeBoardComment(models.Model):
    post = models.ForeignKey(FreeBoard, verbose_name="Free Board", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(FreeBoard, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(FreeBoard, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

###############################################################################################################################
#  시황분석 모델들
class NormalAnalysis(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='NAlike_user_set',
                                           through='NormalAnalysisLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='NAdislike_user_set',
                                           through='NormalAnalysisDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:analysis_read', args=[self.id])

class NormalAnalysisComment(models.Model):
    post = models.ForeignKey(NormalAnalysis, verbose_name="Free Board", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class NormalAnalysisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(NormalAnalysis, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NormalAnalysisDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(NormalAnalysis, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


###############################################################################################################################
#  꿀팁(Honey-Tip) 모델들
class HoneyTip(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='HTlike_user_set',
                                           through='HoneyTipLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='HTdislike_user_set',
                                           through='HoneyTipDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:honeytip_read', args=[self.id])

class HoneyTipComment(models.Model):
    post = models.ForeignKey(HoneyTip, verbose_name="HoneyTip Comment", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class HoneyTipLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(HoneyTip, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HoneyTipDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(HoneyTip, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



###############################################################################################################################
#  ForumBitCoin
class ForumBitCoin(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='FBClike_user_set',
                                           through='ForumBitCoinLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='FBCdislike_user_set',
                                           through='ForumBitCoinDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:forumbitcoin_read', args=[self.id])

class ForumBitCoinComment(models.Model):
    post = models.ForeignKey(ForumBitCoin, verbose_name="HoneyTip Comment", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class ForumBitCoinLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(ForumBitCoin, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ForumBitCoinDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(ForumBitCoin, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

<<<<<<< HEAD
#######################################################################################################################################
#호재
class Favorable(models.Model):
    title = models.CharField(verbose_name="title",max_length=20)
    content = models.CharField(verbose_name="content",max_length=20)
    photo = models.ImageField(blank=True)
    date = models.DateTimeField()
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Favorable_like_user_set',
                                           through='Favorable_Like') # post.like_set 으로 접근 가능
    @property
    def like_count(self):
        return self.like_user_set.count()

    def __str__(self):
        return self.title

class Favorable_Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Favorable, on_delete=models.CASCADE ,related_name='like_set')
=======

###############################################################################################################################
#  ForumBitCoin
class Gallery(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Glike_user_set',
                                           through='galleryLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='GCdislike_user_set',
                                           through='galleryDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:gallery_read', args=[self.id])

class GalleryComment(models.Model):
    post = models.ForeignKey(Gallery, verbose_name="HoneyTip Comment", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class GalleryLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Gallery, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GalleryDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='dislike_set')
>>>>>>> 5a4324f35e5a06a5871a83862a28af71e397792a
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)