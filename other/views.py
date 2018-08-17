from django.shortcuts import render


# Create your views here.

def page_not_found(request):
	return render(request, '404_old.html')
