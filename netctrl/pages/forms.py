from tinymce.widgets import TinyMCE

from django import forms
from .models import Page

class PageForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))
    slug = forms.CharField(max_length=100)

        

    


