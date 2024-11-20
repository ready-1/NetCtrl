from django.shortcuts import render
from .models import WikiPage

def wiki_list(request):
    pages = WikiPage.objects.all()
    return render(request, 'wiki/wiki_list.html', {'pages': pages})