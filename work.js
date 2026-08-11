// Portfolio grid + lightbox — used only on work.html

// "img" is the filename saved inside the /images folder.
var PORTFOLIO = [
  { img: 'portfolio-1.jpg', style: 'Crucifix & crown of thorns', tag: 'Traditional' },
  { img: 'portfolio-2.jpg', style: 'Jesus & Mary split portrait', tag: 'Realism' },
  { img: 'portfolio-3.jpg', style: 'Dove & cross', tag: 'Blackwork' },
  { img: 'portfolio-4.jpg', style: 'Lion chest piece', tag: 'Realism' },
  { img: 'portfolio-5.jpg', style: 'Praying hands, "Amen"', tag: 'Lettering' },
  { img: 'portfolio-6.jpg', style: 'Guitar & bull skull', tag: 'Blackwork' },
  { img: 'portfolio-7.jpg', style: 'Jesus portrait & dove', tag: 'Realism' },
  { img: 'portfolio-8.jpg', style: 'Wings & dagger, "Hope"', tag: 'Fine Line' },
  { img: 'portfolio-9.jpg', style: 'Compass, clock & rose sleeve', tag: 'Blackwork' },
  { img: 'portfolio-10.jpg', style: 'Archangel Michael', tag: 'Realism' },
  { img: 'portfolio-11.jpg', style: 'Lion & spear', tag: 'Color' },
  { img: 'portfolio-12.jpg', style: 'Holy family & names', tag: 'Lettering' },
  { img: 'portfolio-13.jpg', style: 'Sacred Heart of Mary', tag: 'Fine Line' }
];

document.addEventListener('DOMContentLoaded', function(){
  var grid = document.getElementById('flashGrid');
  if(!grid) return;

  PORTFOLIO.forEach(function(item, i){
    var card = document.createElement('div');
    card.className = 'flash-card';
    card.innerHTML =
      '<span class="flash-num mono">' + String(i+1).padStart(2,'0') + '</span>' +
      '<div class="flash-img-frame">' +
        '<img src="images/' + item.img + '" alt="' + item.style + ' tattoo by Trippy Tattooz" loading="lazy">' +
      '</div>' +
      '<div class="flash-caption">' +
        '<span class="flash-style">' + item.style + '</span>' +
        '<span class="flash-tag mono">' + item.tag + '</span>' +
      '</div>';
    var img = card.querySelector('img');
    img.addEventListener('error', function(){ window.__ph(img, 'images/' + item.img); });
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', function(){ openLightbox(i); });
    grid.appendChild(card);
  });

  // ---- Lightbox: click any portfolio photo to view it full-size ----
  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxCaption = document.getElementById('lightboxCaption');
  var lbIndex = 0;

  function renderLightbox(){
    var item = PORTFOLIO[lbIndex];
    lightboxImg.src = 'images/' + item.img;
    lightboxImg.alt = item.style;
    lightboxCaption.textContent = item.style + ' — ' + item.tag;
  }
  function openLightbox(i){
    lbIndex = i;
    renderLightbox();
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeLightbox(){
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
  }
  function lbPrev(){ lbIndex = (lbIndex - 1 + PORTFOLIO.length) % PORTFOLIO.length; renderLightbox(); }
  function lbNext(){ lbIndex = (lbIndex + 1) % PORTFOLIO.length; renderLightbox(); }

  document.getElementById('lightboxClose').addEventListener('click', closeLightbox);
  document.getElementById('lightboxPrev').addEventListener('click', lbPrev);
  document.getElementById('lightboxNext').addEventListener('click', lbNext);
  lightbox.addEventListener('click', function(e){ if(e.target === lightbox){ closeLightbox(); } });
  document.addEventListener('keydown', function(e){
    if(!lightbox.classList.contains('open')) return;
    if(e.key === 'Escape') closeLightbox();
    if(e.key === 'ArrowLeft') lbPrev();
    if(e.key === 'ArrowRight') lbNext();
  });
});
