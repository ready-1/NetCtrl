// Switch status polling
console.log('=== Switch Status Script Loaded ===');
console.log('Script version: 1.0.0');
console.log('Initializing status polling...');

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM Content Loaded - Starting switch status monitoring');

    // Get CSRF token from global variable
    const csrfToken = window.CSRF_TOKEN;
    console.log('CSRF token found:', csrfToken ? 'Yes' : 'No');

    // Function to fetch switch status
    async function fetchSwitchStatus() {
        try {
            console.log('Fetching switch status...');
            const response = await fetch('/switches/api/status/', {
                method: 'GET',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                credentials: 'include'
            });
            console.log('Status response:', response.status, response.statusText);

            if (response.status === 401) {
                console.error('Authentication required - redirecting to login');
                window.location.href = '/auth/login/?next=' + encodeURIComponent(window.location.pathname);
                return;
            }

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const contentType = response.headers.get('content-type');
            if (!contentType || !contentType.includes('application/json')) {
                throw new Error(`Expected JSON response but got ${contentType}`);
            }

            const switches = await response.json();
            console.log('Received switch data:', switches);

            if (!Array.isArray(switches)) {
                throw new Error('Expected array of switches but got: ' + typeof switches);
            }

            switches.forEach(data => {
                console.log(`Updating switch ${data.id}:`, data);
                updateSwitchStatus(data.id, {
                    status: data.status,
                    in_band: {
                        status: data.in_band_status,
                        last_seen: data.in_band_last_seen,
                        error: data.in_band_error,
                        error_detail: data.in_band_error_detail,
                        response_time: data.in_band_response_time
                    },
                    out_band: {
                        status: data.out_band_status,
                        last_seen: data.out_band_last_seen,
                        error: data.out_band_error,
                        error_detail: data.out_band_error_detail,
                        response_time: data.out_band_response_time
                    }
                });
            });
        } catch (error) {
            console.error('Error fetching switch status:', error);
            if (error.name === 'TypeError' && error.message.includes('Failed to fetch')) {
                console.error('Network error - server might be down');
            }
        }
    }

    // Update switch status in the UI
    function updateSwitchStatus(switchId, data) {
        const card = document.querySelector(`[data-switch-id="${switchId}"]`);
        if (!card) {
            console.warn(`Switch card not found for ID: ${switchId}`);
            return;
        }

        console.log(`Updating UI for switch ${switchId}:`, data);

        // Update status badge
        const statusBadge = card.querySelector('.status-badge .badge');
        if (statusBadge) {
            const oldClass = statusBadge.className;
            statusBadge.className = 'badge ' + getStatusClass(data.status);
            statusBadge.textContent = data.status.charAt(0).toUpperCase() + data.status.slice(1);
            console.log(`Updated status badge: ${oldClass} -> ${statusBadge.className}`);
        }

        // Update last seen timestamps and error details
        const lastSeenText = card.querySelector('.status-badge small');
        if (lastSeenText) {
            const inBandError = data.in_band.error !== 'none' ?
                `(${data.in_band.error_detail})` :
                data.in_band.response_time ?
                    `(${data.in_band.response_time.toFixed(1)}ms)` : '';

            const outBandError = data.out_band.error !== 'none' ?
                `(${data.out_band.error_detail})` :
                data.out_band.response_time ?
                    `(${data.out_band.response_time.toFixed(1)}ms)` : '';

            const newText = `
                In-Band: ${formatLastSeen(data.in_band.last_seen)} ${inBandError}<br>
                Out-Band: ${formatLastSeen(data.out_band.last_seen)} ${outBandError}
            `;
            lastSeenText.innerHTML = newText;
            console.log('Updated last seen text:', newText);
        }

        // Update in-band button
        const inBandBtn = card.querySelector('a[href*="in_band"]');
        if (inBandBtn) {
            const wasEnabled = !inBandBtn.classList.contains('disabled');
            const shouldBeEnabled = data.in_band.status !== 'down';
            if (wasEnabled !== shouldBeEnabled) {
                console.log(`Updating in-band button state: ${wasEnabled} -> ${shouldBeEnabled}`);
                updateButtonState(inBandBtn, shouldBeEnabled, data.in_band.status);
            }
            // Update tooltip
            let tooltip = `In-Band Interface`;
            if (data.in_band.error !== 'none') {
                tooltip += ` - ${data.in_band.error_detail}`;
            } else if (data.in_band.response_time) {
                tooltip += ` - Response time: ${data.in_band.response_time.toFixed(1)}ms`;
            }
            inBandBtn.title = tooltip;
        }

        // Update out-band button
        const outBandBtn = card.querySelector('a[href*="out_band"]');
        if (outBandBtn) {
            const wasEnabled = !outBandBtn.classList.contains('disabled');
            const shouldBeEnabled = data.out_band.status !== 'down';
            if (wasEnabled !== shouldBeEnabled) {
                console.log(`Updating out-band button state: ${wasEnabled} -> ${shouldBeEnabled}`);
                updateButtonState(outBandBtn, shouldBeEnabled, data.out_band.status);
            }
            // Update tooltip
            let tooltip = `Out-Band Interface`;
            if (data.out_band.error !== 'none') {
                tooltip += ` - ${data.out_band.error_detail}`;
            } else if (data.out_band.response_time) {
                tooltip += ` - Response time: ${data.out_band.response_time.toFixed(1)}ms`;
            }
            outBandBtn.title = tooltip;
        }

        // Update modal if open
        const modal = document.getElementById(`statusModal${switchId}`);
        if (modal && modal.classList.contains('show')) {
            console.log('Updating modal for switch:', switchId);
            updateStatusModal(modal, data);
        }
    }

    // Update button state
    function updateButtonState(button, isEnabled, status) {
        if (!isEnabled) {
            button.classList.add('disabled');
            button.classList.remove('nc-btn-primary', 'nc-btn-warning');
            button.classList.add('nc-btn-secondary');
        } else {
            button.classList.remove('disabled');
            if (status === 'up') {
                button.classList.remove('nc-btn-secondary', 'nc-btn-warning');
                button.classList.add('nc-btn-primary');
            } else {
                // Degraded status
                button.classList.remove('nc-btn-secondary', 'nc-btn-primary');
                button.classList.add('nc-btn-warning');
            }
        }
    }

    // Update status modal content
    function updateStatusModal(modal, data) {
        // Update in-band status
        const inBandStatus = modal.querySelector('.in-band-status');
        if (inBandStatus) {
            inBandStatus.className = 'badge in-band-status ' + getStatusClass(data.in_band.status);
            inBandStatus.textContent = data.in_band.status.charAt(0).toUpperCase() + data.in_band.status.slice(1);
            if (data.in_band.error !== 'none') {
                inBandStatus.title = data.in_band.error_detail;
            } else if (data.in_band.response_time) {
                inBandStatus.title = `Response time: ${data.in_band.response_time.toFixed(1)}ms`;
            }
        }

        // Update out-band status
        const outBandStatus = modal.querySelector('.out-band-status');
        if (outBandStatus) {
            outBandStatus.className = 'badge out-band-status ' + getStatusClass(data.out_band.status);
            outBandStatus.textContent = data.out_band.status.charAt(0).toUpperCase() + data.out_band.status.slice(1);
            if (data.out_band.error !== 'none') {
                outBandStatus.title = data.out_band.error_detail;
            } else if (data.out_band.response_time) {
                outBandStatus.title = `Response time: ${data.out_band.response_time.toFixed(1)}ms`;
            }
        }

        // Update timestamps
        const inBandLastSeen = modal.querySelector('.in-band-last-seen');
        if (inBandLastSeen) {
            let text = formatLastSeen(data.in_band.last_seen);
            if (data.in_band.error !== 'none') {
                text += ` (${data.in_band.error_detail})`;
            } else if (data.in_band.response_time) {
                text += ` (${data.in_band.response_time.toFixed(1)}ms)`;
            }
            inBandLastSeen.textContent = text;
        }

        const outBandLastSeen = modal.querySelector('.out-band-last-seen');
        if (outBandLastSeen) {
            let text = formatLastSeen(data.out_band.last_seen);
            if (data.out_band.error !== 'none') {
                text += ` (${data.out_band.error_detail})`;
            } else if (data.out_band.response_time) {
                text += ` (${data.out_band.response_time.toFixed(1)}ms)`;
            }
            outBandLastSeen.textContent = text;
        }
    }

    // Format last seen timestamp
    function formatLastSeen(timestamp) {
        if (!timestamp) return 'Never';
        const date = new Date(timestamp);
        const now = new Date();
        const diff = Math.floor((now - date) / 1000); // difference in seconds

        if (diff < 60) {
            return `${diff} seconds ago`;
        } else if (diff < 3600) {
            const minutes = Math.floor(diff / 60);
            return `${minutes} minute${minutes === 1 ? '' : 's'} ago`;
        } else if (diff < 86400) {
            const hours = Math.floor(diff / 3600);
            return `${hours} hour${hours === 1 ? '' : 's'} ago`;
        } else {
            const days = Math.floor(diff / 86400);
            return `${days} day${days === 1 ? '' : 's'} ago`;
        }
    }

    // Get appropriate status class
    function getStatusClass(status) {
        switch (status) {
            case 'up':
                return 'bg-success';
            case 'down':
                return 'bg-danger';
            default:
                return 'bg-warning';
        }
    }

    // Start polling
    console.log('Starting switch status polling...');
    fetchSwitchStatus(); // Initial fetch
    setInterval(fetchSwitchStatus, 5000); // Poll every 5 seconds
});
