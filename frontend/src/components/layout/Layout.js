import React, { useContext } from 'react';
import { Outlet } from 'react-router-dom';
import { Container, Row, Col } from 'react-bootstrap';
import Sidebar from './Sidebar';
import Header from './Header';
import AuthContext from '../../store/AuthContext';

/**
 * Main application layout
 * 
 * Provides the overall structure for the application with:
 * - Header (top navbar)
 * - Sidebar (left navigation)
 * - Main content area (Outlet for nested routes)
 */
const Layout = ({ darkMode, toggleDarkMode }) => {
  const { user } = useContext(AuthContext);
  
  // Check if user has admin role
  const isAdmin = user?.roles?.includes('admin');

  return (
    <div className="layout">
      <Header 
        darkMode={darkMode} 
        toggleDarkMode={toggleDarkMode} 
        username={user?.username} 
      />
      
      <Container fluid className="px-0">
        <Row className="g-0">
          {/* Sidebar */}
          <Col md={3} lg={2} className="d-md-block sidebar-col">
            <Sidebar isAdmin={isAdmin} />
          </Col>
          
          {/* Main Content */}
          <Col md={9} lg={10} className="ms-md-auto page-content">
            <Outlet />
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Layout;
