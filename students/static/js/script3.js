function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar.style.left === '0px') {
        sidebar.style.left = '-200px';
    } else {
        sidebar.style.left = '0px';
    }
}
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // You can add any form validation or processing logic here

    // Redirect to view_requests.html
    window.location.href = 'view_requests.html';
});
