import React, { useState, useContext, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Form, Button, Card, Alert, Container, Row, Col } from 'react-bootstrap';
import AuthContext from '../../store/AuthContext';

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  
  const { login, isAuthenticated } = useContext(AuthContext);
  const navigate = useNavigate();
  const location = useLocation();

  // Redirect if already authenticated
  useEffect(() => {
    if (isAuthenticated) {
      // Redirect to the page they tried to visit or to dashboard
      const from = location.state?.from?.pathname || '/';
      navigate(from, { replace: true });
    }
  }, [isAuthenticated, navigate, location]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validate form
    if (!formData.username || !formData.password) {
      setError('Please enter both username and password');
      return;
    }
    
    try {
      setError('');
      setLoading(true);
      
      // Attempt login
      const result = await login(formData);
      
      if (!result.success) {
        setError(result.message);
      }
    } catch (err) {
      setError('Failed to log in. Please try again.');
      console.error('Login error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container">
      <Container>
        <Row className="justify-content-center">
          <Col xs={12} md={6} lg={5}>
            <Card className="login-card shadow">
              <Card.Body>
                <div className="text-center mb-4">
                  <h2 className="mb-3">NetCtrl</h2>
                  <p className="text-muted">Network Switch Management</p>
                </div>
                
                {error && <Alert variant="danger">{error}</Alert>}
                
                <Form onSubmit={handleSubmit}>
                  <Form.Group className="mb-3" controlId="username">
                    <Form.Label>Username</Form.Label>
                    <Form.Control
                      type="text"
                      name="username"
                      value={formData.username}
                      onChange={handleChange}
                      placeholder="Enter your username"
                      required
                    />
                  </Form.Group>

                  <Form.Group className="mb-3" controlId="password">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                      type="password"
                      name="password"
                      value={formData.password}
                      onChange={handleChange}
                      placeholder="Enter your password"
                      required
                    />
                  </Form.Group>

                  <div className="d-grid gap-2 mt-4">
                    <Button 
                      variant="primary" 
                      type="submit" 
                      disabled={loading}
                    >
                      {loading ? 'Logging in...' : 'Log In'}
                    </Button>
                  </div>
                </Form>
              </Card.Body>
              <Card.Footer className="text-center text-muted">
                <small>Contact administrator for account access</small>
              </Card.Footer>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Login;
