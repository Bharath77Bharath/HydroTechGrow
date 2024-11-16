// charts.js
document.addEventListener('DOMContentLoaded', function () {
    // Check if the canvas element exists
    const chartElement = document.getElementById('chart');
    if (chartElement) {
        const ctx = chartElement.getContext('2d');

        // Data for the chart
        const data = JSON.parse(chartElement.dataset.chart);

        // Create a new chart
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: data.label,
                    data: data.values,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        title: { display: true, text: 'Timestamp' }
                    },
                    y: {
                        title: { display: true, text: data.yAxisLabel }
                    }
                }
            }
        });
    }
});
