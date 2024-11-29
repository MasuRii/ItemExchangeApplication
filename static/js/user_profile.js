document.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdownMenu');
    const userProfile = document.querySelector('.user-profile');

    // Check if the click happened inside the dropdown or on the user profile
    if (userProfile.contains(event.target)) {
        // Toggle the 'show' class
        dropdown.classList.toggle('show');
    } else {
        // Hide the dropdown if clicked outside
        dropdown.classList.remove('show');
    }
});