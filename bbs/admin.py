from django.contrib import admin
from .models import FreeBoard, FreeBoardComment, Favorable
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


#자유게시판 게시판
@admin.register(FreeBoard)
class FreeBoardAdmin(admin.ModelAdmin):
    summernote_fields = ('author','title','views','content')

admin.site.register(FreeBoardComment,FreeBoardAdmin)

@admin.register(Favorable)
class FreeBoardAdmin(admin.ModelAdmin):
    summernote_fields = ('title','content','photo','date')