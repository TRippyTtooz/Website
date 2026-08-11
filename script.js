// Shared across every page: mobile drawer, footer year, missing-image placeholder helper.

document.addEventListener('DOMContentLoaded', function(){
  var yearEl = document.getElementById('year');
  if(yearEl){ yearEl.textContent = new Date().getFullYear(); }

  // ---- Mobile side drawer menu ----
  var navMenuBtn = document.getElementById('navMenuBtn');
  var navDrawer = document.getElementById('navDrawer');
  var navDrawerClose = document.getElementById('navDrawerClose');
  var navDrawerOverlay = document.getElementById('navDrawerOverlay');

  function openDrawer(){
    navDrawer.classList.add('open');
    navDrawerOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeDrawer(){
    navDrawer.classList.remove('open');
    navDrawerOverlay.classList.remove('open');
    document.body.style.overflow = '';
  }
  if(navMenuBtn){ navMenuBtn.addEventListener('click', openDrawer); }
  if(navDrawerClose){ navDrawerClose.addEventListener('click', closeDrawer); }
  if(navDrawerOverlay){ navDrawerOverlay.addEventListener('click', closeDrawer); }
  if(navDrawer){
    navDrawer.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', closeDrawer);
    });
  }
});

// ---- placeholder helper: shows a friendly "drop your photo here" card ----
// when a referenced image file doesn't exist yet on disk.
window.__ph = function(imgEl, label){
  var wrap = imgEl.closest('.flash-img-frame, .about-photo');
  if(!wrap) return;
  imgEl.style.display = 'none';
  var note = document.createElement('div');
  note.className = 'placeholder-note';
  note.innerHTML = '📷<br><br>Add photo:<br><strong>' + label + '</strong>';
  wrap.appendChild(note);
};
