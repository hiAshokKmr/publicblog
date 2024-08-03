

document.addEventListener("DOMContentLoaded", function () {

    const togglePasswordVisibility = (toggleButtonId, inputFieldId) => {
        const toggleButton = document.getElementById(toggleButtonId);
        const inputField = document.getElementById(inputFieldId);

        toggleButton.addEventListener('click', () => {
            const type = inputField.getAttribute('type') === 'password' ? 'text' : 'password';
            inputField.setAttribute('type', type);
            toggleButton.classList.toggle('fa-eye');
            toggleButton.classList.toggle('fa-eye-slash');
        });
    };

    togglePasswordVisibility('toggleLoginPassword', 'password');

    document.getElementById("loginForm").addEventListener("submit", function (event) {
        event.preventDefault();
        
        // Trim the email and password values
        const emailValue = document.getElementById("email").value.trim();
        const passwordValue = document.getElementById("password").value.trim();
        
        console.log("Trimmed Email:", emailValue); // Debugging: Log the trimmed email
        console.log("Trimmed Password:", passwordValue); // Debugging: Log the trimmed password

        const formData = new FormData();
        formData.append('csrfmiddlewaretoken', document.querySelector("[name=csrfmiddlewaretoken]").value);
        formData.append("email", emailValue);
        formData.append("password", passwordValue);

        // Get reference to error and success message elements
        const errorMessage = document.getElementById("errorMessage");
        const successMessage = document.getElementById("successMessage");

        fetch('/account/login/', {
            method: "POST",
            credentials: 'same-origin',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    successMessage.textContent = data.message;
                    successMessage.style.display = 'block';
                    errorMessage.style.display = 'none';

                    setTimeout(function () {
                        document.getElementById("loginForm").reset();
                        successMessage.style.display = 'none';
                        window.location.href = data.redirect_url;
                    }, 2000);

                } else {
                    console.log("LOGIN failure");
                    errorMessage.textContent = data.error;
                    errorMessage.style.display = 'block';
                    successMessage.style.display = 'none';
                    console.error(data.error);

                    // Hide error message after 2 seconds
                    setTimeout(function () {
                        errorMessage.style.display = 'none';
                    }, 4000);
                }
            })
            .catch(errors => console.log("Errors", errors));

    });

});
