from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
	"""分类"""
	name = models.CharField(max_length=100, verbose_name='分类')

	class Meta:
		verbose_name = '分类'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称

	def __str__(self):
		return self.name


class Tag(models.Model):
	"""标签"""
	name = models.CharField(max_length=100, verbose_name='标签', unique=True)
	is_show = models.BooleanField(default=True, verbose_name='是否显示')

	class Meta:
		verbose_name = '标签'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称

	def __str__(self):
		return self.name


class Article(models.Model):
	"""文章"""
	title = models.CharField(max_length=100, verbose_name='标题')
	created_time = models.DateTimeField(verbose_name='发布日期')
	modified_time = models.DateTimeField(verbose_name='修改日期')
	author = models.ForeignKey(User, verbose_name='作者')
	category = models.ForeignKey(Category, verbose_name='分类')
	body = models.TextField(verbose_name='内容')
	views = models.PositiveIntegerField(default=0, verbose_name='浏览量')
	tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
	is_show = models.BooleanField(default=True, verbose_name='是否显示')
	image = models.ImageField(upload_to='upload/', null=True, blank=True, verbose_name='图片(220*150)')
	banner_image = models.ImageField(upload_to='upload/', null=True, blank=True, verbose_name='轮播图(820*200)')

	# 评论 pass
	# 获取图片的url
	def image_url(self):
		if not self.image:
			return '/static/images/upload/default_image.jpg'
		return self.image.url

	# 获取轮播图url
	def banner_image_url(self):
		if not self.image:
			return '/static/images/upload/default_banner_image.jpg'
		return self.banner_image.url

	class Meta:
		verbose_name = '文章'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称
		ordering = ['-created_time', ]

	def __str__(self):
		return self.title
