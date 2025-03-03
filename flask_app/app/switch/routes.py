from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import redis
import json
import os

from app.switch import switch_bp
from app.models.user import User
from app.models.switch import Switch
from app import db

# Redis connection
def get_redis_connection():
    """Get a Redis connection."""
    redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
    return redis.from_url(redis_url)

@switch_bp.route('/', methods=['GET'])
@jwt_required()
def list_switches():
    """List all switches."""
    switches = Switch.query.all()
    return jsonify([switch.to_dict() for switch in switches]), 200

@switch_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_switch(id):
    """Get a switch by ID."""
    switch = Switch.query.get_or_404(id)
    return jsonify(switch.to_dict()), 200

@switch_bp.route('/', methods=['POST'])
@jwt_required()
def create_switch():
    """Create a new switch."""
    # Check if user has permission (admin or manager)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or not (current_user.has_role('Admin') or current_user.has_role('Manager')):
        return jsonify({"error": "Unauthorized"}), 403
    
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    data = request.json
    
    # Validate required fields
    if 'ip_address' not in data:
        return jsonify({"error": "IP address is required"}), 400
    
    # Check if switch already exists
    existing_switch = Switch.query.filter_by(ip_address=data['ip_address']).first()
    if existing_switch:
        return jsonify({"error": "Switch with this IP address already exists"}), 400
    
    # Create new switch
    switch = Switch(
        ip_address=data['ip_address'],
        name=data.get('name'),
        description=data.get('description'),
        location=data.get('location'),
        username=data.get('username'),
        password=data.get('password'),
        snmp_community=data.get('snmp_community', 'public'),
        is_active=data.get('is_active', True)
    )
    
    db.session.add(switch)
    db.session.commit()
    
    return jsonify(switch.to_dict()), 201

@switch_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_switch(id):
    """Update a switch."""
    # Check if user has permission (admin or manager)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or not (current_user.has_role('Admin') or current_user.has_role('Manager')):
        return jsonify({"error": "Unauthorized"}), 403
    
    switch = Switch.query.get_or_404(id)
    
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    data = request.json
    
    # Update fields
    if 'name' in data:
        switch.name = data['name']
    if 'ip_address' in data:
        # Check if IP address is already in use by another switch
        existing_switch = Switch.query.filter_by(ip_address=data['ip_address']).first()
        if existing_switch and existing_switch.id != id:
            return jsonify({"error": "IP address already in use by another switch"}), 400
        switch.ip_address = data['ip_address']
    if 'description' in data:
        switch.description = data['description']
    if 'location' in data:
        switch.location = data['location']
    if 'username' in data:
        switch.username = data['username']
    if 'password' in data:
        switch.password = data['password']
    if 'snmp_community' in data:
        switch.snmp_community = data['snmp_community']
    if 'is_active' in data:
        switch.is_active = data['is_active']
    
    db.session.commit()
    
    return jsonify(switch.to_dict()), 200

@switch_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_switch(id):
    """Delete a switch."""
    # Check if user has permission (admin only)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or not current_user.has_role('Admin'):
        return jsonify({"error": "Unauthorized"}), 403
    
    switch = Switch.query.get_or_404(id)
    
    db.session.delete(switch)
    db.session.commit()
    
    return jsonify({"message": "Switch deleted successfully"}), 200

@switch_bp.route('/<int:id>/metrics', methods=['GET'])
@jwt_required()
def get_switch_metrics(id):
    """Get real-time metrics for a switch."""
    switch = Switch.query.get_or_404(id)
    
    # Get metrics from Redis
    r = get_redis_connection()
    metrics_json = r.get(f"switch:{id}:metrics")
    
    if not metrics_json:
        return jsonify({
            "switch_id": id,
            "switch_name": switch.name,
            "ip_address": switch.ip_address,
            "metrics": {},
            "message": "No metrics available"
        }), 200
    
    metrics = json.loads(metrics_json)
    
    return jsonify({
        "switch_id": id,
        "switch_name": switch.name,
        "ip_address": switch.ip_address,
        "metrics": metrics
    }), 200

@switch_bp.route('/<int:id>/poll', methods=['POST'])
@jwt_required()
def poll_switch(id):
    """Trigger an immediate poll for a switch."""
    # Check if user has permission (admin or manager)
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if not current_user or not (current_user.has_role('Admin') or current_user.has_role('Manager')):
        return jsonify({"error": "Unauthorized"}), 403
    
    switch = Switch.query.get_or_404(id)
    
    # Trigger Celery tasks
    from app.worker.tasks import poll_switches_config, poll_switches_metrics
    
    # Start configuration polling task (async)
    config_task = poll_switches_config.apply_async(
        kwargs={"switch_ids": [id]},
        countdown=0
    )
    
    # Start metrics polling task (async)
    metrics_task = poll_switches_metrics.apply_async(
        kwargs={"switch_ids": [id]},
        countdown=1
    )
    
    return jsonify({
        "message": "Polling initiated",
        "switch_id": id,
        "config_task_id": config_task.id,
        "metrics_task_id": metrics_task.id
    }), 202

@switch_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    """Get dashboard data for all switches."""
    switches = Switch.query.all()
    r = get_redis_connection()
    
    dashboard_data = {
        "total_switches": len(switches),
        "online_switches": 0,
        "offline_switches": 0,
        "switches": []
    }
    
    for switch in switches:
        switch_data = switch.to_dict()
        
        # Add metrics if available
        metrics_json = r.get(f"switch:{switch.id}:metrics")
        if metrics_json:
            switch_data["metrics"] = json.loads(metrics_json)
        
        # Count online/offline switches
        if switch.status == "online":
            dashboard_data["online_switches"] += 1
        elif switch.status == "offline":
            dashboard_data["offline_switches"] += 1
        
        dashboard_data["switches"].append(switch_data)
    
    return jsonify(dashboard_data), 200
