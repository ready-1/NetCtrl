from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.auth import auth_bp
from app.models.user import User, Role
from app import db

@auth_bp.route('/login', methods=['POST'])
def login():
    """Login route to authenticate users and issue JWT tokens."""
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    user = User.query.filter_by(username=username).first()
    
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401
    
    if not user.is_active:
        return jsonify({"error": "Account is disabled"}), 403
    
    if not user.is_approved:
        return jsonify({"error": "Account is pending approval"}), 403
    
    # Create JWT token
    access_token = create_access_token(identity=user.id)
    
    return jsonify({
        "access_token": access_token,
        "user": user.to_dict()
    }), 200

@auth_bp.route('/register', methods=['POST'])
def register():
    """Register a new user (pending approval)."""
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    
    if not username or not password or not email:
        return jsonify({"error": "Missing required fields"}), 400
    
    # Check if user already exists
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({"error": "Username already exists"}), 400
    
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"error": "Email already registered"}), 400
    
    # Create new user
    user = User(username=username, email=email, is_approved=False)
    user.set_password(password)
    
    # Add default role
    default_role = Role.query.filter_by(name='User').first()
    if default_role:
        user.roles.append(default_role)
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        "message": "User registered successfully, pending approval",
        "user": user.to_dict()
    }), 201

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    """Get the current user's profile."""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user.to_dict()), 200

@auth_bp.route('/users', methods=['GET'])
@jwt_required()
def list_users():
    """List all users (admin only)."""
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or not current_user.has_role('Admin'):
        return jsonify({"error": "Unauthorized"}), 403
    
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@auth_bp.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    """Update a user (admin only or self)."""
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user:
        return jsonify({"error": "User not found"}), 404
    
    # User can update themselves, but only admin can update others
    if id != current_user_id and not current_user.has_role('Admin'):
        return jsonify({"error": "Unauthorized"}), 403
    
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if request.is_json:
        data = request.json
        
        # Regular users can only update certain fields for themselves
        if id == current_user_id and not current_user.has_role('Admin'):
            if 'email' in data:
                user.email = data['email']
            if 'password' in data:
                user.set_password(data['password'])
        else:
            # Admins can update more fields
            if 'email' in data:
                user.email = data['email']
            if 'password' in data:
                user.set_password(data['password'])
            if 'is_active' in data:
                user.is_active = data['is_active']
            if 'is_approved' in data:
                user.is_approved = data['is_approved']
            
            # Update roles
            if 'roles' in data and isinstance(data['roles'], list):
                # Clear existing roles
                user.roles = []
                
                # Add new roles
                for role_name in data['roles']:
                    role = Role.query.filter_by(name=role_name).first()
                    if role:
                        user.roles.append(role)
        
        db.session.commit()
        return jsonify(user.to_dict()), 200
    
    return jsonify({"error": "Missing JSON in request"}), 400

@auth_bp.route('/roles', methods=['GET'])
@jwt_required()
def list_roles():
    """List all available roles."""
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or not current_user.has_role('Admin'):
        return jsonify({"error": "Unauthorized"}), 403
    
    roles = Role.query.all()
    return jsonify([role.to_dict() for role in roles]), 200
