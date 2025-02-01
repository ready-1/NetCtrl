// HTMX Configuration
document.addEventListener('DOMContentLoaded', () => {
    // Add CSRF token to all HTMX requests
    document.body.addEventListener('htmx:configRequest', (event) => {
        event.detail.headers['X-CSRFToken'] = document.querySelector('[name=csrfmiddlewaretoken]').value;
    });

    // Handle HTMX errors
    document.body.addEventListener('htmx:responseError', (event) => {
        console.error('HTMX Error:', event.detail.error);
        // Show error message to user (using our alerts component)
        const alertsContainer = document.getElementById('alerts-container');
        if (alertsContainer) {
            const alert = document.createElement('div');
            alert.className = 'alert alert-danger alert-dismissible fade show';
            alert.innerHTML = `
                <strong>Error!</strong> An error occurred while processing your request.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            `;
            alertsContainer.appendChild(alert);
        }
    });
});
