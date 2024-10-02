document.addEventListener('DOMContentLoaded', function() {

    // Get the popup elements and buttons by their IDs
    const popupOne = document.getElementById('PopupOne');
    const openPopupOneBtn = document.getElementById('openPopupOneBtn');
    const closePopupOneBtn = document.getElementById('closePopupOneBtn');

    const popupTwo = document.getElementById('PopupTwo');
    const openPopupTwoBtn = document.getElementById('openPopupTwoBtn');
    const closePopupTwoBtn = document.getElementById('closePopupTwoBtn');

    // Function to open the popup
    function openPopupById(popupId) {
        const popup = document.getElementById(popupId);
        if (popup) {
            popup.style.display = 'flex';
        }
    }

    // Function to close the popup
    function closePopupById(popupId) {
        const popup = document.getElementById(popupId);
        if (popup) {
            popup.style.display = 'none';
        }
    }

    // Event listeners to open and close the popups by ID
    openPopupOneBtn.addEventListener('click', () => openPopupById('PopupOne'));
    closePopupOneBtn.addEventListener('click', () => closePopupById('PopupOne'));

    openPopupTwoBtn.addEventListener('click', () => openPopupById('PopupTwo'));
    closePopupTwoBtn.addEventListener('click', () => closePopupById('PopupTwo'));

    // Close the popup when clicking outside the content
    window.addEventListener('click', (event) => {
        if (event.target === popupOne) {
            closePopupById('PopupOne');
        } else if (event.target === popupTwo) {
            closePopupById('PopupTwo');
        }
    });


    const videoContainer = document.querySelector('.video-container');
    const video = videoContainer.querySelector('video');
    const overlay = videoContainer.querySelector('.video-overlay');

    overlay.addEventListener('click', function() {
        overlay.classList.add('hidden');
        video.play();
    });

    video.addEventListener('play', function() {
        overlay.classList.add('hidden');
    });

    video.addEventListener('pause', function() {
        overlay.classList.remove('hidden');
    });

    

});
