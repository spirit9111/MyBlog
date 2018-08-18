# 索引
from haystack import indexes
from utils.constants import SEARCH_ARTICLE_COUNT
from utils.paginator_ex import JuncheePaginator
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Article

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


from haystack.views import SearchView


# from blog.settings import HAYSTACK_SEARCH_RESULTS_PER_PAGE

class MySearchView(SearchView):

	def build_page(self):
		"""重写搜索页分页的逻辑"""
		# todo 不循环查询出的结果就不对,bug不明
		for i in self.results:
			pass
		page, paginator = JuncheePaginator.paging(self.request, self.results, SEARCH_ARTICLE_COUNT)

		return paginator, page
