$(document).ready(function(){
  $(".search a, .search").click(function(){
    $(".overlay").fadeIn(300, function(){
        $(".contain-all").fadeIn(300);
    });
  });

  $(".close").click(function(){
      $(".overlay").fadeOut(0, function(){
        $(".contain-all").fadeOut(0);
      });
  });
});
$(window).scroll(function(){
  var scrollPosition = $(window).scrollTop();
  var targetPosition = 59;
  if (scrollPosition>=targetPosition){
    $(".scroller-bar").addClass("menu-colorchange")
  }
  else{
    $(".scroller-bar").removeClass("menu-colorchange")
  }
})

// $(document).ready(function () {
//   $('body').on('click', '.contain-button-login button', function (){
//     var username = $('#email-input').val();
//     var password = $('#password-input').val();
//     var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
//     $.ajax({
//       type: 'POST',
//       url: '', // Replace with your server's login endpoint
//       data: {
//         'username': username,
//         'password': password,
//         'csrfmiddlewaretoken': csrf_token
//       },
//       success: function (response) {
//         console.log(response['status']);
//         if (response['status'] === true) {
//           alert(response['message'])
//           window.location.href = '/';
//         } else {
//           alert(response['message'])
//         }
//         console.log(response);
//       },
//       error: function () {
//
//       },
//     });
//   });
//   // Attach a submit event handler to the form
//   $('#login-form').submit(function (e) {
//     e.preventDefault(); // Prevent the form from submitting the traditional way
//
//     // Get values from form fields
//     var username = $('email-input').val();
//     var password = $('password-input').val();
//     alert('123');
//     // Create a data object to send with the AJAX request
//     var data = {
//       username: username,
//       password: password,
//     };
//
//     // Send an AJAX POST request to your server for authentication
//     $.ajax({
//       type: 'POST',
//       url: '/your-login-endpoint', // Replace with your server's login endpoint
//       data: data,
//       success: function (response) {
//         if (response.success) {
//           // Successful login, display a success message or redirect
//           $('#message').html('<p>Login successful!</p>');
//         } else {
//           // Failed login, display an error message
//           $('#message').html('<p>Login failed. Please check your credentials.</p>');
//         }
//       },
//       error: function () {
//         // Handle errors like network issues or server errors
//         $('#message').html('<p>An error occurred while processing your request.</p>');
//       },
//     });
//   });
// });
//
//
$(document).ready(function() {
    // Bắt sự kiện submit của biểu mẫu đăng nhập
    $(".contain-form-login").submit(function(event) {
        event.preventDefault();

        var username = $('#username').val();
        var password = $('#password').val();

        $.ajax({
            type: 'POST',
            url: 'login/', // Đặt URL xử lý đăng nhập
            data: {
                'username': username,
                'password': password
            },
            success: function(data) {
                $('#contentToReload').load('');
                $('.contain-form-login').text('Đăng nhập thành công');
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error(xhr.responseText);
            }
        });
    });
});
