// Function to toggle the dropdown visibility
function toggleDropdown() {
    const dropdown = document.getElementById('dropdownMenu');
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
}

const gridContainer = document.querySelector('.grid-container');

function updateScrolling() {
    const items = gridContainer.querySelectorAll('.product-card').length; // Count grid items
    if (items > 12) {
        gridContainer.classList.add('scrollable'); // Enable scrolling
    } else {
        gridContainer.classList.remove('scrollable'); // Disable scrolling
    }
}

// Call the function on page load
updateScrolling();

function addProductCard() {
    const newCard = document.createElement('div');
    newCard.classList.add('product-card');
    newCard.innerHTML = '<p>New Product</p>';
    gridContainer.appendChild(newCard);

    updateScrolling(); // Re-check scrolling
}

// Functions to handle Add Item modal
function openAddItemModal() {
    document.getElementById('addItemModal').style.display = 'block';
}

function closeAddItemModal() {
    document.getElementById('addItemModal').style.display = 'none';
}

// Close the modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById('addItemModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Run updateScrolling when the page content is loaded
document.addEventListener('DOMContentLoaded', function() {
    updateScrolling();
});

document.addEventListener('DOMContentLoaded', function() {
    const ratingForm = document.getElementById('ratingForm');
    const stars = document.querySelectorAll('.star-rating input[type="radio"]');
    const csrfToken = ratingForm.querySelector('input[name="csrfmiddlewaretoken"]').value;

    stars.forEach(function(star) {
        star.addEventListener('change', function() {
            const ratingValue = this.value;
            fetch('', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: new URLSearchParams({
                    'rating': ratingValue,
                    'csrfmiddlewaretoken': csrfToken
                })
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Network response was not ok');
                }
            })
            .then(data => {
                if (data.status === 'success') {
                    alert(data.message);
                    // Optionally update the average rating display
                    location.reload(); // Reload the page to update the average rating
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                alert('An error occurred. Please try again.');
                console.error('Error:', error);
            });
        });
    });
});