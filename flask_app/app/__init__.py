import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    # Load configuration
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
            SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL', 'sqlite:///netctrl.db'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY', 'dev-jwt-secret'),
            REDIS_URL=os.environ.get('REDIS_URL', 'redis://localhost:6379/0'),
            CORS_HEADERS='Content-Type',
        )
    else:
        app.config.from_mapping(test_config)
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # SSL warning suppression (temporary workaround for self-signed certificates)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # Register blueprints
    from app.api import api_bp
    from app.auth import auth_bp
    from app.cms import cms_bp
    from app.switch import switch_bp
    
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(cms_bp, url_prefix='/api/cms')
    app.register_blueprint(switch_bp, url_prefix='/api/switch')
    
    # Shell context
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'app': app}
    
    # Create database tables if they don't exist (for development)
    with app.app_context():
        db.create_all()
    
    return app
