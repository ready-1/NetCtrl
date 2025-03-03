import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Row, 
  Col, 
  Card, 
  Table, 
  Badge, 
  Button, 
  Spinner, 
  Form, 
  Alert,
  Modal
} from 'react-bootstrap';
import { Link } from 'react-router-dom';
import apiService from '../../services/api';

/**
 * Switches Component
 * 
 * Lists all network switches in the system with status indicators
 * and management options.
 */
const Switches = () => {
  const [switches, setSwitches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [statusData, setStatusData] = useState({});
  const [searchTerm, setSearchTerm] = useState('');
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [switchToDelete, setSwitchToDelete] = useState(null);
  const [refreshing, setRefreshing] = useState(false);

  // Fetch all switches on component mount
  useEffect(() => {
    fetchSwitches();
    fetchStatus();
  }, []);

  // Refresh status data every 30 seconds
  useEffect(() => {
    const intervalId = setInterval(() => {
      fetchStatus(false);
    }, 30000);
    
    return () => clearInterval(intervalId);
  }, []);

  // Function to fetch switches from API
  const fetchSwitches = async () => {
    setLoading(true);
    try {
      const response = await apiService.switches.getAll();
      setSwitches(response.data);
      setError(null);
    } catch (err) {
      console.error('Error fetching switches:', err);
      setError('Failed to load switches. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  // Function to fetch status data
  const fetchStatus = async (showSpinner = true) => {
    if (showSpinner) {
      setRefreshing(true);
    }
    try {
      const response = await apiService.switches.getStatus();
      setStatusData(response.data);
    } catch (err) {
      console.error('Error fetching status data:', err);
      // Don't show error for status updates to avoid UI clutter
    } finally {
      setRefreshing(false);
    }
  };

  // Function to handle switch deletion
  const handleDelete = async () => {
    if (!switchToDelete) return;
    
    try {
      await apiService.switches.delete(switchToDelete.id);
      setSwitches(switches.filter(s => s.id !== switchToDelete.id));
      setShowDeleteModal(false);
      setSwitchToDelete(null);
    } catch (err) {
      console.error('Error deleting switch:', err);
      setError('Failed to delete switch. Please try again later.');
    }
  };

  // Function to confirm deletion
  const confirmDelete = (switchItem) => {
    setSwitchToDelete(switchItem);
    setShowDeleteModal(true);
  };

  // Function to get status badge
  const getStatusBadge = (switchId) => {
    if (!statusData || !statusData[switchId]) {
      return <Badge bg="secondary">Unknown</Badge>;
    }
    
    const status = statusData[switchId].status;
    
    switch (status) {
      case 'online':
        return <Badge bg="success">Online</Badge>;
      case 'offline':
        return <Badge bg="danger">Offline</Badge>;
      case 'warning':
        return <Badge bg="warning">Warning</Badge>;
      default:
        return <Badge bg="secondary">Unknown</Badge>;
    }
  };

  // Filter switches based on search term
  const filteredSwitches = switches.filter(s => 
    s.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    s.ip_address.includes(searchTerm)
  );

  // Render loading spinner
  if (loading) {
    return (
      <Container className="py-4 text-center">
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </Container>
    );
  }

  return (
    <Container className="py-4">
      <Row className="mb-4 align-items-center">
        <Col>
          <h1>Network Switches</h1>
        </Col>
        <Col xs="auto">
          <Button 
            variant="outline-primary" 
            className="me-2"
            onClick={() => fetchStatus()}
            disabled={refreshing}
          >
            {refreshing ? (
              <>
                <Spinner 
                  as="span" 
                  animation="border" 
                  size="sm" 
                  role="status" 
                  aria-hidden="true" 
                  className="me-2"
                />
                Refreshing...
              </>
            ) : (
              <>
                <i className="bi bi-arrow-clockwise me-2"></i>
                Refresh Status
              </>
            )}
          </Button>
          <Button 
            as={Link} 
            to="/switches/new" 
            variant="primary"
          >
            <i className="bi bi-plus-circle me-2"></i>
            Add Switch
          </Button>
        </Col>
      </Row>

      {error && (
        <Alert variant="danger" dismissible onClose={() => setError(null)}>
          {error}
        </Alert>
      )}

      <Card className="mb-4">
        <Card.Body>
          <Row className="mb-3">
            <Col md={6}>
              <Form.Group controlId="switchSearch">
                <Form.Control
                  type="text"
                  placeholder="Search by name or IP address..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </Form.Group>
            </Col>
          </Row>

          {switches.length === 0 ? (
            <Alert variant="info">
              No switches found. Add a new switch to get started.
            </Alert>
          ) : filteredSwitches.length === 0 ? (
            <Alert variant="info">
              No switches match your search criteria.
            </Alert>
          ) : (
            <Table responsive hover>
              <thead>
                <tr>
                  <th>Name</th>
                  <th>IP Address</th>
                  <th>Model</th>
                  <th>Status</th>
                  <th>Last Updated</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredSwitches.map((switchItem) => (
                  <tr key={switchItem.id}>
                    <td>
                      <Link to={`/switches/${switchItem.id}`}>
                        {switchItem.name}
                      </Link>
                    </td>
                    <td>{switchItem.ip_address}</td>
                    <td>{switchItem.model || 'N/A'}</td>
                    <td>{getStatusBadge(switchItem.id)}</td>
                    <td>
                      {statusData[switchItem.id]?.last_updated 
                        ? new Date(statusData[switchItem.id].last_updated).toLocaleString() 
                        : 'Never'}
                    </td>
                    <td>
                      <Button
                        as={Link}
                        to={`/switches/${switchItem.id}`}
                        variant="outline-primary"
                        size="sm"
                        className="me-2"
                      >
                        <i className="bi bi-eye"></i>
                      </Button>
                      <Button
                        as={Link}
                        to={`/switches/${switchItem.id}/edit`}
                        variant="outline-secondary"
                        size="sm"
                        className="me-2"
                      >
                        <i className="bi bi-pencil"></i>
                      </Button>
                      <Button
                        variant="outline-danger"
                        size="sm"
                        onClick={() => confirmDelete(switchItem)}
                      >
                        <i className="bi bi-trash"></i>
                      </Button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          )}
        </Card.Body>
      </Card>

      {/* Delete Confirmation Modal */}
      <Modal show={showDeleteModal} onHide={() => setShowDeleteModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Confirm Deletion</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Are you sure you want to delete the switch "{switchToDelete?.name}"? 
          This action cannot be undone.
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowDeleteModal(false)}>
            Cancel
          </Button>
          <Button variant="danger" onClick={handleDelete}>
            Delete
          </Button>
        </Modal.Footer>
      </Modal>
    </Container>
  );
};

export default Switches;
