// 归档相关
$(function () {
	$('.div0').children('a').click(function () {
		$(this).siblings('ul').slideToggle().parent().siblings().children('ul').slideUp()
	})
})
$(function () {
	$('.div01').children('a').click(function () {
		$(this).siblings('li').slideToggle().parent().siblings().children('li').slideUp()
	})
})

$(function () {
	$('.div0').children('a').mouseenter(function () {
		$(this).css({fontSize: "32.3px", color: "red"})
	})
})

$(function () {
	$('.div0').children('a').mouseleave(function () {
		$(this).css({fontSize: "32px", color: "#337ab7"})
	})
})

$(function () {
	$('.div01').children('a').mouseenter(function () {
		$(this).css({fontSize: "26.3px", color: "red"})
	})
})

$(function () {
	$('.div01').children('a').mouseleave(function () {
		$(this).css({fontSize: "26px", color: "#337ab7"})
	})
})


//发送短信
$(function () {
	$('#sms').click(function () {
		// alert('sms')
		var mobile = $('#mobile').val()
		$.ajax({
			url: '/register/sendtomes?mobile=' + mobile,
			type: 'get',
			contentType: 'application/json',
			dataType: 'json',
			success: function (data) {
				alert(data.message)
			},
			error: function () {
				alert(data.message)
			}
		});
	})
})


// $(this).siblings().slideToggle().parent().siblings().children('ul').slideUp()

// $(function () {
// 	var $div = $('.more');
// 	$div.delegate('a', 'click', function () {
// 		var tag = $(this).attr("tag");
// 		// alert(tag);
//
// 		//ajax
// 		// var params = {};
//
// 		$.ajax({
// 			url: 'article/' + tag,
// 			type: 'get',
// 			// data: JSON.stringify(params),
// 			data: '',
// 			contentType: 'application/json',
// 			dataType: 'json',
// 			// headers: {
// 			// 	"X-CSRFToken": getCookie("csrf_token")
// 			// },
// 			success: function (data) {
// 				// alert(response)
// 				$('.content article').remove();
//
//
// 				// for (var i = 0; i < resp.length; i++) {
// 				// 	var article = data[i]
// 					// alert(article.fields.title)
// 				// 	var content = ''
// 				// 	content += '<article class="excerpt excerpt-1"><a class="focus" href="article/'+article.pk+'" title="" draggable="false">'
// 				// 	content += '<img class="thumb" data-original="/static/images/upload/askdhfkahsdfh.png" src="/static/images/upload/askdhfkahsdfh.png" alt="" draggable="false" style="display: inline;"></a>'
// 				// 	content += '<header><a class="cat" href="program" draggable="false">后端<i></i></a>'
// 				// 	content += '<h2><a href="article/7" title="" draggable="false">图片测试1</a></h2>'
// 				// 	content += '</header>'
// 				// 	content += '<p class="meta">'
// 				// 	content += '<time class="time"><i class="glyphicon glyphicon-time"></i>2018年8月12日 17:29</time>'
// 				// 	content += '<span class="views"><i class="glyphicon glyphicon-eye-open"></i> 共100人围观</span>'
// 				// 	content += '<a class="comment" href="article.html#comment" draggable="false"><i class="glyphicon glyphicon-comment"></i>'
// 				// 	content += '0条评论</a>'
// 				// 	content += '</p>'
// 				// 	content += '<p class="note">图片测试1</p>'
// 				// 	content += '</article>'
// 				// }
// 				alert(data.length)
// 			},
// 			error: function () {
// 				alert('error')
// 			}
// 		});
// 	});
// })

