// Import the Firebase scripts
importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-messaging.js');

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

// Initialize Firebase in the Service Worker
firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();

// Handle background messages
messaging.setBackgroundMessageHandler((payload) => {
  console.log('Received background message ', payload);
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: payload.notification.icon
  };

  return self.registration.showNotification(notificationTitle, notificationOptions);
});










