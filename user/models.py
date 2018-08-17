import logging
import re
from django.contrib.auth.models import AbstractUser
from django.db import models, IntegrityError
from django_redis import get_redis_connection
from utils.error_code import ErrorCode


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
			return {'error': ErrorCode.PARAMERR}
		if not re.match(r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$', mobile):
			return {'error': ErrorCode.MOBILETYPEERR}
		try:  # 判断是否已经注册
			is_register = User.objects.filter(mobile=mobile).count()
		except Exception as e:
			logging.error(e)
			return {'error': ErrorCode.DBERR}
		if is_register:
			return {'error': ErrorCode.MOBILEEXIST}
		if password != password2:
			return {'error': ErrorCode.PASSCHECKERR}
		redis_conn = get_redis_connection('sms_code')
		real_sms_code = redis_conn.get('sms_%s' % mobile)
		if not real_sms_code:
			return {'error': ErrorCode.SMSCODEERRR}
		if sms_code != real_sms_code.decode():
			return {'error': ErrorCode.SMSCODECHECKERRR}
		# 保存到数据库
		try:
			user = User()
			user.username = username
			user.mobile = mobile
			user.set_password(password)
			user.save()
		except IntegrityError as e:
			return {'error': ErrorCode.USERNAMEERR}
		except Exception as e:
			logging.error(e)
			return {'error': ErrorCode.DATAERR}
		return {'error': ErrorCode.OK, 'user': user}

	@staticmethod
	def check_user(mobile, password):
		if not all([mobile, password]):
			return {'error': ErrorCode.PARAMERR}
		if not re.match(r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$', mobile):
			return {'error': ErrorCode.MOBILETYPEERR}
		try:
			user_set = User.objects.filter(mobile=mobile)
			count = user_set.count()
		except Exception as e:
			logging.error(e)
			return {'error': ErrorCode.DATAERR}
		if count == 0:
			return {'error': ErrorCode.SERERR}
		user = user_set[0]
		if not user.check_password(password):
			return {'error': ErrorCode.PASSWORDERR}
		return {'error': ErrorCode.OK, 'user': user}
