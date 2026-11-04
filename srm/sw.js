// Offline cache for the phone app.  Data itself lives in the phone's own storage (IndexedDB), never online.
const CACHE = 'srm-1.2.0';
const FILES = ['./', './index.html', './style.css', './bundle.js', './vendor/exceljs.min.js', './vendor/pdf.min.js', './vendor/pdf.worker.min.js', './manifest.webmanifest', './icon-192.png', './icon-512.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES))); self.skipWaiting(); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  // network first (gets updates when online), cache when offline
  e.respondWith(fetch(e.request).then(r => { const c = r.clone(); caches.open(CACHE).then(x => x.put(e.request, c)); return r; }).catch(() => caches.match(e.request)));
});
