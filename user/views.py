import random
import re

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django_redis import get_redis_connection

from blog.models import Article, Tag
from libs.dysms_python.send_2_mes import SendMes
from user import forms
from user.models import User


class SendToMes(View):
	"""短信接口"""

	def get(self, request):
		mobile = request.GET.get('mobile', None)
		print(mobile)
		if not mobile:
			message = '手机号未填写'
			return JsonResponse({'message': message})
		if not re.match(r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$', mobile):
			message = '手机号格式错误'
			return JsonResponse({'message': message})
		# 建立redis连接
		redis_conn = get_redis_connection('sms_code')
		if redis_conn.get('is_send_%s' % mobile):
			# 获取is_send,确保一分钟发送一次,能获得表示已发送
			message = '请求过于频繁'
			return JsonResponse({'message': message})
		sms_obj = SendMes()
		sms_code = '%06d' % random.randint(0, 999999)
		print(sms_code)
		# sms_obj.send_2_mes(mobile, sms_code)
		redis_conn.setex("is_send_%s" % mobile, 60, True)  # 60s一次
		redis_conn.setex("sms_%s" % mobile, 300, sms_code)  # 300s内有效
		message = '短信验证码已发送'
		return JsonResponse({'message': message})


class RegisterView(View):
	def get(self, request):
		sidebar_articles = Article.objects.filter(is_show=True, views__gt=0).order_by('-views')[:5]  # 热门文章
		tags = Tag.objects.all()
		context = {
			'sidebar_articles': sidebar_articles,
			'tags': tags,
		}
		return render(request, 'register.html', context)

	def post(self, request):
		"""注册"""
		mobile = request.POST.get('mobile', None)
		password = request.POST.get('password', None)
		password2 = request.POST.get('password2', None)
		sms_code = request.POST.get('sms_code', None)
		print(mobile, password, password2, sms_code)

		# 校验参数
		if not all([mobile, password, password2, sms_code]):
			message = '参数不足'
			return render(request, 'register.html', {'message': message})
		if not re.match(r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$', mobile):
			message = '手机号格式错误'
			return render(request, 'register.html', {'message': message})
		if password != password2:
			message = '两次密码不一致'
			return render(request, 'register.html', {'message': message})
		redis_conn = get_redis_connection('sms_code')
		real_sms_code = redis_conn.get('sms_%s' % mobile)
		if not real_sms_code:
			message = '验证码过期'
			return render(request, 'register.html', {'message': message})
		if sms_code != real_sms_code.decode():
			message = '验证码错误'
			return render(request, 'register.html', {'message': message})
		# 保存到数据库
		try:
			user = User.objects.create(name=mobile, mobile=mobile, password=password, )
		except Exception as e:
			message = '数据库错误'
			return render(request, 'register.html', {'message': message})
		request.session['is_login'] = True
		request.session['user_id'] = user.id
		request.session['user_name'] = user.name
		return redirect('/')


class LoginView(View):
	"""登录"""

	def get(self, request):
		if request.session.get('is_login', None):
			return redirect("/")
		sidebar_articles = Article.objects.filter(is_show=True, views__gt=0).order_by('-views')[:5]  # 热门文章
		tags = Tag.objects.all()
		context = {
			'sidebar_articles': sidebar_articles,
			'tags': tags,
		}
		return render(request, 'login.html', context)

	def post(self, request):
		if request.session.get('is_login', None):
			return redirect("/")
		login_form = forms.UserForm(request.POST)
		message = "请检查填写的内容！"
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			try:
				user = User.objects.get(name=username)
				if user.password == password:
					# 登录成功保存session
					request.session['is_login'] = True
					request.session['user_id'] = user.id
					request.session['user_name'] = user.name
					return redirect('/')
				else:
					message = "密码不正确！"
			except:
				message = "用户不存在！"
		return render(request, 'login.html', locals())


class LoginOutView(View):
	"""登出"""

	def get(self, request):
		if not request.session.get('is_login', None):
			return redirect("/")
		request.session.flush()
		return redirect("/")
