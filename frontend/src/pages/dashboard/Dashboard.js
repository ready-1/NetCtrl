import React, { useState, useEffect, useContext } from 'react';
import { Card, Row, Col, Alert, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import AuthContext from '../../store/AuthContext';

/**
 * Dashboard Component
 * 
 * Main landing page for authenticated users.
 * Displays summary information and quick access to key features.
 */
const Dashboard = () => {
  const { user } = useContext(AuthContext);
  const [stats, setStats] = useState({
    switches: { total: 0, online: 0, offline: 0 },
    content: { total: 0, recent: 0 },
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch dashboard data
  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        setLoading(true);
        // TODO: Replace with actual API call
        // Simulated data for initial implementation
        setTimeout(() => {
          setStats({
            switches: { total: 12, online: 10, offline: 2 },
            content: { total: 15, recent: 3 },
          });
          setLoading(false);
        }, 500);
      } catch (err) {
        console.error('Error fetching dashboard data:', err);
        setError('Failed to load dashboard data. Please try again later.');
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  if (loading) {
    return (
      <div className="text-center my-5">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-2">Loading dashboard...</p>
      </div>
    );
  }

  return (
    <div className="dashboard">
      <h1 className="mb-4">Dashboard</h1>
      
      {error && <Alert variant="danger">{error}</Alert>}
      
      <div className="welcome-section mb-4">
        <Card>
          <Card.Body>
            <Card.Title>Welcome, {user?.username}</Card.Title>
            <Card.Text>
              Use this dashboard to monitor your network switches and access system functions.
            </Card.Text>
          </Card.Body>
        </Card>
      </div>
      
      <Row className="mb-4">
        {/* Switch Status Summary */}
        <Col md={6} lg={4} className="mb-3">
          <Card className="h-100">
            <Card.Header>
              <i className="bi bi-router me-2"></i>
              Switch Status
            </Card.Header>
            <Card.Body>
              <div className="d-flex justify-content-around text-center">
                <div>
                  <h3>{stats.switches.total}</h3>
                  <p className="text-muted">Total</p>
                </div>
                <div>
                  <h3 className="text-success">{stats.switches.online}</h3>
                  <p className="text-muted">Online</p>
                </div>
                <div>
                  <h3 className="text-danger">{stats.switches.offline}</h3>
                  <p className="text-muted">Offline</p>
                </div>
              </div>
              <div className="d-grid gap-2 mt-3">
                <Button as={Link} to="/switches" variant="outline-primary" size="sm">
                  View All Switches
                </Button>
              </div>
            </Card.Body>
          </Card>
        </Col>
        
        {/* Recent Content */}
        <Col md={6} lg={4} className="mb-3">
          <Card className="h-100">
            <Card.Header>
              <i className="bi bi-file-text me-2"></i>
              Content
            </Card.Header>
            <Card.Body>
              <div className="d-flex justify-content-around text-center">
                <div>
                  <h3>{stats.content.total}</h3>
                  <p className="text-muted">Total Articles</p>
                </div>
                <div>
                  <h3>{stats.content.recent}</h3>
                  <p className="text-muted">Recent Updates</p>
                </div>
              </div>
              <div className="d-grid gap-2 mt-3">
                <Button as={Link} to="/content" variant="outline-primary" size="sm">
                  Manage Content
                </Button>
              </div>
            </Card.Body>
          </Card>
        </Col>
        
        {/* Quick Actions */}
        <Col md={6} lg={4} className="mb-3">
          <Card className="h-100">
            <Card.Header>
              <i className="bi bi-lightning-charge me-2"></i>
              Quick Actions
            </Card.Header>
            <Card.Body>
              <div className="d-grid gap-2">
                <Button as={Link} to="/switches" variant="outline-primary" size="sm">
                  <i className="bi bi-plus-circle me-2"></i>
                  Add New Switch
                </Button>
                <Button as={Link} to="/content/new" variant="outline-primary" size="sm">
                  <i className="bi bi-file-earmark-plus me-2"></i>
                  Create Content
                </Button>
                {user?.roles?.includes('admin') && (
                  <Button as={Link} to="/admin/users" variant="outline-primary" size="sm">
                    <i className="bi bi-person-plus me-2"></i>
                    Manage Users
                  </Button>
                )}
              </div>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default Dashboard;
