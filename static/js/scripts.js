//当浏览器窗口大小改变时重载网页
/*window.onresize=function(){
    window.location.reload();
}*/
 
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
 

 
//获取Cookie
// function getCookie(name) {
//     var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
//     if (arr = document.cookie.match(reg)) {
//         return unescape(arr[2]);
//     } else {
//         return null;
//     }
// }
 
// //导航智能定位
// $.fn.navSmartFloat = function () {
//     var position = function (element) {
//         var top = element.position().top,
//             pos = element.css("position");
//         $(window).scroll(function () {
//             var scrolls = $(this).scrollTop();
//             if (scrolls > top) { //如果滚动到页面超出了当前元素element的相对页面顶部的高度
//                 $('.header-topbar').fadeOut(0);
//                 if (window.XMLHttpRequest) { //如果不是ie6
//                     element.css({
//                         position: "fixed",
//                         top: 0
//                     }).addClass("shadow");
//                 } else { //如果是ie6
//                     element.css({
//                         top: scrolls
//                     });
//                 }
//             } else {
//                 $('.header-topbar').fadeIn(500);
//                 element.css({
//                     position: pos,
//                     top: top
//                 }).removeClass("shadow");
//             }
//         });
//     };
//     return $(this).each(function () {
//         position($(this));
//     });
// };
 
//启用导航定位
// $("#navbar").navSmartFloat();
 
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
 




