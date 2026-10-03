(function () {
  var d = document.documentElement;
  var themeBtn = document.getElementById('themeBtn');
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var dark = d.getAttribute('data-theme') === 'dark';
    if (dark) d.removeAttribute('data-theme'); else d.setAttribute('data-theme', 'dark');
    try { localStorage.setItem('ss-theme', dark ? 'light' : 'dark'); } catch (e) {}
  });
  var menuBtn = document.getElementById('menuBtn'), nav = document.getElementById('navLinks');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function (e) { e.stopPropagation(); nav.classList.toggle('open'); });
    document.addEventListener('click', function (e) { if (!nav.contains(e.target)) nav.classList.remove('open'); });
  }
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
