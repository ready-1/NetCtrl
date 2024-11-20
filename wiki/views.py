from django.shortcuts import render
from .models import WikiPage
from .forms import WikiPageForm

def wiki_list(request):
    pages = WikiPage.objects.all()
    return render(request, 'wiki/wiki_list.html', {'pages': pages})

from django.shortcuts import get_object_or_404

def wiki_detail(request, pk):
    page = get_object_or_404(WikiPage, pk=pk)
    return render(request, 'wiki/wiki_detail.html', {'page': page})

from django.shortcuts import redirect
from .forms import WikiPageForm

def wiki_add(request):
    if request.method == "POST":
        form = WikiPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wiki:wiki_list')
    else:
        form = WikiPageForm()
    return render(request, 'wiki/wiki_form.html', {'form': form})

def wiki_edit(request, pk):
    page = get_object_or_404(WikiPage, pk=pk)
    if request.method == "POST":
        form = WikiPageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('wiki:wiki_detail', pk=page.pk)
    else:
        form = WikiPageForm(instance=page)
    return render(request, 'wiki/wiki_form.html', {'form': form})

def wiki_delete(request, pk):
    page = get_object_or_404(WikiPage, pk=pk)
    if request.method == "POST":
        page.delete()
        return redirect('wiki:wiki_list')
    return render(request, 'wiki/wiki_confirm_delete.html', {'page': page})