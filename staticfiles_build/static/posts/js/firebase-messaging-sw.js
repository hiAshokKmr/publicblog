importScripts('https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/10.13.0/firebase-messaging.js');

// Initialize Firebase app with your configuration
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

// Initialize Firebase Messaging
const messaging = firebase.messaging();

// Handle background notifications
messaging.onBackgroundMessage((payload) => {
  console.log('Received background message: ', payload);
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: '/path-to-your-icon.png',
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});
