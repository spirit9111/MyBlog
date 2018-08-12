from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Article, Tag


# Create your views here.


class IndexView(View):
	"""首页"""

	def get(self, request):
		banner_articles = Tag.objects.get(id=12).article_set.filter(is_show=True)  # 轮播图
		articles = Article.objects.filter(is_show=True).all()  # articles
		tags = Tag.objects.filter(is_show=True)[:5]
		sidebar_articles = Article.objects.order_by('-views')[:3]  # 侧边栏
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
		context = {
			'sidebar_articles': sidebar_articles,
			'article': article,
		}
		return render(request, 'article_test.html', context)
