// WhatsApp booking form — used only on contact.html
// Builds a pre-filled WhatsApp message from the form fields, no backend needed.

document.addEventListener('DOMContentLoaded', function(){
  var bookingForm = document.getElementById('bookingForm');
  if(!bookingForm) return;

  bookingForm.addEventListener('submit', function(e){
    e.preventDefault();
    var data = new FormData(bookingForm);
    var name = (data.get('name') || '').trim();
    var phone = (data.get('phone') || '').trim();
    var idea = (data.get('idea') || '').trim();
    var date = (data.get('date') || '').trim();
    var ref = (data.get('ref') || '').trim();

    var lines = [
      'Hi! I\'d like to book a tattoo appointment.',
      'Name: ' + name,
      'My number: ' + phone,
      'Idea: ' + idea
    ];
    if(date) lines.push('Preferred date: ' + date);
    if(ref) lines.push('Reference: ' + ref);

    var message = encodeURIComponent(lines.join('\n'));
    window.open('https://wa.me/919145456658?text=' + message, '_blank');
  });
});
