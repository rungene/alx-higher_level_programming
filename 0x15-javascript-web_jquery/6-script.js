const $ = window.$;
// Select tag DIV#update_header element
const updateHeader = $('DIV#update_header');

// Bind an event handler to the click event of updateHeader element
updateHeader.click(function () {
  // select header element
  const header = $('HEADER');
  // Set the header text content to New Header!!!
  header.text('New Header!!!');
});
