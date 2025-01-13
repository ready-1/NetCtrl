import os
import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from .services.tags import TagService, TagValidationError
from .models import File

@login_required
def file_manager(request):
    def clean_path(path):
        if not path:
            return ''
        # Convert to forward slashes and normalize
        path = path.replace('\\', '/').strip('/')
        # Split path and remove any .. or . components
        parts = [p for p in path.split('/') if p and p not in ('.', '..')]
        return '/'.join(parts)

    # Get and clean current path
    current_path = clean_path(request.GET.get('path', ''))
    tree_view = request.GET.get('tree') == 'true'
    
    # Build full path and ensure it's within uploads directory
    base_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
    current_full_path = os.path.join(base_path, current_path) if current_path else base_path
    
    # Verify path is within uploads directory
    try:
        real_path = os.path.realpath(current_full_path)
        real_base = os.path.realpath(base_path)
        if not real_path.startswith(real_base):
            current_path = ''
            current_full_path = base_path
    except Exception:
        current_path = ''
        current_full_path = base_path
    
    # Create directory if it doesn't exist
    os.makedirs(current_full_path, exist_ok=True)
    
    if tree_view:
        # Get full directory structure for tree view
        def get_directory_tree(path, rel_path=''):
            items = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    item_rel_path = os.path.join(rel_path, item) if rel_path else item
                    items.append({
                        'name': item,
                        'path': item_rel_path,
                        'children': get_directory_tree(item_path, item_rel_path)
                    })
            return items
        
        tree = get_directory_tree(base_path)
        return JsonResponse({'tree': tree})
    else:
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
            
            # Get file object and tags if it's a file
            file_obj = None
            tags = []
            if not is_dir:
                try:
                    file_obj = File.objects.get(path=rel_path)
                    tags = file_obj.tags or []
                except File.DoesNotExist:
                    # Create File record for existing file
                    file_obj = File.objects.create(
                        name=item,
                        path=rel_path,
                        size=os.path.getsize(item_path),
                        type='OTHER',
                        checksum='',
                        tags=[]
                    )
                    file_obj.save()  # Ensure UUID is generated
                    tags = []

            items.append({
                'name': item,
                'is_dir': is_dir,
                'url': url,
                'id': str(file_obj.id) if file_obj else None,
                'tags': tags
            })
        
        # Sort items: directories first, then files, both alphabetically
        items.sort(key=lambda x: (not x['is_dir'], x['name'].lower()))
        
        # Add parent directory if we're in a subdirectory
        if current_path:
            # Get clean parent path
            parts = current_path.split('/')
            parts.pop()  # Remove last component
            parent_path = '/'.join(parts)
            
            items.insert(0, {
                'name': '..',
                'is_dir': True,
                'url': None,
                'parent_path': parent_path  # Add actual parent path
            })
        
        return render(request, 'cms/file_manager.html', {
            'items': items,
            'current_path': current_path
        })

def clean_path(path):
    if not path:
        return ''
    # Convert to forward slashes and normalize
    path = path.replace('\\', '/').strip('/')
    # Split path and remove any .. or . components
    parts = [p for p in path.split('/') if p and p not in ('.', '..')]
    return '/'.join(parts)

def verify_path(path, base_path):
    try:
        real_path = os.path.realpath(path)
        real_base = os.path.realpath(base_path)
        return real_path.startswith(real_base)
    except Exception:
        return False

@login_required
@require_POST
def rename_item(request):
    try:
        data = json.loads(request.body)
        old_name = data.get('old_name')
        new_name = data.get('new_name')
        is_dir = data.get('is_dir', False)
        current_path = clean_path(data.get('path', ''))
        
        if not old_name or not new_name:
            return JsonResponse({'success': False, 'error': 'Name not provided'})
        
        base_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
        old_path = os.path.join(base_path, current_path, old_name)
        new_path = os.path.join(base_path, current_path, new_name)
        
        # Verify paths are within uploads directory
        if not verify_path(old_path, base_path) or not verify_path(new_path, base_path):
            return JsonResponse({'success': False, 'error': 'Invalid path'})
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Update File record if this is a file
        if not is_dir:
            try:
                rel_old_path = os.path.relpath(old_path, settings.MEDIA_ROOT)
                rel_new_path = os.path.relpath(new_path, settings.MEDIA_ROOT)
                file_obj = File.objects.get(path=rel_old_path)
                file_obj.name = new_name
                file_obj.path = rel_new_path
                file_obj.save()
            except File.DoesNotExist:
                pass  # No File record exists
        
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
        current_path = clean_path(data.get('path', ''))
        
        if not name:
            return JsonResponse({'success': False, 'error': 'Name not provided'})
        
        base_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
        path = os.path.join(base_path, current_path, name)
        
        # Verify path is within uploads directory
        if not verify_path(path, base_path):
            return JsonResponse({'success': False, 'error': 'Invalid path'})
        
        if is_dir:
            os.rmdir(path)  # Only removes empty directories
        else:
            # Delete the file
            os.remove(path)
            
            # Delete the File record if it exists
            try:
                rel_path = os.path.relpath(path, settings.MEDIA_ROOT)
                File.objects.filter(path=rel_path).delete()
            except Exception:
                pass  # Ignore if File record doesn't exist
            
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
@require_POST
def move_item(request):
    def clean_path(path):
        if not path:
            return ''
        # Convert to forward slashes and normalize
        path = path.replace('\\', '/').strip('/')
        # Split path and remove any .. or . components
        parts = [p for p in path.split('/') if p and p not in ('.', '..')]
        return '/'.join(parts)

    try:
        data = json.loads(request.body)
        item_name = data.get('name')
        is_dir = data.get('is_dir', False)
        current_path = clean_path(data.get('current_path', ''))
        destination_path = clean_path(data.get('destination_path', ''))
        
        print(f"Moving item: {item_name}")
        print(f"From path: {current_path}")
        print(f"To path: {destination_path}")
        
        if not item_name:
            return JsonResponse({'success': False, 'error': 'Name not provided'})
        
        # Build full paths
        base_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
        src_path = os.path.join(base_path, current_path, item_name)
        dst_path = os.path.join(base_path, destination_path, item_name)
        
        # Verify paths are within uploads directory
        try:
            real_base = os.path.realpath(base_path)
            real_src = os.path.realpath(src_path)
            real_dst = os.path.realpath(dst_path)
            
            if not all(p.startswith(real_base) for p in [real_src, real_dst]):
                return JsonResponse({'success': False, 'error': 'Invalid path'})
        except Exception:
            return JsonResponse({'success': False, 'error': 'Invalid path'})
            
        print(f"Source full path: {src_path}")
        print(f"Destination full path: {dst_path}")
        
        # Basic validation
        if not os.path.exists(src_path):
            return JsonResponse({'success': False, 'error': 'Source item not found'})
            
        # Prevent moving folder into itself or its subdirectories
        if is_dir and (dst_path + os.sep).startswith(src_path + os.sep):
            return JsonResponse({'success': False, 'error': 'Cannot move folder into itself'})
        
        # Check if destination already exists
        if os.path.exists(dst_path):
            return JsonResponse({'success': False, 'error': 'An item with this name already exists at the destination'})
        
        # Create destination directory if it doesn't exist
        dst_dir = os.path.dirname(dst_path)
        os.makedirs(dst_dir, exist_ok=True)
        
        # Perform move operation
        os.rename(src_path, dst_path)
        
        # Update File record if this is a file
        if not is_dir:
            try:
                rel_src_path = os.path.relpath(src_path, settings.MEDIA_ROOT)
                rel_dst_path = os.path.relpath(dst_path, settings.MEDIA_ROOT)
                file_obj = File.objects.get(path=rel_src_path)
                file_obj.path = rel_dst_path
                file_obj.save()
            except File.DoesNotExist:
                pass  # No File record exists
        
        print(f"Move successful")
        return JsonResponse({'success': True})
        
    except Exception as e:
        print(f"Move error: {str(e)}")
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
@require_POST
def upload_file(request):
    if 'file' not in request.FILES:
        return JsonResponse({'success': False, 'error': 'No file provided'})
    
    current_path = clean_path(request.POST.get('path', ''))
    uploaded_file = request.FILES['file']
    
    base_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
    upload_path = os.path.join(base_path, current_path)
    file_path = os.path.join(upload_path, uploaded_file.name)
    
    # Verify path is within uploads directory
    if not verify_path(file_path, base_path):
        return JsonResponse({'success': False, 'error': 'Invalid path'})
    
    # Create uploads directory if it doesn't exist
    os.makedirs(upload_path, exist_ok=True)
    
    try:
        # Save the file
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Create File record
        rel_path = os.path.relpath(file_path, settings.MEDIA_ROOT)
        file_obj = File.objects.create(
            name=uploaded_file.name,
            path=rel_path,
            size=uploaded_file.size,
            type='OTHER',  # Default type
            checksum='',  # TODO: Calculate checksum
            tags=[]
        )
        file_obj.save()  # Ensure UUID is generated
        
        return JsonResponse({
            'success': True,
            'file_id': str(file_obj.id)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@login_required
@require_POST
def create_folder(request):
    try:
        data = json.loads(request.body)
        folder_name = data.get('name')
        current_path = clean_path(data.get('path', ''))
        
        if not folder_name:
            return JsonResponse({'success': False, 'error': 'No folder name provided'})
        
        base_path = os.path.join(settings.MEDIA_ROOT, 'uploads', current_path)
        folder_path = os.path.join(base_path, folder_name)
        
        # Verify path is within uploads directory
        if not verify_path(folder_path, base_path):
            return JsonResponse({'success': False, 'error': 'Invalid path'})
        
        os.makedirs(folder_path, exist_ok=True)
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
@require_POST
def add_tag(request):
    """Add a tag to a file."""
    try:
        data = json.loads(request.body)
        file_id = data.get('file_id')
        tag = data.get('tag')
        
        if not file_id or not tag:
            return JsonResponse({'success': False, 'error': 'File ID and tag are required'})
            
        tag_service = TagService()
        tag_service.add_tag(file_id, tag, 'file')
        
        return JsonResponse({'success': True})
    except TagValidationError as e:
        return JsonResponse({'success': False, 'error': str(e)})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
@require_POST
def remove_tag(request):
    """Remove a tag from a file."""
    try:
        data = json.loads(request.body)
        file_id = data.get('file_id')
        tag = data.get('tag')
        
        if not file_id or not tag:
            return JsonResponse({'success': False, 'error': 'File ID and tag are required'})
            
        tag_service = TagService()
        tag_service.remove_tag(file_id, tag, 'file')
        
        return JsonResponse({'success': True})
    except TagValidationError as e:
        return JsonResponse({'success': False, 'error': str(e)})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
def get_tags(request):
    """Get all tags or tags for a specific file."""
    try:
        file_id = request.GET.get('file_id')
        tag_service = TagService()
        
        if file_id:
            tags = tag_service.get_tags(file_id, 'file')
        else:
            tags = tag_service.get_all_tags('file')
            
        return JsonResponse({'success': True, 'tags': list(tags)})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
def filter_by_tags(request):
    """Filter files by tags."""
    try:
        tags = request.GET.getlist('tags[]')
        if not tags:
            return JsonResponse({'success': False, 'error': 'No tags provided'})
            
        tag_service = TagService()
        files = tag_service.filter_by_tags(tags, 'file')
        
        # Build full URLs for files that exist
        file_list = []
        for file in files:
            file_path = os.path.join(settings.MEDIA_ROOT, file.path)
            if os.path.exists(file_path):
                file_url = f'{settings.MEDIA_URL}{file.path}'
                file_list.append({
                    'id': str(file.id),
                    'name': file.name,
                    'path': file_url,
                    'tags': file.tags or []
                })
            else:
                # Clean up orphaned record
                file.delete()
            
        return JsonResponse({
            'success': True,
            'files': file_list
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
