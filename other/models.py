from django.db import models


# # Create your models here.
class MottoList(models.Model):
	writer = models.CharField(max_length=255, verbose_name='作者')
	content = models.TextField(max_length=200, verbose_name='内容')
	created_time = models.DateTimeField(auto_now=True, verbose_name='创建日期')

	class Meta:
		verbose_name = '每日一句'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称

	def __str__(self):
		return self.writer
