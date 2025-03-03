from datetime import datetime
from app import db

class Switch(db.Model):
    """Switch model for storing network switch information."""
    __tablename__ = 'switches'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=True)
    ip_address = db.Column(db.String(39), nullable=False, unique=True)  # IPv4 or IPv6
    description = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(255), nullable=True)
    
    # Authentication
    username = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    snmp_community = db.Column(db.String(64), nullable=True, default='public')
    
    # Device information
    model = db.Column(db.String(128), nullable=True)
    firmware_version = db.Column(db.String(64), nullable=True)
    serial_number = db.Column(db.String(64), nullable=True)
    mac_address = db.Column(db.String(17), nullable=True)  # Format: 00:11:22:33:44:55
    
    # Status
    is_active = db.Column(db.Boolean, default=True)
    status = db.Column(db.String(16), default='unknown')  # unknown, online, offline, error
    last_polled = db.Column(db.DateTime, nullable=True)
    last_error = db.Column(db.Text, nullable=True)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Switch {self.name or self.ip_address}>'
    
    def to_dict(self):
        """Return a dictionary representation of the switch."""
        return {
            'id': self.id,
            'name': self.name,
            'ip_address': self.ip_address,
            'description': self.description,
            'location': self.location,
            'model': self.model,
            'firmware_version': self.firmware_version,
            'serial_number': self.serial_number,
            'mac_address': self.mac_address,
            'is_active': self.is_active,
            'status': self.status,
            'last_polled': self.last_polled.isoformat() if self.last_polled else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
