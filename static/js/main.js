// NetCtrl Main JavaScript

// HTMX CSRF Token Setup
document.addEventListener('DOMContentLoaded', function() {
    document.body.addEventListener('htmx:configRequest', function(evt) {
        evt.detail.headers['X-CSRFToken'] = document.querySelector('[name=csrfmiddlewaretoken]').value;
    });
});

// Real-time Status Updates
class StatusMonitor {
    constructor(updateInterval = 5000) {
        this.updateInterval = updateInterval;
        this.socket = null;
    }

    connect() {
        this.socket = new WebSocket(
            `${window.location.protocol === 'https:' ? 'wss:' : 'ws:'}//${window.location.host}/ws/status/`
        );

        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.updateStatus(data);
        };

        this.socket.onclose = () => {
            // Reconnect after 5 seconds
            setTimeout(() => this.connect(), 5000);
        };
    }

    updateStatus(data) {
        // Update status indicators
        const statusElements = document.querySelectorAll('[data-switch-status]');
        statusElements.forEach(element => {
            const switchId = element.dataset.switchStatus;
            if (data.switches && data.switches[switchId]) {
                element.textContent = data.switches[switchId].status;
                element.className = `status-indicator ${data.switches[switchId].status.toLowerCase()}`;
            }
        });
    }
}

// Initialize status monitor when needed
window.statusMonitor = new StatusMonitor();

// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.navbar-toggler');
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            const target = document.querySelector(this.dataset.target);
            if (target) {
                target.classList.toggle('show');
            }
        });
    }
});
