
// Initialize Firebase
if (!firebase.apps.length) {
  firebase.initializeApp({
    apiKey: "AIzaSyD_XjS6m2taKT_8B4hnBQRclPeFJ-I5hm4",
    authDomain: "publicblog-e1866.firebaseapp.com",
    databaseURL: "https://publicblog-e1866-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "publicblog-e1866",
    storageBucket: "publicblog-e1866.appspot.com",
    messagingSenderId: "616505904173",
    appId: "1:616505904173:web:6f062f7b732a9eb15e7ca4",
    measurementId: "G-B5CS3X4EDW"
  });
}

// Get a reference to the messaging service
const messaging = firebase.messaging();

// Handle foreground messages
messaging.onMessage((payload) => {
  console.log('Message received. ', payload);
  // Customize notification if needed
});

// Function to request permission and get the token
function requestPermission() {
  return Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      return messaging.getToken(); // Get the token
    } else {
      throw new Error('Permission not granted for notifications.');
    }
  });
}

// Function to handle notification permission and token
function handleNotification() {
  requestPermission()
    .then((token) => {
      console.log('Token:', token);
      sendTokenToServer(token);
    })
    .catch((err) => {
      console.error('Error getting token:', err);
    });
}

// Function to send the token to the server
function sendTokenToServer(token) {
  fetch('{% url "blogpost:register-device" %}', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ token: token }),
  })
    .then(response => response.json())
    .then(data => console.log('Token saved:', data))
    .catch(error => console.error('Error:', error));
}

// Expose the handleNotification function to global scope
window.handleNotification = handleNotification;







