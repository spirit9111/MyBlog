from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

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
		parent = request.POST.get('parent', None)  # 可以为空,为空时返回''

		if not all([content, article_id]):
			error = '参数不足'
			return JsonResponse({'error': error})

		if not content:  # 如果content的内容为空格等
			return JsonResponse({'error': '请输入评论内容'})
		if not article_id:  # 如果content的内容为空格等
			return JsonResponse({'error': '缺少文章id'})
		# 尝试保存新评论
		try:
			comment = Comment()
			# 给文章评论
			comment.content = content
			comment.article_id = article_id
			comment.user_id = user_id
			if parent:
				# 给评论评论
				comment.parent = parent
			comment.save()
		except Exception as e:
			return JsonResponse({'error': '数据库异常'})
		# 获取当前文章所有的评论
		comments = Comment.objects.filter(article_id=article_id)  # query_set

		json_data = serializers.serialize('json', comments, use_natural_foreign_keys=True)
		# print(json_data)
		# todo 返回数据
		return JsonResponse({"error": 'OK', 'data': json_data})
