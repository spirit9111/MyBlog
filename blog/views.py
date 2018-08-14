import markdown
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
		banner_articles = Article.objects.filter(is_show=True, is_banner=True)  # 轮播图
		articles_list = Article.objects.filter(is_show=True)  # 文章列表
		tags = Tag.objects.all()
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
			# 展示markdown语法
			article.body = markdown.markdown(article.body, ['extra', 'codehilite', 'toc', ])

		except Exception as e:
			return HttpResponse('<h1>NOT FOUNT</h1>')
		sidebar_articles = Article.objects.order_by('-views')[:3]  # 侧边栏
		tags = Tag.objects.all()
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
		sidebar_articles = Article.objects.filter(is_show=True, views__gt=0).order_by('-views')[:5]  # 热门文章
		tags = Tag.objects.all()
		context = {
			# 'banner_articles': banner_articles,
			'articles': articles,
			'tags': tags,
			'sidebar_articles': sidebar_articles,
			'tag': tag,
		}

		return render(request, 'tags.html', context)


class ArchivesView(View):
	def get(self, request):
		sidebar_articles = Article.objects.filter(is_show=True, views__gt=0).order_by('-views')[:5]  # 热门文章
		tags = Tag.objects.all()
		articles_list = Article.objects.filter(is_show=True)  # 文章列表
		# 获取归档的年/月
		dates = Article.objects.datetimes('created_time', 'month', order='DESC')
		year_month = {}
		for t in dates:
			if t.year not in year_month:
				year_month[t.year] = []
			year_month[t.year].append('%02d' % t.month)
		# 整理article的数据,year和month用作判断
		articles = []
		for article in articles_list:
			temp_dict = {}
			temp_dict["id"] = article.id
			temp_dict["title"] = article.title
			temp_dict["year"] = article.created_time.year
			temp_dict["month"] = '%02d' % article.created_time.month
			temp_dict["day"] = '%02d' % article.created_time.day
			articles.append(temp_dict)
		context = {
			'sidebar_articles': sidebar_articles,
			'tags': tags,
			'year_month': year_month,
			'articles': articles
		}
		return render(request, 'archives.html', context)

# class ListView(View):
# 	def get(self, request):
# 		year = request.GET.get('year')
# 		month = request.GET.get('month')
# 		articles = Article.objects.filter(created_time__year=year, created_time__month=month)
# 		data = []
# 		for article in articles:
# 			temp_dict = {}
# 			temp_dict["id"] = article.id
# 			temp_dict["title"] = article.title
# 			data.append(temp_dict)
#
# 		return JsonResponse(data, safe=False)
