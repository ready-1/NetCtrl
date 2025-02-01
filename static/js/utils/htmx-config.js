// Configure HTMX to include CSRF token in all requests
document.addEventListener('DOMContentLoaded', function() {
  htmx.config.defaultSwapStyle = "innerHTML";
  htmx.config.defaultSettleDelay = 100;
  htmx.config.includeIndicatorStyles = false;
  htmx.config.timeout = 10000; // 10 second timeout

  // Add CSRF token to all HTMX requests
  document.body.addEventListener('htmx:configRequest', function(evt) {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    evt.detail.headers['X-CSRFToken'] = csrfToken;
  });

  // Show loading indicator during HTMX requests
  document.body.addEventListener('htmx:beforeRequest', function(evt) {
    document.body.classList.add('htmx-request');
  });

  document.body.addEventListener('htmx:afterRequest', function(evt) {
    document.body.classList.remove('htmx-request');
  });

  // Handle HTMX errors
  document.body.addEventListener('htmx:responseError', function(evt) {
    const alert = document.createElement('div');
    alert.className = 'alert alert-danger';
    alert.textContent = 'An error occurred while processing your request.';
    evt.detail.target.prepend(alert);
  });

  // Handle network errors
  document.body.addEventListener('htmx:sendError', function(evt) {
    const alert = document.createElement('div');
    alert.className = 'alert alert-danger';
    alert.textContent = 'A network error occurred. Please check your connection and try again.';
    evt.detail.target.prepend(alert);
  });

  // Handle request timeouts
  document.body.addEventListener('htmx:timeout', function(evt) {
    const alert = document.createElement('div');
    alert.className = 'alert alert-warning';
    alert.textContent = 'The request timed out. Please try again.';
    evt.detail.target.prepend(alert);
  });

  // Handle validation errors
  document.body.addEventListener('htmx:validation:failed', function(evt) {
    const form = evt.detail.target;
    form.classList.add('was-validated');
  });

  // Handle successful form submission
  document.body.addEventListener('htmx:afterOnLoad', function(evt) {
    if (evt.detail.successful && evt.detail.target.tagName === 'FORM') {
      evt.detail.target.reset();
      evt.detail.target.classList.remove('was-validated');
    }
  });

  // Handle WebSocket events
  document.body.addEventListener('htmx:wsOpen', function(evt) {
    console.log('WebSocket connection established');
  });

  document.body.addEventListener('htmx:wsClose', function(evt) {
    console.log('WebSocket connection closed');
  });

  document.body.addEventListener('htmx:wsError', function(evt) {
    console.error('WebSocket error:', evt.detail.error);
  });
});
