from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields

from django import forms
from .models import FreeBoard, FreeBoardComment , NormalAnalysis, NormalAnalysisComment, HoneyTip, HoneyTipComment

class FreeBoardCreationForm(forms.ModelForm):
    class Meta:
        model = FreeBoard
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class FreeBoardCommentForm(forms.ModelForm):
    class Meta:
        model = FreeBoardComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }
################################################################################################################################
# 시황분석폼
class NormalAnalysisCreationForm(forms.ModelForm):
    class Meta:
        model = NormalAnalysis
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class NormalAnalysisCommentForm(forms.ModelForm):
    class Meta:
        model = NormalAnalysisComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

################################################################################################################################
# 꿀팁 폼

class HoneyTipCreationForm(forms.ModelForm):
    class Meta:
        model = HoneyTip
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class HoneyTipCommentForm(forms.ModelForm):
    class Meta:
        model = HoneyTipComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

################################################################################################################################
# 시황분석폼

################################################################################################################################
# 시황분석폼

################################################################################################################################
# 시황분석폼

################################################################################################################################
# 시황분석폼

################################################################################################################################
# 시황분석폼

################################################################################################################################
# 시황분석폼