document.addEventListener("DOMContentLoaded", function () {
    function adjustFloatingContainer() {
        const footer = document.querySelector('footer');
        const floatingContainer = document.querySelector('.floating-container');

        if (footer && floatingContainer) {
            const footerRect = footer.getBoundingClientRect(); // Get the footer's position relative to the viewport
            const viewportHeight = window.innerHeight; // Get the viewport height

            // Determine the position based on footer visibility
            if (footerRect.top < viewportHeight && footerRect.bottom > 0) { // Check if footer is visible
                // Position the floating container 20px above the footer
                floatingContainer.style.bottom = `${footerRect.height + 20}px`; // 20px above the footer
            } else {
                // Position at 20px from the bottom of the viewport
                floatingContainer.style.bottom = '20px'; 
            }
        } else {
            // Default to 20px from the bottom if no footer is found
            floatingContainer.style.bottom = '20px';
        }

        // Always align to the right
        floatingContainer.style.right = '20px';
    }

    // Call the function on load and on window resize
    adjustFloatingContainer();
    window.onresize = adjustFloatingContainer;
});
