document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('paymentForm');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting the default way
        window.location.href = 'payment_successful.html'; // Redirect to the duplicate_request.html page
    });

    // Function to generate QR code
    function generateQRCode() {
        const username = document.getElementById('username').value;
        const upiId = document.getElementById('upiId').value;
        const amount = document.getElementById('amount').value;

        const qr = qrcode(0, 'L');
        qr.addData(`upi://pay?pa=${upiId}&pn=${username}&mc=&tid=&msg=&amount=${amount}&cu=INR&url=`);
        qr.make();
        
        document.getElementById('qrcode').innerHTML = qr.createImgTag();
    }

    // Generate QR code when input fields change
    document.getElementById('username').addEventListener('input', generateQRCode);
    document.getElementById('upiId').addEventListener('input', generateQRCode);
    document.getElementById('amount').addEventListener('input', generateQRCode);

    // Initial QR code generation
    generateQRCode();
});
// script.js
document.getElementById('paymentForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileUpload');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        fetch('/send-email/', {  // Replace with your actual endpoint
            method: 'POST',
            body: formData,
        })
        .then(response => response.text())
        .then(result => {
            alert('Your request has been sent!');
            // Redirect or show a success message
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error sending your request.');
        });
    } else {
        alert('Please upload a file.');
    }
});
const menuToggle = document.getElementById('menu-toggle');
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('overlay');

menuToggle.addEventListener('click', () => {
    sidebar.style.left = sidebar.style.left === '0px' ? '-250px' : '0px';
    overlay.style.display = overlay.style.display === 'block' ? 'none' : 'block';
});

overlay.addEventListener('click', () => {
    sidebar.style.left = '-250px';
    overlay.style.display = 'none';
});