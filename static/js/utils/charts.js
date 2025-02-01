// Chart.js Utilities

// Default chart configuration
const defaultChartConfig = {
    responsive: true,
    maintainAspectRatio: false,
    darkMode: true,
    interaction: {
        mode: 'index',
        intersect: false,
    },
    animation: {
        duration: 400,
        easing: 'easeOutQuart',
    },
    plugins: {
        legend: {
            labels: {
                color: '#e9ecef' // Light text for dark theme
            }
        }
    },
    scales: {
        x: {
            grid: {
                color: 'rgba(255, 255, 255, 0.1)' // Subtle grid lines
            },
            ticks: {
                color: '#e9ecef'
            }
        },
        y: {
            grid: {
                color: 'rgba(255, 255, 255, 0.1)'
            },
            ticks: {
                color: '#e9ecef'
            }
        }
    }
};

// Create a line chart for time series data
function createTimeSeriesChart(canvasId, data, options = {}) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    return new Chart(ctx, {
        type: 'line',
        data: data,
        options: { ...defaultChartConfig, ...options }
    });
}

// Create a bar chart
function createBarChart(canvasId, data, options = {}) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    return new Chart(ctx, {
        type: 'bar',
        data: data,
        options: { ...defaultChartConfig, ...options }
    });
}

// Update chart data
function updateChartData(chart, newData) {
    chart.data = newData;
    chart.update();
}

// Export utilities
window.NetCtrlCharts = {
    createTimeSeriesChart,
    createBarChart,
    updateChartData,
    defaultChartConfig
};
