// Instagram reel embeds — used only on instagram.html
// Add real post/reel URLs here to embed them, e.g. 'https://www.instagram.com/p/XXXXXXXXXXX/'
var INSTAGRAM_POSTS = [
  'https://www.instagram.com/reel/DRWLXrqCLY0/',
  'https://www.instagram.com/reel/DUSJ6ltiIn8/',
  'https://www.instagram.com/reel/DasglBjIen5/',
  'https://www.instagram.com/reel/DZzNq52IrIf/',
];

document.addEventListener('DOMContentLoaded', function(){
  var instaGrid = document.getElementById('instaGrid');
  if(!instaGrid) return;

  if(INSTAGRAM_POSTS.length){
    INSTAGRAM_POSTS.forEach(function(url){
      var wrap = document.createElement('div');
      wrap.className = 'insta-embed-wrap';
      wrap.innerHTML = '<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="' + url + '"></blockquote>';
      instaGrid.appendChild(wrap);
    });
    var s = document.createElement('script');
    s.src = 'https://www.instagram.com/embed.js';
    s.async = true;
    document.body.appendChild(s);
  } else {
    for(var i = 0; i < 3; i++){
      var ph = document.createElement('div');
      ph.className = 'insta-placeholder';
      ph.innerHTML = '📸<br>Add a post link to<br><strong>INSTAGRAM_POSTS</strong> to embed it here<br><a href="https://instagram.com/trippy_tattooz" target="_blank" rel="noopener">@trippy_tattooz →</a>';
      instaGrid.appendChild(ph);
    }
  }
});
