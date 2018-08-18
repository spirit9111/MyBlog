from django.conf.urls import url, include
from . import views

app_name = 'user'
urlpatterns = [
	url(r'^register$', views.RegisterView.as_view(), name='register'),  # 注册
	url(r'^register/sendtomes', views.SendToMes.as_view(), name='sms'),  # 发送短信
	url(r'^login/$', views.LoginView.as_view(), name='login'),  # 登录
	url(r'^logout/$', views.LoginOutView.as_view(), name='logout'),  # 登出
]
