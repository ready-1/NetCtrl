// WebSocket connection for switch status updates
document.addEventListener('DOMContentLoaded', function() {
    // Create WebSocket connection
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const socket = new WebSocket(
        `${protocol}//${window.location.host}/ws/switch-status/`
    );

    socket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        if (data.type === 'switch.status_update') {
            updateSwitchStatus(data.switch_id, data.data);
        }
    };

    socket.onclose = function(event) {
        console.log('WebSocket connection closed');
        // Attempt to reconnect after 5 seconds
        setTimeout(function() {
            window.location.reload();
        }, 5000);
    };

    // Update switch status in the UI
    function updateSwitchStatus(switchId, data) {
        // Find the switch card
        const card = document.querySelector(`[data-switch-id="${switchId}"]`);
        if (!card) return;

        // Update overall status badge
        const statusBadge = card.querySelector('.status-badge');
        if (statusBadge) {
            statusBadge.className = 'badge ' + getStatusClass(data.overall_status);
            statusBadge.textContent = data.overall_status.charAt(0).toUpperCase() + data.overall_status.slice(1);
        }

        // Update in-band button
        const inBandBtn = card.querySelector('.in-band-btn');
        if (inBandBtn) {
            updateInterfaceButton(inBandBtn, data.in_band);
        }

        // Update out-band button
        const outBandBtn = card.querySelector('.out-band-btn');
        if (outBandBtn) {
            updateInterfaceButton(outBandBtn, data.out_band);
        }

        // Update status modal if open
        const modal = document.getElementById(`statusModal${switchId}`);
        if (modal && modal.classList.contains('show')) {
            updateStatusModal(modal, data);
        }
    }

    // Update interface button status and timestamp
    function updateInterfaceButton(button, data) {
        // Update button state
        if (data.status === 'up') {
            button.classList.remove('btn-secondary', 'disabled');
            button.classList.add('btn-primary');
        } else {
            button.classList.remove('btn-primary');
            button.classList.add('btn-secondary', 'disabled');
        }

        // Update timestamp
        const timestamp = button.querySelector('small');
        if (timestamp && data.last_seen) {
            const lastSeen = new Date(data.last_seen);
            const now = new Date();
            const diff = Math.floor((now - lastSeen) / 1000); // difference in seconds

            let timeAgo;
            if (diff < 60) {
                timeAgo = `${diff} seconds ago`;
            } else if (diff < 3600) {
                timeAgo = `${Math.floor(diff / 60)} minutes ago`;
            } else {
                timeAgo = `${Math.floor(diff / 3600)} hours ago`;
            }

            timestamp.textContent = timeAgo;
        }
    }

    // Update status modal content
    function updateStatusModal(modal, data) {
        // Update status badges
        const inBandBadge = modal.querySelector('.in-band-status');
        if (inBandBadge) {
            inBandBadge.className = 'badge ' + getStatusClass(data.in_band.status);
            inBandBadge.textContent = data.in_band.status.charAt(0).toUpperCase() + data.in_band.status.slice(1);
        }

        const outBandBadge = modal.querySelector('.out-band-status');
        if (outBandBadge) {
            outBandBadge.className = 'badge ' + getStatusClass(data.out_band.status);
            outBandBadge.textContent = data.out_band.status.charAt(0).toUpperCase() + data.out_band.status.slice(1);
        }

        // Update timestamps
        updateModalTimestamp(modal, '.in-band-last-seen', data.in_band.last_seen);
        updateModalTimestamp(modal, '.out-band-last-seen', data.out_band.last_seen);
    }

    // Update timestamp in modal
    function updateModalTimestamp(modal, selector, timestamp) {
        const element = modal.querySelector(selector);
        if (element && timestamp) {
            const date = new Date(timestamp);
            element.textContent = date.toLocaleString();
        }
    }

    // Get appropriate Bootstrap status class
    function getStatusClass(status) {
        switch (status) {
            case 'up':
                return 'bg-success';
            case 'down':
                return 'bg-danger';
            case 'degraded':
                return 'bg-warning';
            default:
                return 'bg-secondary';
        }
    }
});
