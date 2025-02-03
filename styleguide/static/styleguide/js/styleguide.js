// Theme Management
class ThemeManager {
    constructor() {
        this.darkModeToggle = document.getElementById('darkModeToggle');
        this.init();
    }

    init() {
        // Check initial theme
        if (localStorage.getItem('darkMode') === 'enabled') {
            document.body.classList.add('dark-mode');
            this.darkModeToggle.checked = true;
        }

        // Listen for theme changes
        this.darkModeToggle.addEventListener('change', () => this.toggleTheme());

        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
            if (localStorage.getItem('darkMode') === null) {
                this.setTheme(e.matches);
            }
        });
    }

    toggleTheme() {
        const isDarkMode = this.darkModeToggle.checked;
        this.setTheme(isDarkMode);
        localStorage.setItem('darkMode', isDarkMode ? 'enabled' : null);
    }

    setTheme(isDarkMode) {
        document.body.classList.toggle('dark-mode', isDarkMode);
        this.darkModeToggle.checked = isDarkMode;

        // Update charts if they exist
        if (window.charts) {
            Object.values(window.charts).forEach(chart => {
                chart.options.plugins.legend.labels.color = isDarkMode ? '#e0e0e0' : '#666';
                chart.options.scales.x.grid.color = isDarkMode ? '#404040' : '#ddd';
                chart.options.scales.y.grid.color = isDarkMode ? '#404040' : '#ddd';
                chart.update();
            });
        }
    }
}

// Code Snippet Management
class CodeSnippetManager {
    constructor() {
        this.snippets = document.querySelectorAll('.code-snippet');
        this.init();
    }

    init() {
        this.snippets.forEach(snippet => {
            const copyButton = document.createElement('button');
            copyButton.className = 'btn btn-sm btn-secondary float-end';
            copyButton.innerHTML = '<i class="fas fa-copy"></i> Copy';
            copyButton.addEventListener('click', () => this.copyCode(snippet));

            const header = document.createElement('div');
            header.className = 'code-snippet-header';
            header.appendChild(copyButton);

            snippet.insertBefore(header, snippet.firstChild);
        });
    }

    async copyCode(snippet) {
        const code = snippet.querySelector('code').textContent;
        try {
            await navigator.clipboard.writeText(code);
            this.showToast('Code copied to clipboard!');
        } catch (err) {
            this.showToast('Failed to copy code', 'error');
        }
    }

    showToast(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white bg-${type === 'success' ? 'success' : 'danger'} border-0`;
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');

        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        `;

        document.body.appendChild(toast);
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();

        toast.addEventListener('hidden.bs.toast', () => {
            toast.remove();
        });
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ThemeManager();
    new CodeSnippetManager();

    // Initialize syntax highlighting if Prism.js is available
    if (window.Prism) {
        Prism.highlightAll();
    }
});
