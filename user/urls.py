from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^register$', views.RegisterView.as_view()),  # 注册
	url(r'^register/sendtomes', views.SendToMes.as_view()),  # 发送短信
	url(r'^login/$', views.LoginView.as_view()),  # 登录
	url(r'^logout/$', views.LoginOutView.as_view()),  # 登出
]
