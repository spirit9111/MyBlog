var cur_page = 0; // 当前页
var total_page = 1;  // 总页数


$(function () {
	if (cur_page < total_page) {
		// 去加载数据
		updateBlogData()
	}
	//页面滚动加载相关
	$(window).scroll(function () {
				// 浏览器窗口高度
				var showHeight = $(window).height();

				// 整个网页的高度
				var pageHeight = $(document).height();

				// 页面可以滚动的距离
				var canScrollHeight = pageHeight - showHeight;

				// 页面滚动了多少,这个是随着页面滚动实时变化的
				var nowScroll = $(document).scrollTop();

				// 页面滚动了多少,这个是随着页面滚动实时变化的
				if ((canScrollHeight - nowScroll) < 100) {
					// 如果当前页数据如果小于总页数，那么才去加载数据
					if (cur_page < total_page) {
						// cur_page += 1
						// 去加载数据
						updateBlogData()
					}
					// else {
					// 	alert('到底了')
					// }
				}
			}
	)
})

function updateBlogData() {
	cur_page += 1
	$.ajax({
		url: '/article/blogdata?page=' + cur_page,
		type: 'get',
		contentType: 'application/json',
		dataType: 'json',

		success: function (resp) {
			if (resp[0].error == "OK") {
				total_page = resp[0].total_page
				// 显示数据
				for (var i = 1; i <= (resp.length - 1); i++) {
					var data = resp[i]
					var content = ''
					content += '<article class="excerpt excerpt-1"><a class="focus" href="/article/' + data.id + '" title="" draggable="false">'
					content += '<img class="thumb" data-original="' + data.img_url + '" src="' + data.img_url + '" alt="" draggable="false" style="display: inline;"></a>'
					content += '<header><a class="cat" href="/article/category/' + data.category_id + '" draggable="false">' + data.category + '<i></i></a>'
					content += '<h2><a href="/article/' + data.id + '" title="" draggable="false">' + data.title + '</a></h2>'
					content += '</header>'
					content += '<p class="meta">'
					content += '<time class="time"><i class="glyphicon glyphicon-time"></i>' + data.created_time + '</time>'
					content += '<span class="views"><i class="glyphicon glyphicon-eye-open"></i> 共' + data.views + '人围观</span> <a class="comment"href="article.html#comment" draggable="false">'
					content += '<i class="glyphicon glyphicon-comment"></i> ' + data.comments + '条评论</a></p>'
					content += '<p class="note">' + data.excerpt + '</p>'
					content += '</article>'
					$(".content").append(content)
				}
			}
			else {
				// 请求失败
				alert('没有数据了')
			}
		}
	});
}

//2018年8月15日 14:11
//2018-08-17T09:18:00