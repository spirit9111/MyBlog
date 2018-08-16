import markdown
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from utils.paginator_ex import JuncheePaginator
from .models import Article, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class IndexView(View):
	"""首页"""

	def get(self, request):
		banner_articles = Article.objects.filter(is_show=True, is_banner=True)  # 轮播图
		context = {
			'banner_articles': banner_articles,
		}
		# 分页
		articles_set = Article.objects.filter(is_show=True)  # 文章列表
		articles = JuncheePaginator.paging(request, articles_set)
		if articles:
			context['articles'] = articles
		return render(request, 'index_test.html', context)


class ArticleView(View):
	"""详情页"""

	def get(self, request, id):
		if not id:
			# todo 404
			return HttpResponse('<h1>NOT FOUNT</h1>')
		try:
			article = Article.objects.get(id=id)
			article.add_views()
			# 展示markdown语法
			article.body = markdown.markdown(article.body, ['extra', 'codehilite', 'toc', ])
		except Exception as e:
			return HttpResponse('<h1>NOT FOUNT</h1>')
		context = {
			'article': article,
		}
		# 分页
		comments_set = Article.objects.get(id=id).comment_set.all()
		comments = JuncheePaginator.paging(request, comments_set)
		if comments:
			context['comments'] = comments
		return render(request, 'article_test.html', context)


class ArticleListView(View):
	"""分类"""
	def get(self, request, type, id):
		if type == 'category':
			articles_set = Article.objects.filter(category_id=id)
		elif type == 'tag':
			articles_set = Tag.objects.get(id=id).article_set.all()
		else:
			return redirect('/')

		# articles_set = Tag.objects.get(name=tag).article_set.all()
		context = {
			'type': type,
			# 'type': type,
		}
		articles = JuncheePaginator.paging(request, articles_set)
		if articles:
			context['articles'] = articles
		return render(request, 'tags.html', context)


class ArchivesView(View):
	"""归档"""

	def get(self, request):
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
			'year_month': year_month,
			'articles': articles
		}
		return render(request, 'archives.html', context)
