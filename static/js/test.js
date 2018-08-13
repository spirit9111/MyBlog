$(function () {
	var $div = $('.more');
	$div.delegate('a', 'click', function () {
		var tag = $(this).attr("tag");
		// alert(tag);

		//ajax
		// var params = {};

		$.ajax({
			url: 'article/' + tag,
			type: 'get',
			// data: JSON.stringify(params),
			data: '',
			contentType: 'application/json',
			dataType: 'json',
			// headers: {
			// 	"X-CSRFToken": getCookie("csrf_token")
			// },
			success: function (response) {
				// alert(response)
				alert('success')
			},
			error: function () {
				alert('error')
			}
		});
	});
})