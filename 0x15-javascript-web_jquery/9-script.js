const $ = window.$;
const $hello = $('DIV#hello');
$(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    dataType: 'json',
    success: function (response) {
      $hello.text(response.hello);
    },
    error: function () {
      $hello.text('Error fetching value of hello');
    }
  });
});
