from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Article, Tag


# Create your views here.


class IndexView(View):

	def get(self, request):
		articles = Article.objects.filter(is_show=True).all()
		banner_articles = Tag.objects.get(id=12).article_set.filter(is_show=True)
		tags = Tag.objects.filter(is_show=True)[:5]
		data = {
			'articles': articles,
			'banner_articles': banner_articles,
			'tags': tags,
		}
		# article = models.Article.objects.get(id=7)
		# print(article.image_url())
		return render(request, 'index.html', context=data)
