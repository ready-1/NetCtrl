// NetCtrl Main JavaScript

// Loading spinner management
const loadingSpinner = {
    show() {
        document.getElementById('loading-spinner').classList.add('show');
    },
    hide() {
        document.getElementById('loading-spinner').classList.remove('show');
    }
};

// HTMX loading indicators
document.addEventListener('htmx:beforeRequest', function(event) {
    loadingSpinner.show();
});

document.addEventListener('htmx:afterRequest', function(event) {
    loadingSpinner.hide();
});

// Alert management
const alerts = {
    create(message, type = 'info', dismissible = true) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} ${dismissible ? 'alert-dismissible fade show' : ''}`;
        alertDiv.role = 'alert';

        alertDiv.innerHTML = `
            ${message}
            ${dismissible ? '<button type="button" class="btn-close" data-bs-dismiss="alert"></button>' : ''}
        `;

        document.querySelector('.messages').appendChild(alertDiv);

        if (dismissible) {
            setTimeout(() => {
                alertDiv.remove();
            }, 5000);
        }
    }
};

// Dark mode toggle
const darkMode = {
    toggle() {
        document.body.classList.toggle('light-mode');
        const isDark = !document.body.classList.contains('light-mode');
        localStorage.setItem('darkMode', isDark);
    },

    init() {
        const isDark = localStorage.getItem('darkMode') !== 'false';
        if (!isDark) {
            document.body.classList.add('light-mode');
        }
    }
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    darkMode.init();

    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

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
