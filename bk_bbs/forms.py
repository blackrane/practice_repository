from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields

from django import forms
from . import models

class MarketBoardCreationForm(forms.ModelForm):
    class Meta:
        model = models.MarketBoard
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class MarketBoardCommentForm(forms.ModelForm):
    class Meta:
        model = models.MarketBoardComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }