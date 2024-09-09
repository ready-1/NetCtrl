from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Page
from .forms import PageForm


# Create your views here.
def home(request):
    return render(request, "pages/")


def pages(request):
    pages = Page.objects.all()
    return render(request, "pages/pages.html", {"pages": pages})


def page(request, slug):
    page = Page.objects.get(slug=slug)
    return render(request, "pages/page.html", {"page": page})


def edit(request, slug):
    page = Page.objects.get(slug=slug)
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            page.title = form.cleaned_data["title"]
            page.content = form.cleaned_data["content"]
            page.slug = form.cleaned_data["slug"]
            page.save()
            return HttpResponseRedirect("/")
    else:
        form = PageForm(
            initial={"title": page.title, "content": page.content, "slug": page.slug}
        )
    return render(request, "pages/edit.html", {"page": page, "form": form})


def delete(request, slug):
    page = Page.objects.get(slug=slug)
    if request.method == "POST":
        page.delete()
        return HttpResponseRedirect("/")

    return render(request, "pages/delete.html", {"page": page})

def create(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            page = Page()
            page.title = form.cleaned_data["title"]
            page.content = form.cleaned_data["content"]
            page.slug = form.cleaned_data["slug"]
            page.save()
            return HttpResponseRedirect("/")
    else:
        form = PageForm(initial={"title": "Title", "content": "Content", "slug": "Slug"})
    return render(request, "pages/create.html", {"form": form})

