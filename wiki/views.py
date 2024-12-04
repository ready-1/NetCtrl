from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from taggit.models import Tag
from .models import FileUpload, WikiPage
from .forms import FileUploadForm, WikiPageForm
from django.contrib.auth.decorators import login_required


def wiki_list(request):
    pages = WikiPage.objects.all()
    return render(request, "wiki/wiki_list.html", {"pages": pages})


def wiki_detail(request, pk):
    page = get_object_or_404(WikiPage, pk=pk)
    return render(request, "wiki/wiki_detail.html", {"page": page})

@login_required
def wiki_add(request):
    if request.method == "POST":
        form = WikiPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("wiki:wiki_list")
    else:
        form = WikiPageForm()
    return render(request, "wiki/wiki_form.html", {"form": form})


@login_required
def wiki_edit(request, pk):
    page = get_object_or_404(WikiPage, pk=pk)
    if request.method == "POST":
        form = WikiPageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect("wiki:wiki_detail", pk=page.pk)
    else:
        form = WikiPageForm(instance=page)
    return render(request, "wiki/wiki_form.html", {"form": form})

@login_required
def wiki_delete(request, pk):
    page = get_object_or_404(WikiPage, pk=pk)
    if request.method == "POST":
        page.delete()
        return redirect("wiki:wiki_list")
    return render(request, "wiki/wiki_confirm_delete.html", {"page": page})


# File Manager Views
@login_required
def file_list(request):
    files = FileUpload.objects.all()
    return render(request, "wiki/file_list.html", {"files": files})

@login_required
def file_upload(request):
    existing_tags = Tag.objects.all()  # Fetch all existing tags
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("wiki:file_list")
    else:
        form = FileUploadForm()
    return render(
        request, "wiki/file_upload.html", {"form": form, "existing_tags": existing_tags}
    )

@login_required
def file_delete(request, pk):
    file = get_object_or_404(FileUpload, pk=pk)
    file.delete()
    return redirect("wiki:file_list")

@login_required
def file_confirm_delete(request, pk):
    file = get_object_or_404(FileUpload, pk=pk)
    if request.method == "POST":
        file.delete()
        return redirect("wiki:file_list")
    return render(request, "wiki/file_confirm_delete.html", {"file": file})

@login_required
@csrf_exempt
def image_upload(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        if file:
            path = default_storage.save(
                f"uploads/wiki_images/{file.name}", ContentFile(file.read())
            )
            return JsonResponse({"location": default_storage.url(path)})
    return JsonResponse({"error": "Image upload failed"}, status=400)

@login_required
def file_list_api(request):
    files = FileUpload.objects.all()
    file_data = [{"name": file.name, "url": file.file.url} for file in files]
    return JsonResponse(file_data, safe=False)
