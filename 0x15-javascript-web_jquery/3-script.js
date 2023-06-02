const $ = window.$;
// Select tag DIV#red_header element
const redHeader = $('DIV#red_header');

// Bind an event handler to the click event of readHeader element
redHeader.click(function () {
  // Get class element
  const header = $('HEADER');

  // Set color property of the header
  header.addClass('red');
});
