/* Video cards: a card with data-yt="<YouTube id>" opens a dialog player; placeholder cards (empty data-yt) do nothing. */
(function () {
  var dlg = document.createElement('dialog');
  dlg.className = 'vdialog';
  dlg.innerHTML = '<button class="x" aria-label="סגירה">&times;</button><div class="frame16"></div>';
  document.body.appendChild(dlg);
  var box = dlg.querySelector('.frame16');
  function close() { box.innerHTML = ''; if (dlg.open) dlg.close(); }
  dlg.querySelector('.x').addEventListener('click', close);
  dlg.addEventListener('click', function (e) { if (e.target === dlg) close(); });
  dlg.addEventListener('close', function () { box.innerHTML = ''; });
  document.querySelectorAll('.vcard').forEach(function (c) {
    c.addEventListener('click', function () {
      var src = c.getAttribute('data-src');
      if (src) {
        box.innerHTML = '<video controls autoplay playsinline src="' + src + '"></video>';
        dlg.showModal();
        return;
      }
      var id = c.getAttribute('data-yt');
      if (!id) return;
      box.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1" title="' + c.textContent.trim() + '" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
      dlg.showModal();
    });
  });
})();
