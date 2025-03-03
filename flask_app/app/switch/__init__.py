from flask import Blueprint

switch_bp = Blueprint('switch', __name__)

from app.switch import routes
