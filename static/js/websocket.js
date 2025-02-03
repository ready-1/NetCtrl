class WebSocketClient {
    constructor(path) {
        this.connect(path);
        this.reconnectAttempts = 0;
        this.maxReconnectAttempts = 5;
        this.reconnectDelay = 1000; // Start with 1 second
    }

    connect(path) {
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsUrl = `${protocol}//${window.location.host}${path}`;

        this.ws = new WebSocket(wsUrl);

        this.ws.onopen = () => {
            console.log('WebSocket connected');
            this.reconnectAttempts = 0;
            this.reconnectDelay = 1000;
        };

        this.ws.onclose = (e) => {
            console.log('WebSocket disconnected');
            if (this.reconnectAttempts < this.maxReconnectAttempts) {
                setTimeout(() => {
                    this.reconnectAttempts++;
                    this.reconnectDelay *= 2; // Exponential backoff
                    this.connect(path);
                }, this.reconnectDelay);
            }
        };

        this.ws.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        this.ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.handleMessage(data);
        };
    }

    handleMessage(data) {
        if (data.type === 'notification') {
            this.showNotification(data);
        }
    }

    showNotification(data) {
        const { message, notification_type = 'info' } = data;

        // Create notification element
        const notification = document.createElement('div');
        notification.className = `alert alert-${notification_type} alert-dismissible fade show`;
        notification.role = 'alert';

        notification.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;

        // Add to notification container
        const container = document.getElementById('notification-container');
        if (container) {
            container.appendChild(notification);

            // Auto-dismiss after 5 seconds
            setTimeout(() => {
                notification.classList.remove('show');
                setTimeout(() => notification.remove(), 150);
            }, 5000);
        }
    }

    send(data) {
        if (this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify(data));
        }
    }

    close() {
        if (this.ws) {
            this.ws.close();
        }
    }
}

// Initialize WebSocket connection for notifications
document.addEventListener('DOMContentLoaded', () => {
    if (document.body.dataset.userAuthenticated === 'true') {
        window.notificationSocket = new WebSocketClient('/ws/notifications/');
    }
});
