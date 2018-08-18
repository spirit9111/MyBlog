from django.conf.urls import url, include
from . import views

app_name = 'comment'
urlpatterns = [
	url(r'^comment', views.CommentView.as_view()),  # 评论
]
