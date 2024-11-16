// script.js
function controlPump(action) {
    fetch('/pumps', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ action })
    })
    .then(response => response.json())
    .then(data => {
        alert(`Pump ${data.action}ed successfully!`);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to perform the action. Try again!');
    });
}
