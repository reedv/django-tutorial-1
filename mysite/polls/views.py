from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# defining our first view
def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

