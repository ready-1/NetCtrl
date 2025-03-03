import React from 'react';
import { Nav } from 'react-bootstrap';
import { NavLink } from 'react-router-dom';

/**
 * Sidebar navigation component
 * 
 * Provides main application navigation with:
 * - Dashboard
 * - Switch management
 * - CMS
 * - Administration (for admin users only)
 * - Settings
 */
const Sidebar = ({ isAdmin }) => {
  return (
    <div className="sidebar py-3">
      <Nav className="flex-column">
        <Nav.Item>
          <Nav.Link as={NavLink} to="/" end className="nav-link">
            <i className="bi bi-speedometer2 me-2"></i>
            Dashboard
          </Nav.Link>
        </Nav.Item>
        
        <Nav.Item>
          <Nav.Link as={NavLink} to="/switches" className="nav-link">
            <i className="bi bi-router me-2"></i>
            Switches
          </Nav.Link>
        </Nav.Item>
        
        <Nav.Item>
          <Nav.Link as={NavLink} to="/content" className="nav-link">
            <i className="bi bi-file-text me-2"></i>
            Content
          </Nav.Link>
        </Nav.Item>
        
        {isAdmin && (
          <Nav.Item>
            <Nav.Link as={NavLink} to="/admin/users" className="nav-link">
              <i className="bi bi-people me-2"></i>
              User Management
            </Nav.Link>
          </Nav.Item>
        )}
        
        <Nav.Item>
          <Nav.Link as={NavLink} to="/settings" className="nav-link">
            <i className="bi bi-gear me-2"></i>
            Settings
          </Nav.Link>
        </Nav.Item>
      </Nav>
      
      <div className="mt-auto p-3 text-light text-center">
        <small className="text-muted d-block mb-2">NetCtrl v0.1.0</small>
      </div>
    </div>
  );
};

export default Sidebar;
