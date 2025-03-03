from flask import jsonify
from app.api import api_bp

@api_bp.route('/')
def index():
    """Root API endpoint."""
    return jsonify({
        'name': 'NetCtrl API',
        'version': '1.0.0',
        'documentation': '/api/docs',
        'endpoints': [
            '/api/auth',
            '/api/cms',
            '/api/switch'
        ]
    })

@api_bp.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'services': {
            'api': 'up',
            'database': 'up',
            'redis': 'up'
        }
    })
