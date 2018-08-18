import logging

from django.db import models

# Create your models here.
from django.http import JsonResponse

from blog.models import Article
from user.models import User
from utils.error_code import ErrorCode


class Comment(models.Model):
	"""评论表,自关联多对多"""
	content = models.CharField(max_length=256, verbose_name='评论')
	created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
	user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='评论人')
	article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE, verbose_name='文章')
	parent = models.ForeignKey('self', default=None, on_delete=models.CASCADE, null=True, blank=True,
							   verbose_name='父评论')
	floor = models.IntegerField(default=0, verbose_name='楼层')

	@staticmethod
	def check_create(user_id, content, article_id, comment_id):
		if not all([content, article_id]):
			return JsonResponse({'error': ErrorCode.PARAMERR})
		if content.isspace():  # 如果content的内容为空格等
			return JsonResponse({'error': ErrorCode.COMMENTNONEERR})
		if not article_id:
			return JsonResponse({'error': ErrorCode.PARAMERR})
		# 尝试保存新评论
		try:
			comment = Comment()

			if comment_id:
				# 给评论评论
				comment.parent_id = comment_id
			# 给文章评论
			comment.content = content
			comment.article_id = article_id
			comment.user_id = user_id
			try:
				comment.floor = Comment.objects.filter(article_id=article_id).count() + 1
			except Exception as e:
				logging.error(e)
				pass
			comment.save()
		except Exception as e:
			logging.error(e)
			return JsonResponse({'error': ErrorCode.DATAERR})

		data = dict()
		data['id'] = comment.id
		data['article_id'] = comment.article_id
		data['content'] = comment.content
		data['user'] = comment.user.username
		data['img_url'] = comment.user.icon_url()
		data['floor'] = comment.floor
		data['created_time'] = comment.created_time.strftime('%Y年%m月%d日 %H:%S')
		return JsonResponse({"error": ErrorCode.OK, 'data': data})

	class Meta:
		ordering = ["-created_time", ]
		verbose_name = '评论'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称

	def __str__(self):
		return self.content
