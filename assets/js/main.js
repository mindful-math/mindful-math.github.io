// Mark active nav link
(function () {
  const path = location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('nav a').forEach(a => {
    const href = a.getAttribute('href').replace(/\/$/, '') || '/';
    if (path === href || (href !== '/' && href !== '/index.html' && path.startsWith(href))) {
      a.classList.add('active');
    }
  });
})();

// Notebook iframe auto-height helper (same-origin only)
function fitIframe(iframe) {
  try {
    iframe.style.height = iframe.contentDocument.body.scrollHeight + 40 + 'px';
  } catch (_) {}
}
