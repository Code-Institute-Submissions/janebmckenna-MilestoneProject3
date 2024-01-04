$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('.modal').modal();
    $(".collapsible").collapsible();
    // check passwords match
    $('#password, #confirm').on('keyup', function () {
        if ($('#password').val() == $('#confirm').val()) {
          $('#password-message').html('Passwords Match').css('color', 'green');
        } else 
          $('#password-message').html('Passwords Do Not Match').css('color', 'red');
      });
    $('select').formSelect();
    $(".tooltipped").tooltip();
    });


