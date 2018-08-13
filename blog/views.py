from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Article, Tag


# Create your views here.


class IndexView(View):
	"""首页"""

	def get(self, request):
		banner_articles = Tag.objects.get(id=12).article_set.filter(is_show=True)  # 轮播图
		articles_list = Article.objects.filter(is_show=True)  # 文章列表
		tags = Tag.objects.filter(is_show=True)
		sidebar_articles = Article.objects.filter(is_show=True, views__gt=0).order_by('-views')[:5]  # 热门文章
		# 分页
		paginator = Paginator(articles_list, 2)  # 显示3条数据
		page = request.GET.get('page')
		try:
			articles = paginator.page(page)
		except PageNotAnInteger:  # None或者其他
			# 如果用户请求的页码号不是整数，显示第一页
			articles = paginator.page(1)
		except EmptyPage:
			# 如果用户请求的页码号超过了最大页码号，显示最后一页
			articles = paginator.page(paginator.num_pages)
		context = {
			'banner_articles': banner_articles,
			'articles': articles,
			'tags': tags,
			'sidebar_articles': sidebar_articles,
		}
		return render(request, 'index_test.html', context)


class ArticleView(View):
	def get(self, request, id):
		if not id:
			# todo 404
			return HttpResponse('<h1>NOT FOUNT</h1>')
		try:
			article = Article.objects.get(id=id)
		except Exception as e:
			return HttpResponse('<h1>NOT FOUNT</h1>')
		sidebar_articles = Article.objects.order_by('-views')[:3]  # 侧边栏
		tags = Tag.objects.filter(is_show=True)
		context = {
			'sidebar_articles': sidebar_articles,
			'article': article,
			'tags': tags,
		}
		return render(request, 'article_test.html', context)


class TagView(View):
	def get(self, request, tag):
		articles_list = Tag.objects.get(name=tag).article_set.all()
		paginator = Paginator(articles_list, 1)  # 显示3条数据
		page = request.GET.get('page')
		try:
			articles = paginator.page(page)
		except PageNotAnInteger:  # None或者其他
			# 如果用户请求的页码号不是整数，显示第一页
			articles = paginator.page(1)
		except EmptyPage:
			# 如果用户请求的页码号超过了最大页码号，显示最后一页
			articles = paginator.page(paginator.num_pages)
		json_data = serializers.serialize('json', articles)
		return HttpResponse(json_data, content_type='application/json')
