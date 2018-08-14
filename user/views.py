from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from blog.models import Article, Tag
from user import forms
from user.models import User


class RegisterView(View):
	def get(self, request):
		sidebar_articles = Article.objects.filter(is_show=True, views__gt=0).order_by('-views')[:5]  # 热门文章
		tags = Tag.objects.all()

		context = {
			'sidebar_articles': sidebar_articles,
			'tags': tags,
		}
		return render(request, 'register.html', context)


class LoginView(View):
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
