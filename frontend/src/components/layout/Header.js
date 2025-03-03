import React, { useContext } from 'react';
import { Navbar, Nav, Button, Form } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import AuthContext from '../../store/AuthContext';

/**
 * Application header component
 * 
 * Displays top navigation bar with:
 * - Application title/logo
 * - User information
 * - Dark mode toggle
 * - Logout button
 */
const Header = ({ darkMode, toggleDarkMode, username }) => {
  const { logout } = useContext(AuthContext);

  return (
    <Navbar bg={darkMode ? 'dark' : 'light'} variant={darkMode ? 'dark' : 'light'} expand="lg" className="px-3 py-2 shadow-sm">
      <Navbar.Brand as={Link} to="/">
        <i className="bi bi-router me-2"></i>
        NetCtrl
      </Navbar.Brand>
      
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      
      <Navbar.Collapse id="basic-navbar-nav" className="justify-content-end">
        <Nav>
          {/* Dark Mode Toggle */}
          <div className="d-flex align-items-center me-3">
            <i className={`bi ${darkMode ? 'bi-moon-fill' : 'bi-sun-fill'} me-2`}></i>
            <Form.Check
              type="switch"
              id="dark-mode-switch"
              label=""
              checked={darkMode}
              onChange={toggleDarkMode}
            />
          </div>
          
          {/* User Info */}
          <div className="d-flex align-items-center me-3">
            <div className="avatar me-2">
              {username ? username.charAt(0).toUpperCase() : 'U'}
            </div>
            <span>{username}</span>
          </div>
          
          {/* Logout Button */}
          <Button 
            variant={darkMode ? 'outline-light' : 'outline-dark'} 
            size="sm"
            onClick={logout}
          >
            <i className="bi bi-box-arrow-right me-1"></i>
            Logout
          </Button>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default Header;
