// service_worker_test.js

self.addEventListener('install', (event) => {
    console.log('Service Worker installing.');
  });
  
  self.addEventListener('activate', (event) => {
    console.log('Service Worker activating.');
  });
  
  self.addEventListener('push', (event) => {
    console.log('Push event received.');
  });
  