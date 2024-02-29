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
        }

class MDEditorModleForm (forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__' '''

Lang = (
    ("Fr", "Fr"),
    ("En", "En")
)        

class ArticleForm(forms.ModelForm):
    body = MDTextFormField()

    class Meta:
        model = Article
        fields = ('langue', 'titre', 'theme', 'slug', 'body', 'picture')
        
        labels = {
            'langue': 'Langue',
            'titre': 'Titre',
            'theme': 'Theme',
            'slug': 'Slug',
            'body': 'Corps',
            'picture': 'Image'
        }
        
        widgets = {
            'langue': forms.Select(choices=Lang, attrs={'class':'input'}),
            'titre': forms.TextInput(attrs={'class':'input'}),
            'theme': forms.TextInput(attrs={'class':'input'}),
            'slug': forms.TextInput(attrs={'class':'input'}),
            'body': forms.TextInput(attrs={'class':'input textarea has-fixed-size', 'rows':'10'}),
            'picture': forms.FileInput(attrs={'class':'input'})
        }