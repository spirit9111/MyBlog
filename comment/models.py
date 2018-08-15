from django.db import models

# Create your models here.
from blog.models import Article
from user.models import User


class Comment(models.Model):
	"""评论表,自关联多对多"""
	content = models.CharField(max_length=256, verbose_name='评论')
	created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
	user = models.ForeignKey(User, verbose_name='评论人')
	article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
	parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='父评论')

	# 如果有父评论,本身就是子评论
	# son = father.comment_set.all()
	# 如果没有父评论,本身就是父评论
	# father = Comment.objects.filter(article=1,parent__isnull=True)
	class Meta:
		ordering = ["-created_time", ]
		verbose_name = '评论'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称

	def __str__(self):
		return self.content
