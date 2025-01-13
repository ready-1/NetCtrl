import os
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.http import require_POST

@login_required
def file_manager(request):
    # Get current path from query parameter
    current_path = request.GET.get('path', '')
    
    # Ensure path is safe and within uploads directory
    if current_path:
        current_path = os.path.normpath(current_path)
        if current_path.startswith('..') or current_path.startswith('/'):
            current_path = ''
    
    # Build full path
    base_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
    current_full_path = os.path.join(base_path, current_path) if current_path else base_path
    
    # Create directory if it doesn't exist
    os.makedirs(current_full_path, exist_ok=True)
    
    # Get items in current directory
    items = []
    for item in os.listdir(current_full_path):
        item_path = os.path.join(current_full_path, item)
        is_dir = os.path.isdir(item_path)
        
        # Build URL for files
        url = None
        if not is_dir:
            rel_path = os.path.relpath(item_path, settings.MEDIA_ROOT)
            url = f'{settings.MEDIA_URL}{rel_path}'
        
        items.append({
            'name': item,
            'is_dir': is_dir,
            'url': url
        })
    
    # Sort items: directories first, then files, both alphabetically
    items.sort(key=lambda x: (not x['is_dir'], x['name'].lower()))
    
    # Add parent directory if we're in a subdirectory
    if current_path:
        parent_path = os.path.dirname(current_path)
        items.insert(0, {
            'name': '..',
            'is_dir': True,
            'url': None
        })
    
    return render(request, 'cms/file_manager.html', {
        'items': items,
        'current_path': current_path
    })

@login_required
@require_POST
def rename_item(request):
    try:
        data = json.loads(request.body)
        old_name = data.get('old_name')
        new_name = data.get('new_name')
        current_path = data.get('path', '')
        
        if not old_name or not new_name:
            return JsonResponse({'success': False, 'error': 'Name not provided'})
        
        # Ensure path is safe
        if current_path:
            current_path = os.path.normpath(current_path)
            if current_path.startswith('..') or current_path.startswith('/'):
                current_path = ''
        
        base_path = os.path.join(settings.MEDIA_ROOT, 'uploads', current_path)
        old_path = os.path.join(base_path, old_name)
        new_path = os.path.join(base_path, new_name)
        
        os.rename(old_path, new_path)
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
@require_POST
def delete_item(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        is_dir = data.get('is_dir', False)
        current_path = data.get('path', '')
        
        if not name:
            return JsonResponse({'success': False, 'error': 'Name not provided'})
        
        # Ensure path is safe
        if current_path:
            current_path = os.path.normpath(current_path)
            if current_path.startswith('..') or current_path.startswith('/'):
                current_path = ''
        
        base_path = os.path.join(settings.MEDIA_ROOT, 'uploads', current_path)
        path = os.path.join(base_path, name)
        
        if is_dir:
            os.rmdir(path)  # Only removes empty directories
        else:
            os.remove(path)
            
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
@require_POST
def upload_file(request):
    if 'file' not in request.FILES:
        return JsonResponse({'success': False, 'error': 'No file provided'})
    
    current_path = request.POST.get('path', '')
    
    # Ensure path is safe
    if current_path:
        current_path = os.path.normpath(current_path)
        if current_path.startswith('..') or current_path.startswith('/'):
            current_path = ''
    
    uploaded_file = request.FILES['file']
    upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads', current_path)
    
    # Create uploads directory if it doesn't exist
    os.makedirs(upload_path, exist_ok=True)
    
    # Save the file
    file_path = os.path.join(upload_path, uploaded_file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    
    return JsonResponse({'success': True})

@login_required
@require_POST
def create_folder(request):
    try:
        data = json.loads(request.body)
        folder_name = data.get('name')
        current_path = data.get('path', '')
        
        if not folder_name:
            return JsonResponse({'success': False, 'error': 'No folder name provided'})
        
        # Ensure path is safe
        if current_path:
            current_path = os.path.normpath(current_path)
            if current_path.startswith('..') or current_path.startswith('/'):
                current_path = ''
        
        base_path = os.path.join(settings.MEDIA_ROOT, 'uploads', current_path)
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
