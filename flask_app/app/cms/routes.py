import os
import uuid
from flask import request, jsonify, current_app, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import re

from app.cms import cms_bp
from app.models.user import User
from app.models.content import Content, Category, Tag, Attachment, ContentRevision
from app import db

def slugify(text):
    """Convert a string to a URL-friendly slug."""
    # Convert to lowercase
    text = text.lower()
    # Replace non-alphanumeric characters with hyphens
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text

@cms_bp.route('/', methods=['GET'])
@jwt_required()
def list_content():
    """List all published content."""
    # Get query parameters
    category = request.args.get('category')
    tag = request.args.get('tag')
    search = request.args.get('search')
    
    # Base query
    query = Content.query.filter_by(published=True)
    
    # Apply filters
    if category:
        query = query.join(Content.category).filter(Category.name == category)
    
    if tag:
        query = query.join(Content.tags).filter(Tag.name == tag)
    
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            (Content.title.ilike(search_term)) | 
            (Content.content.ilike(search_term)) |
            (Content.summary.ilike(search_term))
        )
    
    # Execute query and convert to dict
    contents = query.order_by(Content.created_at.desc()).all()
    return jsonify([content.to_dict() for content in contents]), 200

@cms_bp.route('/unpublished', methods=['GET'])
@jwt_required()
def list_unpublished():
    """List all unpublished content (admin only)."""
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or not current_user.has_role('Admin'):
        return jsonify({"error": "Unauthorized"}), 403
    
    contents = Content.query.filter_by(published=False).order_by(Content.created_at.desc()).all()
    return jsonify([content.to_dict() for content in contents]), 200

@cms_bp.route('/<string:slug>', methods=['GET'])
@jwt_required()
def get_content(slug):
    """Get a specific content by slug."""
    content = Content.query.filter_by(slug=slug).first_or_404()
    
    # Only allow viewing unpublished content for admins or the author
    if not content.published:
        current_user_id = get_jwt_identity()
        current_user = User.query.get(current_user_id)
        
        if not current_user or (current_user.id != content.author_id and not current_user.has_role('Admin')):
            return jsonify({"error": "Unauthorized"}), 403
    
    return jsonify(content.to_dict()), 200

@cms_bp.route('/', methods=['POST'])
@jwt_required()
def create_content():
    """Create new content."""
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    data = request.json
    
    # Validate required fields
    if 'title' not in data or 'content' not in data:
        return jsonify({"error": "Title and content are required"}), 400
    
    # Get author
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user:
        return jsonify({"error": "User not found"}), 404
    
    # Generate slug from title if not provided
    slug = data.get('slug', slugify(data['title']))
    
    # Check if slug already exists
    if Content.query.filter_by(slug=slug).first():
        return jsonify({"error": "Slug already exists"}), 400
    
    # Create content
    content = Content(
        title=data['title'],
        slug=slug,
        content=data['content'],
        summary=data.get('summary'),
        published=data.get('published', True),
        author_id=current_user_id
    )
    
    # Add category if provided
    if 'category' in data:
        category = Category.query.filter_by(name=data['category']).first()
        if not category:
            category = Category(name=data['category'])
            db.session.add(category)
        content.category = category
    
    # Add tags if provided
    if 'tags' in data and isinstance(data['tags'], list):
        for tag_name in data['tags']:
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.session.add(tag)
            content.tags.append(tag)
    
    db.session.add(content)
    db.session.commit()
    
    return jsonify(content.to_dict()), 201

@cms_bp.route('/<string:slug>', methods=['PUT'])
@jwt_required()
def update_content(slug):
    """Update existing content."""
    content = Content.query.filter_by(slug=slug).first_or_404()
    
    # Check permissions (only author or admin can edit)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or (current_user.id != content.author_id and not current_user.has_role('Admin')):
        return jsonify({"error": "Unauthorized"}), 403
    
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    data = request.json
    
    # Create a revision of the current content
    content.create_revision()
    
    # Update fields
    if 'title' in data:
        content.title = data['title']
    if 'content' in data:
        content.content = data['content']
    if 'summary' in data:
        content.summary = data['summary']
    if 'published' in data:
        content.published = data['published']
    if 'slug' in data:
        # Check if new slug already exists (and is not the current one)
        if data['slug'] != slug and Content.query.filter_by(slug=data['slug']).first():
            return jsonify({"error": "Slug already exists"}), 400
        content.slug = data['slug']
    
    # Update category
    if 'category' in data:
        if data['category']:
            category = Category.query.filter_by(name=data['category']).first()
            if not category:
                category = Category(name=data['category'])
                db.session.add(category)
            content.category = category
        else:
            content.category = None
    
    # Update tags
    if 'tags' in data and isinstance(data['tags'], list):
        # Clear existing tags
        content.tags = []
        
        # Add new tags
        for tag_name in data['tags']:
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.session.add(tag)
            content.tags.append(tag)
    
    db.session.commit()
    
    return jsonify(content.to_dict()), 200

@cms_bp.route('/<string:slug>', methods=['DELETE'])
@jwt_required()
def delete_content(slug):
    """Delete content."""
    content = Content.query.filter_by(slug=slug).first_or_404()
    
    # Check permissions (only author or admin can delete)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or (current_user.id != content.author_id and not current_user.has_role('Admin')):
        return jsonify({"error": "Unauthorized"}), 403
    
    db.session.delete(content)
    db.session.commit()
    
    return jsonify({"message": "Content deleted successfully"}), 200

@cms_bp.route('/categories', methods=['GET'])
@jwt_required()
def list_categories():
    """List all categories."""
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories]), 200

@cms_bp.route('/tags', methods=['GET'])
@jwt_required()
def list_tags():
    """List all tags."""
    tags = Tag.query.all()
    return jsonify([tag.to_dict() for tag in tags]), 200

@cms_bp.route('/<string:slug>/revisions', methods=['GET'])
@jwt_required()
def list_revisions(slug):
    """List all revisions for a content."""
    content = Content.query.filter_by(slug=slug).first_or_404()
    
    # Check permissions (only author or admin can view revisions)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or (current_user.id != content.author_id and not current_user.has_role('Admin')):
        return jsonify({"error": "Unauthorized"}), 403
    
    revisions = content.revisions.order_by(ContentRevision.created_at.desc()).all()
    return jsonify([revision.to_dict() for revision in revisions]), 200

@cms_bp.route('/<string:slug>/revisions/<int:revision_id>', methods=['GET'])
@jwt_required()
def get_revision(slug, revision_id):
    """Get a specific revision."""
    content = Content.query.filter_by(slug=slug).first_or_404()
    
    # Check permissions (only author or admin can view revisions)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or (current_user.id != content.author_id and not current_user.has_role('Admin')):
        return jsonify({"error": "Unauthorized"}), 403
    
    revision = ContentRevision.query.get_or_404(revision_id)
    
    # Make sure the revision belongs to the content
    if revision.content_id != content.id:
        return jsonify({"error": "Revision not found for this content"}), 404
    
    return jsonify(revision.to_dict()), 200

@cms_bp.route('/<string:slug>/attachments', methods=['POST'])
@jwt_required()
def upload_attachment(slug):
    """Upload an attachment to a content."""
    content = Content.query.filter_by(slug=slug).first_or_404()
    
    # Check permissions (only author or admin can add attachments)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or (current_user.id != content.author_id and not current_user.has_role('Admin')):
        return jsonify({"error": "Unauthorized"}), 403
    
    # Check if file is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    
    # Check if file is empty
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Secure the filename
    original_filename = secure_filename(file.filename)
    
    # Generate a unique filename
    filename = f"{uuid.uuid4()}_{original_filename}"
    
    # Get upload directory
    upload_dir = current_app.config.get('UPLOAD_FOLDER', '/app/shared_files')
    
    # Create directory if it doesn't exist
    os.makedirs(upload_dir, exist_ok=True)
    
    # Save the file
    file_path = os.path.join(upload_dir, filename)
    file.save(file_path)
    
    # Create the attachment record
    attachment = Attachment(
        content_id=content.id,
        filename=filename,
        original_filename=original_filename,
        mime_type=file.content_type,
        size=os.path.getsize(file_path)
    )
    
    db.session.add(attachment)
    db.session.commit()
    
    return jsonify(attachment.to_dict()), 201

@cms_bp.route('/attachments/<int:attachment_id>', methods=['DELETE'])
@jwt_required()
def delete_attachment(attachment_id):
    """Delete an attachment."""
    attachment = Attachment.query.get_or_404(attachment_id)
    content = Content.query.get(attachment.content_id)
    
    # Check permissions (only author or admin can delete attachments)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or (current_user.id != content.author_id and not current_user.has_role('Admin')):
        return jsonify({"error": "Unauthorized"}), 403
    
    # Delete the file from disk
    upload_dir = current_app.config.get('UPLOAD_FOLDER', '/app/shared_files')
    file_path = os.path.join(upload_dir, attachment.filename)
    
    try:
        os.remove(file_path)
    except OSError:
        # Just log the error, don't fail
        current_app.logger.error(f"Could not delete file {file_path}")
    
    # Delete the attachment record
    db.session.delete(attachment)
    db.session.commit()
    
    return jsonify({"message": "Attachment deleted successfully"}), 200

@cms_bp.route('/files/<path:filename>', methods=['GET'])
def get_file(filename):
    """Serve a file."""
    upload_dir = current_app.config.get('UPLOAD_FOLDER', '/app/shared_files')
    return send_from_directory(upload_dir, filename)
