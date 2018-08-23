from django.contrib import admin
from .models import FreeBoard, FreeBoardComment, Favorable, Notice, SeoulUnvSocietyRequest
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


#자유게시판 게시판
@admin.register(FreeBoard)
class FreeBoardAdmin(admin.ModelAdmin):
    summernote_fields = ('author','title','views','content')

admin.site.register(FreeBoardComment,FreeBoardAdmin)

@admin.register(Favorable)
class FavorableAdmin(admin.ModelAdmin):
    summernote_fields = ('title','content','photo','date')

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    summernote_fields = ('author','title','summer_field','updated_at','views')

@admin.register(SeoulUnvSocietyRequest)
class SeoulUnvSocietyRequestAdmin(admin.ModelAdmin):
    summernote_fields = ('user','username','unv_number','department')