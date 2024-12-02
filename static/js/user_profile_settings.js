// user_profile_settings.js

function toggleDropdown(event) {
    // Stop the event from propagating to avoid unwanted closures
    event.stopPropagation();

    // Get the dropdown menu element
    var dropdownMenu = document.getElementById('dropdownMenu');

    // Toggle the 'show' class to either display or hide the dropdown
    dropdownMenu.classList.toggle('show');
}

// Close the dropdown when clicking anywhere outside of it
window.onclick = function(event) {
    var dropdownMenu = document.getElementById('dropdownMenu');

    // Check if the clicked element is not the dropdown or user-profile
    if (!event.target.closest('.user-profile')) {
        // If the dropdown is open, close it
        if (dropdownMenu.classList.contains('show')) {
            dropdownMenu.classList.remove('show');
        }
    }
};

document.addEventListener('DOMContentLoaded', function() {
    // Avatar upload preview
    const avatarInput = document.getElementById('avatar-input');
    if (avatarInput) {
        avatarInput.addEventListener('change', function() {
            const [file] = this.files;
            if (file) {
                const avatarImg = document.querySelector('.avatar');
                avatarImg.src = URL.createObjectURL(file);
            }
        });
    }

    // Delete Account functionality
    const deleteAccountBtn = document.getElementById('deleteAccountBtn');
    if (deleteAccountBtn) {
        deleteAccountBtn.addEventListener('click', function() {
            // First confirmation
            const firstConfirm = confirm("Are you sure you want to delete your account? This action cannot be undone.");
            if (firstConfirm) {
                // Second confirmation
                const secondConfirm = confirm("This is your last chance. Do you really want to delete your account permanently?");
                if (secondConfirm) {
                    // Submit the hidden form
                    const deleteAccountForm = document.getElementById('deleteAccountForm');
                    deleteAccountForm.submit();
                }
            }
        });
    }
});