from django.db import models


# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=128, unique=True, verbose_name='名字')
	password = models.CharField(max_length=256, verbose_name='密码')
	email = models.EmailField(unique=True, verbose_name='邮箱')
	created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-created_time", ]
		verbose_name = '用户'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称
