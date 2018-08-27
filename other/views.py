import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from MyBlog.settings import BASE_DIR


def page_not_found(request):
	return render(request, '404.html')


class AboutMeView(View):
	"""AboutMe"""

	def get(self, request):
		return render(request, 'about.html')


class UpdateStaticFileView(View):
	"""手动更新静态文件"""

	def get(self, request):
		sh_file = os.path.join(BASE_DIR, 'py_collecte.sh')
		status = os.system('bash %s' % sh_file)
		if status == 0:
			return HttpResponse('<h1>静态文件更新完毕</h1>')
		else:
			return HttpResponse('<h1>ERROR:静态文件更新失败</h1>')
