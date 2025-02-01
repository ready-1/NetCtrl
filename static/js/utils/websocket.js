// WebSocket Utilities

class WebSocketManager {
    constructor(path) {
        this.path = path;
        this.socket = null;
        this.reconnectAttempts = 0;
        this.maxReconnectAttempts = 5;
        this.listeners = new Map();

        // Initialize default handlers
        this.handleSwitchUpdate = this.handleSwitchUpdate.bind(this);
        this.handlePortUpdate = this.handlePortUpdate.bind(this);
        this.handleConfigUpdate = this.handleConfigUpdate.bind(this);
    }

    connect() {
        const wsScheme = window.location.protocol === 'https:' ? 'wss' : 'ws';
        const wsUrl = `${wsScheme}://${window.location.host}${this.path}`;

        this.socket = new WebSocket(wsUrl);

        this.socket.onopen = () => {
            console.log('WebSocket connected');
            this.reconnectAttempts = 0;
            this.emit('connected');
        };

        this.socket.onclose = () => {
            console.log('WebSocket disconnected');
            this.handleReconnect();
            this.emit('disconnected');
        };

        this.socket.onerror = (error) => {
            console.error('WebSocket error:', error);
            this.emit('error', error);
        };

        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.handleMessage(data);
        };
    }

    handleReconnect() {
        if (this.reconnectAttempts < this.maxReconnectAttempts) {
            this.reconnectAttempts++;
            console.log(`Attempting to reconnect (${this.reconnectAttempts}/${this.maxReconnectAttempts})`);
            setTimeout(() => this.connect(), 1000 * Math.pow(2, this.reconnectAttempts));
        } else {
            console.error('Max reconnection attempts reached');
            this.emit('maxReconnectAttemptsReached');
        }
    }

    handleMessage(data) {
        const { type, payload } = data;

        // Handle specific message types
        switch (type) {
            case 'switch_update':
                this.handleSwitchUpdate(payload);
                break;
            case 'port_update':
                this.handlePortUpdate(payload);
                break;
            case 'config_update':
                this.handleConfigUpdate(payload);
                break;
        }

        // Notify general listeners
        if (this.listeners.has(type)) {
            this.listeners.get(type).forEach(callback => callback(payload));
        }
    }

    handleSwitchUpdate(payload) {
        const { id, status, lastSeen } = payload;
        // Update switch status in UI
        const switchElement = document.querySelector(`[data-switch-id="${id}"]`);
        if (switchElement) {
            switchElement.querySelector('.switch-status').textContent = status;
            switchElement.querySelector('.switch-last-seen').textContent = lastSeen;
            switchElement.classList.toggle('switch-offline', status === 'offline');
        }
    }

    handlePortUpdate(payload) {
        const { switchId, portId, status, speed, errors } = payload;
        // Update port status in UI
        const portElement = document.querySelector(`[data-switch-id="${switchId}"][data-port-id="${portId}"]`);
        if (portElement) {
            portElement.querySelector('.port-status').textContent = status;
            portElement.querySelector('.port-speed').textContent = speed;
            portElement.querySelector('.port-errors').textContent = errors;
            portElement.classList.toggle('port-error', errors > 0);
        }
    }

    handleConfigUpdate(payload) {
        const { switchId, version, timestamp } = payload;
        // Update configuration version in UI
        const configElement = document.querySelector(`[data-switch-id="${switchId}"] .config-version`);
        if (configElement) {
            configElement.textContent = version;
            configElement.setAttribute('title', `Last updated: ${timestamp}`);
        }
    }

    addEventListener(type, callback) {
        if (!this.listeners.has(type)) {
            this.listeners.set(type, new Set());
        }
        this.listeners.get(type).add(callback);
    }

    removeEventListener(type, callback) {
        if (this.listeners.has(type)) {
            this.listeners.get(type).delete(callback);
        }
    }

    emit(type, payload = null) {
        if (this.listeners.has(type)) {
            this.listeners.get(type).forEach(callback => callback(payload));
        }
    }

    send(type, payload) {
        if (this.socket && this.socket.readyState === WebSocket.OPEN) {
            this.socket.send(JSON.stringify({ type, payload }));
        } else {
            console.error('WebSocket is not connected');
            this.emit('error', new Error('WebSocket is not connected'));
        }
    }

    disconnect() {
        if (this.socket) {
            this.socket.close();
        }
    }
}

// Export WebSocket manager
window.NetCtrlWebSocket = WebSocketManager;
