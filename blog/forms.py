from django import forms

from mdeditor.fields import MDTextFormField
from .models import *

'''
class MDEditorForm (forms.Form):
    name = forms.CharField ()
    content = MDTextFormField ()


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'tag', 'content', 'language')

        labels = {
            'title': 'Title',
            'tag': 'Tags',
            'content': ' ',
            'language': 'Language',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'input'}),
            'intro': forms.TextInput(attrs={'class':'input textarea has-fixed-size', 'rows':'3'}),
            'body': forms.TextInput(attrs={'class':'input textarea has-fixed-size', 'rows':'10'}),
            'link': forms.TextInput(attrs={'class':'input'})
        }'''

class MDEditorModleForm (forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'