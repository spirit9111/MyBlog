from django.conf.urls import url, include
from . import views

app_name = 'other'
urlpatterns = [
	url(r'^about', views.AboutMeView.as_view(), name='about'),  # 评论
	url(r'^refresh', views.UpdateStaticFileView.as_view(), name='flush'),  # 评论
]
