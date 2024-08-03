
// CODE Desktop Dropdown 
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.post-one').forEach(function(div) {
        div.addEventListener('click', function() {
            var url = div.getAttribute('data-url');
            window.location.href = url;
        });
    });

    document.querySelectorAll('.popular-post').forEach(function(div) {
        div.addEventListener('click', function() {
            var url = div.getAttribute('data-url');
            window.location.href = url;
        });
    });

    document.querySelectorAll('.scrollable-post').forEach(function(div) {
        div.addEventListener('click', function() {
            var url = div.getAttribute('data-url');
            window.location.href = url;
        });
    });


});


document.addEventListener('DOMContentLoaded', function() {
    console.log("index js Document is fully loaded and parsed");

   

    document.querySelector('.back-to-top').addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    
    // Set initial selectedLanguage and selectedCategory from the dropdowns
    desktopSelectedLanguage = document.getElementById("desktop-language").innerText.trim();
    desktopSelectedCategory = document.getElementById("desktop-category").innerText.trim();
    console.log("Initial Desktop selected language is", desktopSelectedLanguage);
    console.log("Initial Desktop selected category is", desktopSelectedCategory);


     
});


document.addEventListener('click', function(event) {
    if (!event.target.closest('.desktop-dropdown')) {
        closeDropdowns();
    }
     handleClickOutsideSidebar(event);
});



function sendDesktopLanguage(language) {
    console.log("Selected language:", language);

    fetch(getUrl(), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken() // Add CSRF token to headers
        },
        body: JSON.stringify({ language: language }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Parse response as JSON
    })
    .then(data => {
        console.log('Success:', data);
        window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function sendDesktopCategory(category) {
    console.log("Selected category:", category);

    fetch(getUrl(), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken() 
        },
        body: JSON.stringify({ category: category }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Parse response as JSON
    })
    .then(data => {
        console.log('Success:', data);
        window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}



// function setLanguage(language) {
//     desktopSelectedLanguage = language;
//     document.getElementById("desktop-language").innerHTML = `${language} <i class="fas fa-chevron-down"></i>`;
//     closeDropdowns();
//     sendDesktopLanguage(desktopSelectedLanguage);
//     localStorage.setItem('selectedLanguage', language);
//     //console.log("Desktop Selected language is", desktopSelectedLanguage);
// }

function setLanguage(language) {
    const storedLanguage = localStorage.getItem('selectedLanguage');
    
    if (language !== storedLanguage) {
        desktopSelectedLanguage = language;
        document.getElementById("desktop-language").innerHTML = `${language} <i class="fas fa-chevron-down"></i>`;
        sendDesktopLanguage(desktopSelectedLanguage);
        localStorage.setItem('selectedLanguage', language);
    }
    
    closeDropdowns();
    window.location.href=getUrl();
    //console.log("Desktop Selected language is", desktopSelectedLanguage);
}

document.addEventListener('DOMContentLoaded', function() {
    // Check if a language is stored in local storage
    var storedLanguage = localStorage.getItem('selectedLanguage');
    var storedCategory=localStorage.getItem('selectedCategory');
    if (storedLanguage) {
        // Set the language in the dropdown and update the display
        document.getElementById("desktop-language").innerHTML = `${storedLanguage} <i class="fas fa-chevron-down"></i>`;
    }
    if(storedCategory){
        document.getElementById("desktop-category").innerHTML = `${storedCategory} <i class="fas fa-chevron-down"></i>`;
    }
});

function setCategory(category) {
    const storedCategory = localStorage.getItem('selectedCategory');
    if(category !== storedCategory){
        desktopSelectedCategory = category;
        document.getElementById("desktop-category").innerHTML = `${category} <i class="fas fa-chevron-down"></i>`;
        sendDesktopCategory(category);
        localStorage.setItem("selectedCategory",category);
    }

    closeDropdowns();
    window.location.href=getUrl();
    // console.log("Desktop Selected category is", desktopSelectedCategory);
}


function toggleDropdown(event, dropdownId) {
    event.preventDefault();
    const dropdown = document.getElementById(dropdownId);
    const isVisible = dropdown.style.display === 'block';
    closeDropdowns();
    if (!isVisible) {
        dropdown.style.display = 'block';
    }
}

function closeDropdowns() {
    document.querySelectorAll('.desktop-dropdown-content').forEach(dropdown => {
        dropdown.style.display = 'none';
    });
}
// CODE Desktop Dropdown END







// CODE Sidebar 

function showSideBar() {
    const sidebar = document.getElementById("mobile-sidebar");
    sidebar.style.display = "flex";
}

function hideSideBar() {
    const sidebar = document.getElementById("mobile-sidebar");
    sidebar.style.display = "none";
}

function handleClickOutsideSidebar(event) {
    const sidebar = document.getElementById("mobile-sidebar");
    const menuButton = document.querySelector(".menu-button");

    if (!sidebar.contains(event.target) && !menuButton.contains(event.target)) {
        hideSideBar();
    }
}

// CODE Sidebar END




// //Mobile DropDown Code Start

// // Function to toggle submenu display
// function toggleSubmenu(selectedItemId, submenuId) {
//     document.getElementById(selectedItemId).addEventListener("click", function() {
//         var submenu = document.getElementById(submenuId);
//         if (submenu.classList.contains("show")) {
//             submenu.classList.remove("show");
//         } else {
//             submenu.classList.add("show");
//         }
//     });
// }

// // Function to handle submenu item selection
// function handleSubmenuItemClick(submenuId, selectedItemId, fetchFunction) {
//     var submenuItems = document.querySelectorAll(`#${submenuId} .sidebar-submenu-item`);
//     submenuItems.forEach(function(item) {
//         item.addEventListener("click", function(event) {
//             event.preventDefault();
//             var selectedText = this.textContent;
//             var selectedItemSpan = document.querySelector(`#${selectedItemId} span`);
//             selectedItemSpan.textContent = selectedText;
//             var submenu = document.getElementById(submenuId);
//             setTimeout(function() {
//                 submenu.classList.remove("show");
//             }, 100);
//             window.location.href=getUrl();
//             fetchFunction(selectedText);
//         });
//     });
// }

// // Function to send selected language
// function sendMobileSelectedLanguage(selectedLanguage) {
//     console.log("mobile selected language is ", selectedLanguage);
//     fetch(getUrl(), {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': getCsrfToken(),
//         },
//         body: JSON.stringify({ language: selectedLanguage }),
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Success:', data);
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//     });
// }

// // Function to send selected category
// function sendMobileSelectedCategory(selectedCategory) {
//     console.log("mobile selected category is ", selectedCategory);
//     fetch(getUrl(), {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': getCsrfToken(),
//         },
//         body: JSON.stringify({ category: selectedCategory }),
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Success:', data);
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//     });
// }

// // Initialize language selection
// toggleSubmenu("mobile-selected-language", "sidebar-submenu-language");
// handleSubmenuItemClick("sidebar-submenu-language", "mobile-selected-language", sendMobileSelectedLanguage);

// // Initialize category selection
// toggleSubmenu("mobile-selected-category", "sidebar-submenu-category");
// handleSubmenuItemClick("sidebar-submenu-category", "mobile-selected-category", sendMobileSelectedCategory);

// //Mobile DropDown Code End



// Function to toggle submenu display
function toggleSubmenu(selectedItemId, submenuId) {
    document.getElementById(selectedItemId).addEventListener("click", function() {
        var submenu = document.getElementById(submenuId);
        if (submenu.classList.contains("show")) {
            submenu.classList.remove("show");
        } else {
            submenu.classList.add("show");
        }
    });
}

// Function to handle submenu item selection
function handleSubmenuItemClick(submenuId, selectedItemId, fetchFunction, storageKey) {
    var submenuItems = document.querySelectorAll(`#${submenuId} .sidebar-submenu-item`);
    submenuItems.forEach(function(item) {
        item.addEventListener("click", function(event) {
            event.preventDefault();
            var selectedText = this.textContent;
            var selectedItemSpan = document.querySelector(`#${selectedItemId} span`);
            selectedItemSpan.textContent = selectedText;

            // Store the selected item in localStorage
            localStorage.setItem(storageKey, selectedText);

            var submenu = document.getElementById(submenuId);
            setTimeout(function() {
                submenu.classList.remove("show");
            }, 100);

            
            fetchFunction(selectedText);
                        // Redirect after a slight delay to ensure the fetch completes
            setTimeout(function() {
                window.location.href = getUrl();
            }, 100);

        });
    });
}

// Function to initialize selected language or category from localStorage
function initializeSelection(selectedItemId, storageKey) {
    var storedValue = localStorage.getItem(storageKey);
    if (storedValue) {
        var selectedItemSpan = document.querySelector(`#${selectedItemId} span`);
        selectedItemSpan.textContent = storedValue;
    }
}

// Function to send selected language
function sendMobileSelectedLanguage(selectedLanguage) {
    console.log("mobile selected language is ", selectedLanguage);
    fetch(getUrl(), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ language: selectedLanguage }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Function to send selected category
function sendMobileSelectedCategory(selectedCategory) {
    console.log("mobile selected category is ", selectedCategory);
    fetch(getUrl(), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ category: selectedCategory }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Initialize language selection
toggleSubmenu("mobile-selected-language", "sidebar-submenu-language");
handleSubmenuItemClick("sidebar-submenu-language", "mobile-selected-language", sendMobileSelectedLanguage, 'selectedLanguage');
initializeSelection("mobile-selected-language", 'selectedLanguage');

// Initialize category selection
toggleSubmenu("mobile-selected-category", "sidebar-submenu-category");
handleSubmenuItemClick("sidebar-submenu-category", "mobile-selected-category", sendMobileSelectedCategory, 'selectedCategory');
initializeSelection("mobile-selected-category", 'selectedCategory');
