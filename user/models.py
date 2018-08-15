from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
	# name = models.CharField(max_length=128, verbose_name='名字')
	mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
	# password = models.CharField(max_length=256, verbose_name='密码')
	# created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

	def __str__(self):
		return self.username

	class Meta:
		ordering = ["-date_joined", ]
		verbose_name = '用户'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称
