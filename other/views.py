from django.shortcuts import render

# Create your views here.
from django.views import View

from utils.constants import ABOUT_CONTENT


def page_not_found(request):
	return render(request, '404.html')


class AboutMeView(View):
	"""AboutMe"""

	# todo
	def get(self, request):
		context = {
			"contents": ABOUT_CONTENT
		}
		return render(request, 'about.html', context=context)
