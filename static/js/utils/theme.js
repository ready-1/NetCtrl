/**
 * Theme management utilities for NetCtrl.
 * Handles dark/light theme toggling and persistence.
 */

// Theme constants
const THEME_STORAGE_KEY = 'nc-theme-preference';
const DARK_THEME_CLASS = 'nc-dark-theme';

/**
 * Toggle between dark and light theme.
 */
function toggleDarkTheme() {
    const isDark = document.documentElement.classList.contains(DARK_THEME_CLASS);
    setThemePreference(!isDark);
}

/**
 * Set theme preference and apply it.
 * @param {boolean} isDark - Whether to use dark theme.
 */
function setThemePreference(isDark) {
    localStorage.setItem(THEME_STORAGE_KEY, isDark ? 'dark' : 'light');
    applyTheme(isDark);
}

/**
 * Get current theme preference.
 * @returns {boolean} True if dark theme is preferred.
 */
function getThemePreference() {
    // Check localStorage
    const stored = localStorage.getItem(THEME_STORAGE_KEY);
    if (stored) {
        return stored === 'dark';
    }

    // Check system preference
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
}

/**
 * Apply theme to document.
 * @param {boolean} isDark - Whether to apply dark theme.
 */
function applyTheme(isDark) {
    if (isDark) {
        document.documentElement.classList.add(DARK_THEME_CLASS);
    } else {
        document.documentElement.classList.remove(DARK_THEME_CLASS);
    }

    // Update Chart.js themes if any charts exist
    if (window.Chart) {
        Chart.defaults.theme = isDark ? 'dark' : 'light';
        // Update existing charts
        Chart.instances.forEach(chart => {
            chart.update();
        });
    }
}

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', () => {
    applyTheme(getThemePreference());

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (!localStorage.getItem(THEME_STORAGE_KEY)) {
            applyTheme(e.matches);
        }
    });
});
