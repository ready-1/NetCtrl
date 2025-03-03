from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

# User-Role association table
user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
)

class User(db.Model):
    """User model for authentication and authorization."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    roles = db.relationship('Role', secondary=user_roles, 
                          backref=db.backref('users', lazy='dynamic'))
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        """Set the password hash for the user."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the password is correct."""
        return check_password_hash(self.password_hash, password)
    
    def has_role(self, role_name):
        """Check if the user has a specific role."""
        return any(role.name == role_name for role in self.roles)
    
    def add_role(self, role):
        """Add a role to the user."""
        if not self.has_role(role.name):
            self.roles.append(role)
    
    def remove_role(self, role):
        """Remove a role from the user."""
        if self.has_role(role.name):
            self.roles.remove(role)
    
    def to_dict(self):
        """Return a dictionary representation of the user."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active,
            'is_approved': self.is_approved,
            'roles': [role.name for role in self.roles],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class Role(db.Model):
    """Role model for user permissions."""
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<Role {self.name}>'
    
    def to_dict(self):
        """Return a dictionary representation of the role."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
