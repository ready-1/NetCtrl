from django import forms

class PageForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    slug = forms.CharField(max_length=100)

    


