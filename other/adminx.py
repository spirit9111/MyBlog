import xadmin
from xadmin import views
from . import models


@xadmin.sites.register(models.MottoList)
class MottoListAdmin(object):
	list_display = ['id', 'writer', 'content']
	list_per_page = 10
	search_fields = ['writer', 'content']
