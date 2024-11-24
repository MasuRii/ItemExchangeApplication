// User Profile Settings JavaScript

// Preview the uploaded avatar image
document.getElementById('avatar-input').addEventListener('change', function() {
    const [file] = this.files;
    if (file) {
        const avatarImg = document.querySelector('.avatar');
        avatarImg.src = URL.createObjectURL(file);
    }
});