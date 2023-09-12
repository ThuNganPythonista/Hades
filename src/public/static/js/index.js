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


