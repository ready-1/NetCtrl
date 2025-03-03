-- PostgreSQL Default Data Initialization Script for NetCtrl
-- Populates the database with default data for the application

-- Default roles
INSERT INTO roles (name, description) VALUES 
('admin', 'Full administrative access to all features')
ON CONFLICT (name) DO NOTHING;

INSERT INTO roles (name, description) VALUES 
('manager', 'Management access to create and edit content and switch configurations')
ON CONFLICT (name) DO NOTHING;

INSERT INTO roles (name, description) VALUES 
('user', 'Standard user with read-write access to most features')
ON CONFLICT (name) DO NOTHING;

INSERT INTO roles (name, description) VALUES 
('readonly', 'Read-only access to content and switch information')
ON CONFLICT (name) DO NOTHING;

-- Default admin user (username: admin, password: changeme)
-- Password is hashed, this is just a placeholder that should be changed immediately
INSERT INTO users (username, email, password_hash, is_active, is_approved)
VALUES ('admin', 'admin@netctrl.local', 
        'pbkdf2:sha256:150000$lZ1jHAEq$5088d4c193abd15a5d71c95c494e4b7de91e8785bc19df1913b382aeb41b49b6',
        TRUE, TRUE)
ON CONFLICT (username) DO NOTHING;

-- Assign admin role to admin user
INSERT INTO user_roles (user_id, role_id) 
SELECT u.id, r.id FROM users u, roles r
WHERE u.username = 'admin' AND r.name = 'admin'
ON CONFLICT DO NOTHING;

-- Default categories for CMS
INSERT INTO categories (name, description) VALUES 
('Documentation', 'System documentation and tutorials'),
('Announcements', 'System announcements and updates'),
('Troubleshooting', 'Network troubleshooting guides')
ON CONFLICT (name) DO NOTHING;

-- Default tags
INSERT INTO tags (name) VALUES 
('important'),
('networking'),
('security'),
('configuration'),
('maintenance')
ON CONFLICT (name) DO NOTHING;

-- Default welcome content
INSERT INTO contents (title, slug, content, summary, published, author_id, category_id)
SELECT 
    'Welcome to NetCtrl', 
    'welcome-to-netctrl',
    '# Welcome to NetCtrl

This is the network switch management application. Use this system to:

- Monitor and configure network switches
- Create and share documentation
- Manage network configuration

## Getting Started

1. Change the default admin password
2. Add network switches to the inventory
3. Configure SNMP monitoring settings
4. Create additional users as needed

For more information, refer to the documentation section.',
    'Welcome to the NetCtrl switch management application',
    TRUE,
    u.id,
    c.id
FROM 
    users u, 
    categories c
WHERE 
    u.username = 'admin' AND 
    c.name = 'Announcements'
ON CONFLICT (slug) DO NOTHING;
