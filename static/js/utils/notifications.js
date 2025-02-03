// Notification handling
document.addEventListener('DOMContentLoaded', function() {
    const notificationsList = document.querySelector('.notification-list');
    const unreadBadge = document.querySelector('#notifications-badge');

    // Function to mark a notification as read
    function markNotificationRead(notificationId) {
        fetch(`/core/notifications/mark-read/${notificationId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrf-token]').content
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                updateNotifications();
            }
        });
    }

    // Function to mark all notifications as read
    function markAllNotificationsRead() {
        fetch('/core/notifications/mark-all-read/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrf-token]').content
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                updateNotifications();
            }
        });
    }

    // Function to update notifications list
    function updateNotifications() {
        fetch('/core/notifications/')
        .then(response => response.json())
        .then(data => {
            // Update notifications list
            if (notificationsList) {
                notificationsList.innerHTML = '';
                if (data.notifications.length === 0) {
                    notificationsList.innerHTML = '<span class="dropdown-item">No new notifications</span>';
                } else {
                    data.notifications.forEach(notification => {
                        const item = document.createElement('a');
                        item.href = notification.url || '#';
                        item.className = 'dropdown-item' + (notification.read ? ' read' : '');
                        item.innerHTML = `
                            <div class="d-flex align-items-center">
                                <i class="bi bi-${getNotificationIcon(notification.type)} me-2"></i>
                                <div>
                                    <div class="notification-message">${notification.message}</div>
                                    <small class="text-muted">${formatDate(notification.created_at)}</small>
                                </div>
                            </div>
                        `;
                        item.addEventListener('click', () => markNotificationRead(notification.id));
                        notificationsList.appendChild(item);
                    });
                }
            }

            // Update unread count badge
            if (unreadBadge) {
                const unreadCount = data.notifications.filter(n => !n.read).length;
                unreadBadge.textContent = unreadCount;
                unreadBadge.style.display = unreadCount > 0 ? 'block' : 'none';
            }
        });
    }

    // Helper function to get appropriate icon for notification type
    function getNotificationIcon(type) {
        switch (type) {
            case 'success': return 'check-circle-fill';
            case 'warning': return 'exclamation-triangle-fill';
            case 'error': return 'x-circle-fill';
            default: return 'info-circle-fill';
        }
    }

    // Helper function to format date
    function formatDate(isoString) {
        const date = new Date(isoString);
        return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
    }

    // Update notifications every minute
    updateNotifications();
    setInterval(updateNotifications, 60000);

    // Add click handler for "Mark all as read"
    const markAllReadBtn = document.querySelector('#mark-all-notifications-read');
    if (markAllReadBtn) {
        markAllReadBtn.addEventListener('click', markAllNotificationsRead);
    }
});
