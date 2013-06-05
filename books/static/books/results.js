(function($) {
	$(document).ready(function() {
		$(".js-track").click(function(e) {
			e.preventDefault();
			document.location.href = $(this).data('track');
		});
	});
})(jQuery);
