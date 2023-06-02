const $ = window.$;
// Select tag DIV#toggle_header element
const toggleHeader = $('DIV#toggle_header');

// Bind an event handler to the click event of toggleHeader element
toggleHeader.click(function () {
  // Get class element
  const header = $('HEADER');
  // Set color property of the header
  header.toggleClass('red green');
});
