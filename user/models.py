import re

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.shortcuts import render
from django_redis import get_redis_connection


class User(AbstractUser):
	# name = models.CharField(max_length=128, verbose_name='名字')
	mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
	icon = models.ImageField(upload_to='icon', null=True, blank=True,
							 verbose_name='头像(36*36)')

	# password = models.CharField(max_length=256, verbose_name='密码')
	# created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
	def icon_url(self):
		if not self.icon:
			return '/static/images/icon/icon.png'
		return self.icon.url

	def __str__(self):
		return self.username

	class Meta:
		ordering = ["-date_joined", ]
		verbose_name = '用户'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称

	@staticmethod
	def check_create(mobile, username, password, password2, sms_code):
		# 校验参数
		if not all([username, mobile, password, password2, sms_code]):
			message = '参数不足'
			return {'message': message}
		if not re.match(r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$', mobile):
			message = '手机号格式错误'
			return {'message': message}
		try:  # 判断是否已经注册
			is_register = User.objects.filter(mobile=mobile).count()
		except Exception as e:
			# print(e)
			message = '数据库错误'
			return {'message': message}
		if is_register:
			message = '手机号已注册'
			return {'message': message}
		if password != password2:
			message = '两次密码不一致'
			return {'message': message}
		redis_conn = get_redis_connection('sms_code')
		real_sms_code = redis_conn.get('sms_%s' % mobile)
		if not real_sms_code:
			message = '验证码过期'
			return {'message': message}
		if sms_code != real_sms_code.decode():
			message = '验证码错误'
			return {'message': message}
		# 保存到数据库
		try:
			user = User()
			user.username = username
			user.mobile = mobile
			user.set_password(password)
			user.save()
		except Exception as e:
			message = '数据库错误'
			return {'message': message}
		return {'message': 'OK', 'user': user}

	@staticmethod
	def check_user(mobile, password):
		if not all([mobile, password]):
			message = '参数不足'
			return {'message': message}
		if not re.match(r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$', mobile):
			message = '手机号格式错误'
			return {'message': message}
		user_set = User.objects.filter(mobile=mobile)
		count = user_set.count()
		if count == 0:
			message = '%s,没有注册!' % mobile
			return {'message': message}
		user = user_set[0]
		if not user.check_password(password):
			message = '密码错误'
			return {'message': message}
		return {'message': 'OK', 'user': user}
