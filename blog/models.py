import markdown
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class OtherManager(models.Manager):
# 	def get_by_natural_key(self, name):
# 		return self.get(name=name)
from django.utils.html import strip_tags
from mdeditor.fields import MDTextField


class Category(models.Model):
	"""分类"""
	# objects = OtherManager()
	name = models.CharField(max_length=100, verbose_name='分类')

	class Meta:
		verbose_name = '分类'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称

	def __str__(self):
		return self.name


class Tag(models.Model):
	"""标签"""
	name = models.CharField(max_length=100, verbose_name='标签', unique=True)

	class Meta:
		verbose_name = '标签'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称

	def __str__(self):
		return self.name


class Article(models.Model):
	"""文章"""
	title = models.CharField(max_length=100, verbose_name='标题')
	excerpt = models.TextField(max_length=200, blank=True, verbose_name='摘要')
	created_time = models.DateTimeField(verbose_name='发布日期')
	modified_time = models.DateTimeField(verbose_name='修改日期')
	author = models.ForeignKey(User, verbose_name='作者')
	category = models.ForeignKey(Category, verbose_name='分类')
	body = MDTextField(verbose_name='内容')
	views = models.PositiveIntegerField(default=0, verbose_name='浏览量')
	tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
	is_show = models.BooleanField(default=True, verbose_name='是否显示')
	is_banner = models.BooleanField(default=False, verbose_name='是否轮播')
	image = models.ImageField(upload_to='upload', null=True, blank=True,
							  verbose_name='图(820*200)')

	# 评论 pass
	# 获取图片的url
	def image_url(self):
		if not self.image:
			return '/static/images/upload/default_image.jpg'
		return '/static/images/' + self.image.url

	class Meta:
		verbose_name = '文章'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称
		ordering = ['-created_time', ]

	def save(self, *args, **kwargs):
		"""保存时,自动生成摘要"""
		if not self.excerpt:
			md = markdown.Markdown(['extra', 'codehilite', 'toc', ])
			excerpt = strip_tags(md.convert(self.body))[:150]
			if len(excerpt) < 150:
				self.excerpt = excerpt
			else:
				self.excerpt = excerpt + '......'

		# 调用父类的 save 方法将数据保存到数据库中
		super(Article, self).save(*args, **kwargs)

	def __str__(self):
		return self.title
