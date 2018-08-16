from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from blog.models import Article
from comment.models import Comment


class CommentView(View):
	"""评论"""

	def post(self, request):
		is_login = request.session.get('is_login', None)
		if not is_login:  # 如果没有登录
			return JsonResponse({'error': '请登录,发表评论!'})
		user_id = request.session.get('user_id', None)
		content = request.POST.get('content', None)
		article_id = request.POST.get('article_id', None)
		comment_id = request.POST.get('comment_id', None)  # 可以为空,为空时返回''
		response = Comment.check_create(user_id, content, article_id, comment_id)
		# todo ajax,返回数据
		return response
