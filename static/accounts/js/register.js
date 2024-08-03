



console.log("triggering java script");
const uploadImg = document.getElementById("uploadImg")
const profile = document.getElementById("profile")


profile.addEventListener("change", function (e) {
    // const file = e.target.files[0];
    // uploadImg.src = URL.createObjectURL(file)
    const file = e.target.files[0];
    console.log("uploaded image is : ", file)
    if (file) {
        uploadImg.src = URL.createObjectURL(file);
    }
});


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

togglePasswordVisibility('toggleRegisterPassword', 'password1');
togglePasswordVisibility('toggleConfirmPassword', 'password2');
function cleanUsername(username) {
    // Remove dots and special characters except underscore and alphanumeric characters
    return username.replace(/[^a-zA-Z0-9_]/g, '');
}
function validateForm() {
    let valid = true;

    // Username validation
    const username = document.getElementById('username').value.trim();
    const nameError = document.getElementById('nameError');
    if (username.length < 5) {
        nameError.textContent = 'Username must be at least 5 characters long.';
        valid = false;
    } else {
        nameError.textContent = '';
    }

    // Email validation
    const email = document.getElementById('email').value.trim();
    const emailError = document.getElementById('emailError');
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        emailError.textContent = 'Please enter a valid email address.';
        valid = false;
    } else if (username === email) {
        nameError.textContent = 'username and email cannot be same, user different username';
        valid = false;
    }
    else {
        emailError.textContent = '';
    }

    // Password validation
    const password1 = document.getElementById('password1').value.trim();
    const passwordError = document.getElementById('passwordError');
    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordPattern.test(password1)) {
        passwordError.textContent = 'Password must contain at least 1 special character, 1 uppercase letter, 1 lowercase letter, and 1 number.';
        valid = false;
    } else {
        passwordError.textContent = '';
    }

    // Confirm password validation
    const password2 = document.getElementById('password2').value.trim();
    const confirmPasswordError = document.getElementById('confirmPasswordError');
    if (password1.length < 8) {  // Moved this check to correct position
        passwordError.textContent = 'Password must be at least 8 characters long.';
        valid = false;
    } else if (password1 !== password2) {
        confirmPasswordError.textContent = 'Passwords do not match.';
        valid = false;
    } else {
        confirmPasswordError.textContent = '';
    }

    return valid;
}

document.addEventListener('DOMContentLoaded', function () {
    // Form submission event
    document.getElementById('registerForm').addEventListener('submit', function (event) {
        event.preventDefault(); // This should always be here to prevent default form submission
        const profileFile = document.getElementById('profile').files[0];
        console.log('Profile Picture File:', profileFile);

        if (validateForm()) {
            const formData = new FormData();
            //form data append name should be same name as django form fields
            formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);
            formData.append('username', document.getElementById('username').value.trim());
            formData.append('email', document.getElementById('email').value.trim());
            formData.append('password1', document.getElementById('password1').value.trim());
            formData.append('password2', document.getElementById('password2').value.trim());
            formData.append('profile_picture', document.getElementById('profile').files[0]);

            // Print the form data
            for (const [key, value] of formData.entries()) {
                console.log(`${key}: ${value}`);
            }
            console.log(`profilepicture: ${formData.get('profilepicture')}`);
            fetch('/account/register/', {
                method: 'POST',
                body: formData
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        console.log("SUCCESS MESSAGE", data);
                        console.log("LOGIN URL", loginUrl);
                        // Handle success case, e.g., redirect to login page

                        document.querySelector(".form-title").style.display = "none";
                        document.querySelector('.server-error-message').style.display = 'none';
                        document.querySelector(".server-success-message").style.display = "block";
                        document.getElementById('server-success-message-add').textContent = "Account Registration Successfull";
                        document.getElementById("registerForm").reset();
                        setTimeout(function () {
                            // window.location.href = loginUrl;
                            window.location.href = data.redirect_url;
                        }, 2000);

                    } else {
                        console.log("Failure", data.errors);
                        // document.querySelector(".form-title").style.display = "none";
                        document.querySelector(".server-error-message").style.display = "block";
                        document.getElementById('nameErrorMessage').textContent = data.errors.username ? data.errors.username : '';
                        document.getElementById('emailErrorMessage').textContent = data.errors.email ? data.errors.email : '';
                        document.getElementById('passwordErrorMessage').textContent = data.errors.password1 ? data.errors.password1 : '';
                        document.getElementById('confirmpasswordMessage').textContent = data.errors.password2 ? data.errors.password2 : '';
                        document.getElementById('profilepictureMessage').textContent = data.errors.profile_picture ? data.errors.profile_picture : '';
                        setTimeout(function () {
                            document.querySelector(".server-error-message").style.display = "none";
                        }, 5000);
                    }
                })
                .catch(error => console.error('Fetch error:', error));
        }


    });
});
