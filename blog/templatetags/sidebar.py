from django import template

from blog.models import Tag, Article

register = template.Library()


@register.simple_tag
def get_hot_articles():
	"""获取热门文章"""
	sidebar_articles = Article.objects.order_by('-views')[:3]  # 侧边栏
	return sidebar_articles


@register.simple_tag
def get_tags():
	"""tag云"""
	tags = Tag.objects.all()
	return tags

# todo 每日一句
