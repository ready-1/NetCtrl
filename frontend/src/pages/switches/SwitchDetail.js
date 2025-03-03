import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Row, 
  Col, 
  Card, 
  Button, 
  Nav, 
  Tab, 
  Table, 
  Badge, 
  Alert, 
  Spinner,
  ListGroup,
  ProgressBar
} from 'react-bootstrap';
import { useParams, Link, useNavigate } from 'react-router-dom';
import apiService from '../../services/api';

/**
 * SwitchDetail Component
 * 
 * Displays detailed information about a specific network switch,
 * including configuration, metrics, and port status.
 */
const SwitchDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [switchData, setSwitchData] = useState(null);
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('overview');
  const [refreshing, setRefreshing] = useState(false);

  // Fetch switch data and metrics on component mount
  useEffect(() => {
    fetchSwitchData();
    fetchMetrics();
    
    // Set up interval to refresh metrics every 30 seconds
    const intervalId = setInterval(() => {
      fetchMetrics(false);
    }, 30000);
    
    return () => clearInterval(intervalId);
  }, [id]);

  // Function to fetch switch data
  const fetchSwitchData = async () => {
    setLoading(true);
    try {
      const response = await apiService.switches.getById(id);
      setSwitchData(response.data);
      setError(null);
    } catch (err) {
      console.error('Error fetching switch data:', err);
      setError('Failed to load switch details. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  // Function to fetch metrics
  const fetchMetrics = async (showSpinner = true) => {
    if (showSpinner) {
      setRefreshing(true);
    }
    try {
      const response = await apiService.switches.getMetrics(id);
      setMetrics(response.data);
    } catch (err) {
      console.error('Error fetching metrics:', err);
      // Don't show error for metrics updates to avoid UI clutter
    } finally {
      setRefreshing(false);
    }
  };

  // Get status badge color
  const getStatusBadge = (status) => {
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

  // Get port status badge
  const getPortStatusBadge = (status) => {
    switch (status) {
      case 'up':
        return <Badge bg="success">Up</Badge>;
      case 'down':
        return <Badge bg="danger">Down</Badge>;
      case 'disabled':
        return <Badge bg="secondary">Disabled</Badge>;
      default:
        return <Badge bg="secondary">Unknown</Badge>;
    }
  };

  // Format bytes to human readable format
  const formatBytes = (bytes) => {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

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

  // Render error message
  if (error) {
    return (
      <Container className="py-4">
        <Alert variant="danger">
          <Alert.Heading>Error</Alert.Heading>
          <p>{error}</p>
          <div className="d-flex justify-content-end">
            <Button onClick={() => navigate('/switches')} variant="outline-danger">
              Back to Switches
            </Button>
          </div>
        </Alert>
      </Container>
    );
  }

  return (
    <Container className="py-4">
      {/* Header */}
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>{switchData?.name || 'Switch Details'}</h1>
        <div>
          <Button 
            variant="outline-primary" 
            className="me-2"
            onClick={() => fetchMetrics()}
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
                Refresh Metrics
              </>
            )}
          </Button>
          <Button 
            as={Link} 
            to={`/switches/${id}/edit`} 
            variant="outline-secondary" 
            className="me-2"
          >
            <i className="bi bi-pencil me-2"></i>
            Edit
          </Button>
          <Button as={Link} to="/switches" variant="outline-secondary">
            <i className="bi bi-arrow-left me-2"></i>
            Back
          </Button>
        </div>
      </div>

      {/* Switch Status Card */}
      <Card className="mb-4">
        <Card.Body>
          <Row>
            <Col md={3} className="border-end">
              <div className="text-center mb-3">
                <h5>Status</h5>
                <div className="my-2">
                  {getStatusBadge(switchData?.status || 'unknown')}
                </div>
                <div className="text-muted small">
                  Last Updated: {switchData?.last_updated 
                    ? new Date(switchData.last_updated).toLocaleString() 
                    : 'Never'}
                </div>
              </div>
            </Col>
            <Col md={3} className="border-end">
              <div className="text-center mb-3">
                <h5>IP Address</h5>
                <div className="my-2 fw-bold">
                  {switchData?.ip_address || 'N/A'}
                </div>
                <div className="text-muted small">
                  MAC: {switchData?.mac_address || 'N/A'}
                </div>
              </div>
            </Col>
            <Col md={3} className="border-end">
              <div className="text-center mb-3">
                <h5>Model</h5>
                <div className="my-2 fw-bold">
                  {switchData?.model || 'N/A'}
                </div>
                <div className="text-muted small">
                  Firmware: {switchData?.firmware_version || 'N/A'}
                </div>
              </div>
            </Col>
            <Col md={3}>
              <div className="text-center mb-3">
                <h5>Uptime</h5>
                <div className="my-2 fw-bold">
                  {metrics?.uptime || 'N/A'}
                </div>
                <div className="text-muted small">
                  Serial: {switchData?.serial_number || 'N/A'}
                </div>
              </div>
            </Col>
          </Row>
        </Card.Body>
      </Card>

      {/* Tabs */}
      <Tab.Container id="switch-tabs" activeKey={activeTab} onSelect={setActiveTab}>
        <Card>
          <Card.Header>
            <Nav variant="tabs">
              <Nav.Item>
                <Nav.Link eventKey="overview">Overview</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="ports">Ports</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="vlans">VLANs</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="configuration">Configuration</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="logs">Logs</Nav.Link>
              </Nav.Item>
            </Nav>
          </Card.Header>
          <Card.Body>
            <Tab.Content>
              {/* Overview Tab */}
              <Tab.Pane eventKey="overview">
                <Row>
                  <Col md={6}>
                    <Card className="mb-4">
                      <Card.Header>System Information</Card.Header>
                      <ListGroup variant="flush">
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">Hostname:</Col>
                            <Col>{switchData?.name || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">Model:</Col>
                            <Col>{switchData?.model || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">Serial Number:</Col>
                            <Col>{switchData?.serial_number || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">Firmware:</Col>
                            <Col>{switchData?.firmware_version || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">Hardware Rev:</Col>
                            <Col>{switchData?.hardware_version || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">Last Backup:</Col>
                            <Col>
                              {switchData?.last_backup_date 
                                ? new Date(switchData.last_backup_date).toLocaleString() 
                                : 'Never'}
                            </Col>
                          </Row>
                        </ListGroup.Item>
                      </ListGroup>
                    </Card>

                    <Card className="mb-4">
                      <Card.Header>Network Information</Card.Header>
                      <ListGroup variant="flush">
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">IP Address:</Col>
                            <Col>{switchData?.ip_address || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">MAC Address:</Col>
                            <Col>{switchData?.mac_address || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">Subnet Mask:</Col>
                            <Col>{switchData?.subnet_mask || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">Gateway:</Col>
                            <Col>{switchData?.default_gateway || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <Row>
                            <Col xs={4} className="fw-bold">DNS Servers:</Col>
                            <Col>{switchData?.dns_servers || 'N/A'}</Col>
                          </Row>
                        </ListGroup.Item>
                      </ListGroup>
                    </Card>
                  </Col>

                  <Col md={6}>
                    <Card className="mb-4">
                      <Card.Header>Resource Utilization</Card.Header>
                      <Card.Body>
                        <h6>CPU Utilization</h6>
                        <ProgressBar 
                          now={metrics?.cpu_utilization || 0} 
                          label={`${metrics?.cpu_utilization || 0}%`}
                          variant={metrics?.cpu_utilization > 80 ? 'danger' : 
                                  metrics?.cpu_utilization > 60 ? 'warning' : 'success'}
                          className="mb-3"
                        />
                        
                        <h6>Memory Utilization</h6>
                        <ProgressBar 
                          now={metrics?.memory_utilization || 0} 
                          label={`${metrics?.memory_utilization || 0}%`}
                          variant={metrics?.memory_utilization > 80 ? 'danger' : 
                                  metrics?.memory_utilization > 60 ? 'warning' : 'success'}
                          className="mb-3"
                        />
                        
                        <div className="d-flex justify-content-between text-muted small">
                          <span>Total Memory: {metrics?.total_memory ? formatBytes(metrics.total_memory) : 'N/A'}</span>
                          <span>Free Memory: {metrics?.free_memory ? formatBytes(metrics.free_memory) : 'N/A'}</span>
                        </div>
                      </Card.Body>
                    </Card>

                    <Card className="mb-4">
                      <Card.Header>Traffic Statistics</Card.Header>
                      <Card.Body>
                        <div className="mb-3">
                          <h6>Total Traffic (24h)</h6>
                          <div className="d-flex justify-content-between">
                            <div>
                              <div className="fw-bold text-success">
                                <i className="bi bi-arrow-down me-1"></i>
                                {metrics?.total_rx_24h ? formatBytes(metrics.total_rx_24h) : 'N/A'}
                              </div>
                              <div className="text-muted small">Received</div>
                            </div>
                            <div>
                              <div className="fw-bold text-danger">
                                <i className="bi bi-arrow-up me-1"></i>
                                {metrics?.total_tx_24h ? formatBytes(metrics.total_tx_24h) : 'N/A'}
                              </div>
                              <div className="text-muted small">Transmitted</div>
                            </div>
                          </div>
                        </div>
                        
                        <div>
                          <h6>Current Traffic Rate</h6>
                          <div className="d-flex justify-content-between">
                            <div>
                              <div className="fw-bold text-success">
                                <i className="bi bi-arrow-down me-1"></i>
                                {metrics?.current_rx_rate ? `${metrics.current_rx_rate} Mbps` : 'N/A'}
                              </div>
                              <div className="text-muted small">Receiving</div>
                            </div>
                            <div>
                              <div className="fw-bold text-danger">
                                <i className="bi bi-arrow-up me-1"></i>
                                {metrics?.current_tx_rate ? `${metrics.current_tx_rate} Mbps` : 'N/A'}
                              </div>
                              <div className="text-muted small">Transmitting</div>
                            </div>
                          </div>
                        </div>
                      </Card.Body>
                    </Card>

                    <Card className="mb-4">
                      <Card.Header>Port Summary</Card.Header>
                      <Card.Body>
                        <div className="d-flex justify-content-around text-center">
                          <div>
                            <div className="h3 text-success mb-0">
                              {metrics?.ports_up || '0'}
                            </div>
                            <div>Ports Up</div>
                          </div>
                          <div>
                            <div className="h3 text-danger mb-0">
                              {metrics?.ports_down || '0'}
                            </div>
                            <div>Ports Down</div>
                          </div>
                          <div>
                            <div className="h3 text-secondary mb-0">
                              {metrics?.ports_disabled || '0'}
                            </div>
                            <div>Disabled</div>
                          </div>
                          <div>
                            <div className="h3 mb-0">
                              {switchData?.total_ports || '0'}
                            </div>
                            <div>Total Ports</div>
                          </div>
                        </div>
                      </Card.Body>
                    </Card>
                  </Col>
                </Row>
              </Tab.Pane>

              {/* Ports Tab */}
              <Tab.Pane eventKey="ports">
                <Card>
                  <Card.Body>
                    {!metrics?.ports ? (
                      <Alert variant="info">
                        Port information is not available.
                      </Alert>
                    ) : (
                      <Table responsive hover>
                        <thead>
                          <tr>
                            <th>Port</th>
                            <th>Status</th>
                            <th>Speed</th>
                            <th>Duplex</th>
                            <th>VLAN</th>
                            <th>Description</th>
                            <th>Traffic (Rx/Tx)</th>
                            <th>Errors</th>
                          </tr>
                        </thead>
                        <tbody>
                          {Object.entries(metrics.ports).map(([portId, portData]) => (
                            <tr key={portId}>
                              <td>
                                <Link to={`/switches/${id}/ports/${portId}`}>
                                  {portData.name || portId}
                                </Link>
                              </td>
                              <td>{getPortStatusBadge(portData.status)}</td>
                              <td>{portData.speed || 'N/A'}</td>
                              <td>{portData.duplex || 'N/A'}</td>
                              <td>{portData.vlan || 'N/A'}</td>
                              <td>{portData.description || 'N/A'}</td>
                              <td>
                                <div className="small">
                                  <i className="bi bi-arrow-down text-success me-1"></i>
                                  {portData.rx_rate ? `${portData.rx_rate} Mbps` : 'N/A'}
                                </div>
                                <div className="small">
                                  <i className="bi bi-arrow-up text-danger me-1"></i>
                                  {portData.tx_rate ? `${portData.tx_rate} Mbps` : 'N/A'}
                                </div>
                              </td>
                              <td>{portData.errors || '0'}</td>
                            </tr>
                          ))}
                        </tbody>
                      </Table>
                    )}
                  </Card.Body>
                </Card>
              </Tab.Pane>

              {/* VLANs Tab */}
              <Tab.Pane eventKey="vlans">
                <Card>
                  <Card.Body>
                    {!metrics?.vlans ? (
                      <Alert variant="info">
                        VLAN information is not available.
                      </Alert>
                    ) : (
                      <Table responsive hover>
                        <thead>
                          <tr>
                            <th>VLAN ID</th>
                            <th>Name</th>
                            <th>Status</th>
                            <th>Associated Ports</th>
                          </tr>
                        </thead>
                        <tbody>
                          {Object.entries(metrics.vlans).map(([vlanId, vlanData]) => (
                            <tr key={vlanId}>
                              <td>{vlanId}</td>
                              <td>{vlanData.name || `VLAN ${vlanId}`}</td>
                              <td>
                                <Badge bg={vlanData.status === 'active' ? 'success' : 'secondary'}>
                                  {vlanData.status || 'Unknown'}
                                </Badge>
                              </td>
                              <td>{vlanData.ports?.join(', ') || 'None'}</td>
                            </tr>
                          ))}
                        </tbody>
                      </Table>
                    )}
                  </Card.Body>
                </Card>
              </Tab.Pane>

              {/* Configuration Tab */}
              <Tab.Pane eventKey="configuration">
                <Alert variant="info">
                  The configuration tab will display detailed switch configuration options
                  and allow for configuration changes once fully implemented.
                </Alert>
                
                <Card className="mb-3">
                  <Card.Header>Configuration Actions</Card.Header>
                  <Card.Body>
                    <Row>
                      <Col md={4} className="mb-3">
                        <Button variant="outline-primary" className="w-100">
                          <i className="bi bi-cloud-download me-2"></i>
                          Backup Configuration
                        </Button>
                      </Col>
                      <Col md={4} className="mb-3">
                        <Button variant="outline-primary" className="w-100">
                          <i className="bi bi-cloud-upload me-2"></i>
                          Restore Configuration
                        </Button>
                      </Col>
                      <Col md={4} className="mb-3">
                        <Button variant="outline-warning" className="w-100">
                          <i className="bi bi-arrow-repeat me-2"></i>
                          Reboot Switch
                        </Button>
                      </Col>
                    </Row>
                  </Card.Body>
                </Card>
              </Tab.Pane>

              {/* Logs Tab */}
              <Tab.Pane eventKey="logs">
                <Alert variant="info">
                  The logs tab will display switch system logs and event history
                  once fully implemented.
                </Alert>
                
                <Card>
                  <Card.Header className="d-flex justify-content-between align-items-center">
                    <span>System Logs</span>
                    <Button variant="outline-secondary" size="sm">
                      <i className="bi bi-download me-1"></i>
                      Export Logs
                    </Button>
                  </Card.Header>
                  <Card.Body>
                    <Alert variant="secondary">
                      Log data will be displayed here.
                    </Alert>
                  </Card.Body>
                </Card>
              </Tab.Pane>
            </Tab.Content>
          </Card.Body>
        </Card>
      </Tab.Container>
    </Container>
  );
};

export default SwitchDetail;
