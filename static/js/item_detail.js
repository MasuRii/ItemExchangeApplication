// Function to toggle the dropdown visibility
function toggleDropdown() {
    const dropdown = document.getElementById('dropdownMenu');
    dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
}

// Close the dropdown if the user clicks anywhere outside the user profile
document.addEventListener('click', function(event) {
    const profile = document.querySelector('.user-profile');
    const dropdown = document.getElementById('dropdownMenu');
    if (!profile.contains(event.target)) {
        dropdown.style.display = 'none';
    }
});

// Function to open the modal
function openModal() {
    document.getElementById('editItemModal').style.display = 'block';
}

// Function to close the modal
function closeModal() {
    document.getElementById('editItemModal').style.display = 'none';
}

document.addEventListener("DOMContentLoaded", function() {
    // Get the value of the data-form-errors attribute
    const hasFormErrors = document.body.getAttribute('data-form-errors') === 'true';
  
    // If there are form errors, call the openModal function
    if (hasFormErrors) {
      openModal(); // Ensure this function is defined elsewhere
    }
  });

// Close the modal when clicking outside of the modal content
window.onclick = function(event) {
    var modal = document.getElementById('editItemModal');
    if (event.target == modal) {
      closeModal();
    }
  }