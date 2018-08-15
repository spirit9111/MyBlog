from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^comment/', views.CommentView.as_view()),  # 评论
]
