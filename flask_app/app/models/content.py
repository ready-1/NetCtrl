from datetime import datetime
from app import db

class Content(db.Model):
    """Content model for the CMS system."""
    __tablename__ = 'contents'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True, index=True)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.String(500), nullable=True)
    published = db.Column(db.Boolean, default=True)
    
    # Author information
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User', backref=db.backref('contents', lazy='dynamic'))
    
    # Category association
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    category = db.relationship('Category', backref=db.backref('contents', lazy='dynamic'))
    
    # Tags (many-to-many relationship)
    tags = db.relationship('Tag', secondary='content_tags', 
                           backref=db.backref('contents', lazy='dynamic'))
    
    # Attachments (one-to-many)
    attachments = db.relationship('Attachment', backref='content', lazy='dynamic',
                                cascade="all, delete-orphan")
    
    # Revisions (one-to-many)
    revisions = db.relationship('ContentRevision', backref='content', lazy='dynamic',
                              cascade="all, delete-orphan")
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Content {self.title}>'
    
    def to_dict(self):
        """Return a dictionary representation of the content."""
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'content': self.content,
            'summary': self.summary,
            'published': self.published,
            'author': self.author.username if self.author else None,
            'category': self.category.name if self.category else None,
            'tags': [tag.name for tag in self.tags],
            'attachments': [attachment.to_dict() for attachment in self.attachments],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def create_revision(self):
        """Create a new revision of the content."""
        revision = ContentRevision(
            content_id=self.id,
            title=self.title,
            content=self.content,
            author_id=self.author_id
        )
        db.session.add(revision)
        return revision


class ContentRevision(db.Model):
    """Model for content revisions."""
    __tablename__ = 'content_revisions'
    
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    # Author information
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User')
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContentRevision {self.id} for {self.content_id}>'
    
    def to_dict(self):
        """Return a dictionary representation of the revision."""
        return {
            'id': self.id,
            'content_id': self.content_id,
            'title': self.title,
            'author': self.author.username if self.author else None,
            'created_at': self.created_at.isoformat()
        }


class Category(db.Model):
    """Model for content categories."""
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<Category {self.name}>'
    
    def to_dict(self):
        """Return a dictionary representation of the category."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


class Tag(db.Model):
    """Model for content tags."""
    __tablename__ = 'tags'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Tag {self.name}>'
    
    def to_dict(self):
        """Return a dictionary representation of the tag."""
        return {
            'id': self.id,
            'name': self.name
        }


# Content-Tag association table
content_tags = db.Table('content_tags',
    db.Column('content_id', db.Integer, db.ForeignKey('contents.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)


class Attachment(db.Model):
    """Model for content attachments."""
    __tablename__ = 'attachments'
    
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    mime_type = db.Column(db.String(128), nullable=False)
    size = db.Column(db.Integer, nullable=False)  # Size in bytes
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Attachment {self.original_filename}>'
    
    def to_dict(self):
        """Return a dictionary representation of the attachment."""
        return {
            'id': self.id,
            'content_id': self.content_id,
            'filename': self.filename,
            'original_filename': self.original_filename,
            'mime_type': self.mime_type,
            'size': self.size,
            'created_at': self.created_at.isoformat()
        }
