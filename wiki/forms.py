from django import forms
from tinymce.widgets import TinyMCE
from .models import FileUpload, WikiPage


class WikiPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = WikiPage
        fields = ['title', 'content']


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file', 'name', 'description', 'tags']