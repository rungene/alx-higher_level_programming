const $ = window.$;
// Select tag DIV#add_item element
const addItem = $('DIV#add_item');

// Bind an event handler to the click event of addItem element
addItem.click(function () {
  // create a new li element
  const li = ('<li>Item</li>');
  // Append the new li element to to UL.my_list element
  $('UL.my_list').append(li);
});
