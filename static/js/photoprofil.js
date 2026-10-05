
const profilePhoto = document.getElementById('profilePhoto');
const profileImage = document.querySelector('.profile-photo img');

profilePhoto.addEventListener('change', function () {
    const file = this.files[0];

    if (file) {
        profileImage.src = URL.createObjectURL(file);
    }
});
