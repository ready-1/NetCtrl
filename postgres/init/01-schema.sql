-- PostgreSQL Initialization Script for NetCtrl
-- Creates all necessary database tables for the application

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_approved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create roles table
CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL UNIQUE,
    description VARCHAR(255)
);

-- Create user-role association table
CREATE TABLE IF NOT EXISTS user_roles (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    role_id INTEGER REFERENCES roles(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, role_id)
);

-- Create switches table
CREATE TABLE IF NOT EXISTS switches (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128),
    ip_address VARCHAR(39) NOT NULL UNIQUE,
    description VARCHAR(255),
    location VARCHAR(255),
    username VARCHAR(64),
    password VARCHAR(64),
    snmp_community VARCHAR(64) DEFAULT 'public',
    model VARCHAR(128),
    firmware_version VARCHAR(64),
    serial_number VARCHAR(64),
    mac_address VARCHAR(17),
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(16) DEFAULT 'unknown',
    last_polled TIMESTAMP,
    last_error TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL UNIQUE,
    description VARCHAR(255)
);

-- Create tags table
CREATE TABLE IF NOT EXISTS tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL UNIQUE
);

-- Create contents table
CREATE TABLE IF NOT EXISTS contents (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) NOT NULL UNIQUE,
    content TEXT NOT NULL,
    summary VARCHAR(500),
    published BOOLEAN DEFAULT TRUE,
    author_id INTEGER REFERENCES users(id),
    category_id INTEGER REFERENCES categories(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create content-tag association table
CREATE TABLE IF NOT EXISTS content_tags (
    content_id INTEGER REFERENCES contents(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (content_id, tag_id)
);

-- Create content revisions table
CREATE TABLE IF NOT EXISTS content_revisions (
    id SERIAL PRIMARY KEY,
    content_id INTEGER NOT NULL REFERENCES contents(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create attachments table
CREATE TABLE IF NOT EXISTS attachments (
    id SERIAL PRIMARY KEY,
    content_id INTEGER NOT NULL REFERENCES contents(id) ON DELETE CASCADE,
    filename VARCHAR(255) NOT NULL,
    original_filename VARCHAR(255) NOT NULL,
    mime_type VARCHAR(128) NOT NULL,
    size INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_contents_slug ON contents(slug);
CREATE INDEX IF NOT EXISTS idx_contents_author ON contents(author_id);
CREATE INDEX IF NOT EXISTS idx_contents_category ON contents(category_id);
CREATE INDEX IF NOT EXISTS idx_revisions_content ON content_revisions(content_id);
CREATE INDEX IF NOT EXISTS idx_attachments_content ON attachments(content_id);
