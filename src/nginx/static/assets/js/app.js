// NetCtrl CMS with RBAC - Main JavaScript File

document.addEventListener('DOMContentLoaded', function() {
  // Update the current time
  updateDateTime();
  
  // Initialize any interactive elements
  initializeComponents();
  
  // Set up periodic time updates
  setInterval(updateDateTime, 1000);
});

/**
 * Updates the current date and time display
 */
function updateDateTime() {
  const timeElement = document.getElementById('current-time');
  if (timeElement) {
    const now = new Date();
    timeElement.textContent = now.toLocaleString();
  }
}

/**
 * Initializes interactive components on the page
 */
function initializeComponents() {
  // Set up buttons
  const buttons = document.querySelectorAll('.button');
  buttons.forEach(button => {
    button.addEventListener('click', handleButtonClick);
  });
  
  // Set up service status checks if on index page
  if (document.getElementById('service-status-container')) {
    checkServiceStatus();
  }
}

/**
 * Handle button clicks based on data attributes
 */
function handleButtonClick(event) {
  const button = event.currentTarget;
  const action = button.getAttribute('data-action');
  
  if (action === 'home') {
    window.location.href = '/';
  } else if (action === 'docs') {
    window.location.href = '/docs';
  } else if (action === 'refresh') {
    window.location.reload();
  } else if (action === 'back') {
    window.history.back();
  }
}

/**
 * Check the status of services
 * This is a mock implementation that would be replaced with real status checks
 */
function checkServiceStatus() {
  const statusElements = {
    backend: document.getElementById('backend-status'),
    database: document.getElementById('database-status'),
    frontend: document.getElementById('frontend-status'),
    nginx: document.getElementById('nginx-status')
  };
  
  // For demo purposes, we'll simulate backend and database as online
  // In a real implementation, this would make API calls to health check endpoints
  if (statusElements.backend) {
    updateStatusElement(statusElements.backend, 'online');
  }
  
  if (statusElements.database) {
    updateStatusElement(statusElements.database, 'online');
  }
  
  if (statusElements.frontend) {
    updateStatusElement(statusElements.frontend, 'online');
  }
  
  if (statusElements.nginx) {
    updateStatusElement(statusElements.nginx, 'online');
  }
}

/**
 * Update a service status element
 */
function updateStatusElement(element, status) {
  // Clear existing status classes
  element.classList.remove('chip-success', 'chip-error', 'chip-warning');
  
  if (status === 'online') {
    element.classList.add('chip-success');
    element.textContent = 'Online';
  } else if (status === 'offline') {
    element.classList.add('chip-error');
    element.textContent = 'Offline';
  } else if (status === 'degraded') {
    element.classList.add('chip-warning');
    element.textContent = 'Degraded';
  } else {
    element.classList.add('chip-info');
    element.textContent = 'Unknown';
  }
}

/**
 * Get service version information
 * This is a mock implementation
 */
function getVersionInfo() {
  return {
    system: 'NetCtrl CMS with RBAC',
    version: '1.0.0',
    environment: 'Development'
  };
}
