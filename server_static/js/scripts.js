//页面加载
$('body').show();
$('.version').text(NProgress.version);
NProgress.start();
setTimeout(function () {
	NProgress.done();
	$('.fade').removeClass('out');
}, 1000);

//页面加载时给img和a标签添加draggable属性
(function () {
	$('img').attr('draggable', 'false');
	$('a').attr('draggable', 'false');
})();

//返回顶部按钮
$("#gotop").hide();
$(window).scroll(function () {
	if ($(window).scrollTop() > 100) {
		$("#gotop").fadeIn();
	} else {
		$("#gotop").fadeOut();
	}
});
$("#gotop").click(function () {
	$('html,body').animate({
		'scrollTop': 0
	}, 500);
});

//图片延时加载
$("img.thumb").lazyload({
	placeholder: "/Home/images/occupying.png",
	effect: "fadeIn"
});
$(".single .content img").lazyload({
	placeholder: "/Home/images/occupying.png",
	effect: "fadeIn"
});

$('[data-toggle="tooltip"]').tooltip();
 




