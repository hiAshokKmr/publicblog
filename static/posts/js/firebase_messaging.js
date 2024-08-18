// firebase-messaging.js

import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js';
import { getMessaging, getToken, onMessage } from 'https://www.gstatic.com/firebasejs/9.0.0/firebase-messaging.js';

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
const messaging = getMessaging(app);

// Request permission and get the token
Notification.requestPermission()
  .then(() => getToken(messaging))
  .then((token) => {
    console.log('Token:', token);
    // Send the token to your server
    sendTokenToServer(token);
  })
  .catch((err) => {
    console.error('Error getting token:', err);
  });

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






