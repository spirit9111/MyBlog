from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view()),  # 首页
	url(r'^index/$', views.IndexView.as_view()),  # 首页
	url(r'^article/(?P<id>\d+)$', views.ArticleView.as_view()),  # 详情页
	url(r'^article/archives', views.ArchivesView.as_view()),
	# url(r'^article/lists', views.ListView.as_view()),  # 归档接口
	url(r'^article/(?P<tag>\w+)$', views.TagView.as_view()),
]
