import markdown
from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from utils.constants import BANNER_COUNT, ARTICLE_PAGINATE_BY, COMMENT_PAGINATE_BY, TYPE_PAGINATE_BY, NEWESTCOUNT
from utils.paginator_ex import JuncheePaginator
from .models import Article, Tag, Category


class IndexView(View):
	"""首页"""

	def get(self, request):
		try:
			banner_articles = Article.objects.filter(is_show=True, is_banner=True)[:BANNER_COUNT]  # 轮播图数据
		except Exception as e:
			banner_articles = []
		context = {
			"banner_articles": banner_articles,
		}
		# 分页
		try:
			articles_set = Article.objects.filter(is_show=True)[:NEWESTCOUNT]  # 文章列表
		except Exception as e:
			articles_set = []
		articles = JuncheePaginator.paging(request, articles_set, ARTICLE_PAGINATE_BY)
		if articles:
			context["articles"] = articles
		return render(request, "index_test.html", context)


class ArticleView(View):
	"""详情页"""

	def get(self, request, id):
		if not id:
			# todo 404
			return render(request, "404.html")
		try:
			article = Article.objects.get(id=id, is_show=True)
			article.add_views()
			# 展示markdown语法
			article.body = markdown.markdown(article.body, ["extra", "codehilite", "toc", ])
		except Exception as e:
			return render(request, "404.html")
		context = {
			"article": article,
		}
		# 分页
		try:
			comments_set = Article.objects.get(id=id, is_show=True).comment_set.all()
		except Exception as e:
			comments_set = []
		comments = JuncheePaginator.paging(request, comments_set, COMMENT_PAGINATE_BY)
		if comments:
			context["comments"] = comments
		return render(request, "article_test.html", context)


class ArticleListView(View):
	"""分类"""

	def get(self, request, type, id):
		if type == "category":
			try:
				articles_set = Article.objects.filter(category_id=id, is_show=True)
				name = Category.objects.get(id=id)
			except Exception as e:
				name = ""
				articles_set = []
		elif type == "tag":
			try:
				articles_set = Tag.objects.get(id=id).article_set.filter(is_show=True).all()
				name = Tag.objects.get(id=id)
			except Exception as e:
				name = ""
				articles_set = []
		else:
			return redirect("/")

		# articles_set = Tag.objects.get(name=tag).article_set.all()
		context = {
			"type": type,
			"name": name,
		}
		articles = JuncheePaginator.paging(request, articles_set, TYPE_PAGINATE_BY)
		if articles:
			context["articles"] = articles
		return render(request, "tags.html", context)


class ArchivesView(View):
	"""归档"""

	def get(self, request):
		try:
			articles_list = Article.objects.filter(is_show=True)  # 文章列表
			# 获取归档的年/月
			dates = Article.objects.datetimes("created_time", "month", order="DESC")
		except Exception as e:
			articles_list = []
			dates = []
		year_month = {}
		for t in dates:
			if t.year not in year_month:
				year_month[t.year] = []
			year_month[t.year].append("%02d" % t.month)
		# 整理article的数据,year和month用作判断
		articles = []
		for article in articles_list:
			temp_dict = {}
			temp_dict["id"] = article.id
			temp_dict["title"] = article.title
			temp_dict["year"] = article.created_time.year
			temp_dict["month"] = "%02d" % article.created_time.month
			temp_dict["day"] = "%02d" % article.created_time.day
			articles.append(temp_dict)
		context = {
			"year_month": year_month,
			"articles": articles
		}
		return render(request, "archives.html", context)


class BlogListView(View):

	def get(self, request):
		return render(request, "bloglist.html")


class BlogListDataView(View):
	"""blog返回数据"""

	def get(self, request):
		page = request.GET.get("page", 1)
		print(page)
		try:
			page = int(page)
		except Exception as e:
			page = 1

		try:
			articles_set = Article.objects.filter(is_show=True).all()
		except Exception as e:
			articles_set = []
		paginator = Paginator(articles_set, 1)  # 数据按照每页2条进行分页
		total_page = paginator.num_pages
		data = []
		if page <= total_page:
			try:
				article_list = paginator.page(page)  # 第x页
			except Exception as e:
				article_list = paginator.page(1)  # 出错返回第一页

			if article_list:
				data = [{"error": "OK", "total_page": total_page}]
				for article in article_list.object_list:
					temp_dict = {}
					temp_dict["id"] = article.id
					temp_dict["title"] = article.title
					temp_dict["excerpt"] = article.excerpt
					temp_dict["created_time"] = article.created_time.strftime('%Y年%m月%d日 %H:%S')
					temp_dict["category"] = article.category.name
					temp_dict["category_id"] = article.category.id
					temp_dict["views"] = article.views
					temp_dict["img_url"] = article.image_url()
					temp_dict["comments"] = article.comment_set.count()
					data.append(temp_dict)
		return JsonResponse(data, safe=False)
