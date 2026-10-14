document.querySelectorAll('.burger').forEach(function (b) {
  b.addEventListener('click', function () {
    var bar = b.closest('.mainbar');
    var open = bar.classList.toggle('open');
    b.setAttribute('aria-expanded', open);
  });
});

/* keep the active category visible in the horizontally scrolling sub nav */
(function () {
  var cur = document.querySelector('.subnav [aria-current="page"]');
  var bar = document.querySelector('.subnav .wrap');
  if (cur && bar) bar.scrollLeft += cur.getBoundingClientRect().left - bar.getBoundingClientRect().left - 80;
})();

/* article share button: native share sheet, otherwise copy the link */
document.querySelectorAll('[data-share]').forEach(function (b) {
  b.addEventListener('click', function () {
    var data = { title: document.title, url: location.href };
    if (navigator.share) { navigator.share(data).catch(function () {}); }
    else if (navigator.clipboard) { navigator.clipboard.writeText(location.href).then(function () { b.lastChild.textContent = 'הקישור הועתק'; }); }
  });
});
document.querySelectorAll('.lobby .ltabs').forEach(function (bar) {
  var root = bar.parentNode;
  bar.querySelectorAll('.lt').forEach(function (b) {
    b.addEventListener('click', function () {
      bar.querySelectorAll('.lt').forEach(function (x) { x.classList.toggle('on', x === b); });
      root.querySelectorAll('.lp').forEach(function (p) { p.classList.toggle('off', p.getAttribute('data-p') !== b.getAttribute('data-t')); });
    });
  });
});
