// 获得前端cookie
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// 这些HTTP方法不要求CSRF包含
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
	beforeSend: function (xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});
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
$('.switch').click(function () {
	$(this).parent('p').siblings().children('form').toggleClass('innershow')
	// alert('弹出输入框')

})

$('.reply').click(function (event) {
	//阻止跳转
	event.preventDefault();
	var comment_id = $(this).parent('form').attr('comment_id') //默认没有父评论
	var article_id = $(this).siblings('.articleid').val();
	var content = $(this).siblings('.textarea').val();
	if (!content) {
		alert('请输入评论内容');
		return
	}

	var params = {
		'article_id': article_id,
		'content': content,
		'comment_id': comment_id
	};

	$.ajax({
		url: 'http://127.0.0.1:8000/comment',
		type: 'post',
		data: params,
		dataType: 'json',
		// contentType: 'application/json',
		headers: {
			"X-CSRFToken": getCookie("csrf_token")
		},
		success: function (resp) {
			console.log(resp.error)
			// alert(resp.error);
			// alert('success')
			//
			if (resp.error == 'OK') {
				// alert('返回评论数据,拼接字符串!')
				window.location.reload()
			}
			else {
				//简单显示,未做处理
				alert(resp.error)
			}
		},
	});
});

$('#comment-submit').click(function (event) {
	//阻止跳转
	event.preventDefault();
	var comment_id = '' //默认没有父评论
	var article_id = $('.articleid').val();
	var content = $('.textarea').val();
	if (!content) {
		alert('请输入评论内容');
		return
	}

	var params = {
		'article_id': article_id,
		'content': content,
		'comment_id': comment_id
	};

	$.ajax({
		url: 'http://127.0.0.1:8000/comment',
		type: 'post',
		data: params,
		dataType: 'json',
		// contentType: 'application/json',
		headers: {
			"X-CSRFToken": getCookie("csrf_token")
		},
		success: function (resp) {
			console.log(resp.error)
			// alert(resp.error);
			// alert('success')
			//
			if (resp.error == 'OK') {
				// alert('返回评论数据,拼接字符串!')
				window.location.reload()
			}
			else {
				//简单显示,未做处理
				alert(resp.error)
			}
		},
	});
});