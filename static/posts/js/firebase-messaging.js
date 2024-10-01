

// Check if Firebase Messaging is supported
isSupported().then((supported) => {
  if (supported) {
    console.log('Browser supports Firebase Messaging.');
    navigator.serviceWorker.register('/firebase-messaging-sw.js')
      .then((registration) => {
        const messaging = getMessaging();
        console.log('Firebase Messaging initialized.');
      })
      .catch((err) => {
        console.error('Service Worker registration failed:', err);
      });
  } else {
    console.error('Browser does not support Firebase Messaging.');
  }
});




// Import Firebase SDKs for Messaging
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-analytics.js";
import { getMessaging, isSupported,getToken, onMessage } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-messaging.js";

// Your Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyD_XjS6m2taKT_8B4hnBQRclPeFJ-I5hm4",
  authDomain: "publicblog-e1866.firebaseapp.com",
  databaseURL: "https://publicblog-e1866-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "publicblog-e1866",
  storageBucket: "publicblog-e1866.appspot.com",
  messagingSenderId: "616505904173",
  appId: "1:616505904173:web:6f062f7b732a9eb15e7ca4",
  measurementId: "G-B5CS3X4EDW"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Initialize Messaging
const messaging = getMessaging(app);

// Request permission for notifications and get token
function requestNotificationPermission() {
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      console.log('Notification permission granted.');

      // Get the registration token for the device
      getToken(messaging, { vapidKey: 'YOUR_VAPID_KEY_HERE' }).then((currentToken) => {
        if (currentToken) {
          console.log('Generated Token:', currentToken);
          sendTokenToServer(currentToken);  // Send this token to your Django server
        } else {
          console.log('No registration token available.');
        }
      }).catch((err) => {
        console.error('An error occurred while retrieving token.', err);
      });
    } else {
      console.log('Notification permission not granted.');
    }
  });
}

// Send token to your server
function sendTokenToServer(token) {
  fetch('/save-token/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': '{{ csrf_token }}',
    },
    body: JSON.stringify({ token: token })
  })
  .then(response => response.json())
  .then(data => console.log('Token saved:', data))
  .catch(error => console.error('Error sending token:', error));
}

// Listen for incoming messages
onMessage(messaging, (payload) => {
  console.log('Message received: ', payload);
  alert(`Notification: ${payload.notification.title} - ${payload.notification.body}`);
});
