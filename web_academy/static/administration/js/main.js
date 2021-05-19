(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });

})(jQuery);


function notificationError(msj){
    Swal.fire({
        title: 'Error',
        text: msj,
        icon: 'error'
    })
}

function notificationSuccess(msj){
    Swal.fire({
        title: 'Good job',
        text: msj,
        icon: 'success'
    })
}

$(document).ready(function(){
    $(".nav-tabs a").click(function(){
        $(this).tab('show');
    });
});