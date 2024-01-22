from django import forms

from mdeditor.fields import MDTextFormField
from .models import *

class MDEditorForm (forms.Form):
    name = forms.CharField ()
    content = MDTextFormField ()


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'intro', 'body', 'link')

        labels = {
            'title': 'Titre',
            'intro': 'Introduction',
            'body': ' ',
            'link': 'Lien du média',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'input'}),
            'intro': forms.TextInput(attrs={'class':'input textarea has-fixed-size', 'rows':'3'}),
            'body': forms.TextInput(attrs={'class':'input textarea has-fixed-size', 'rows':'10'}),
            'link': forms.TextInput(attrs={'class':'input'})
        }