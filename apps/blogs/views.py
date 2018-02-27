from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "Placeholder to later display all the list of blogs"
	return HttpResponse(response)

def new(request):
	response = "Placeholder to display a form to created a new blog"
	return HttpResponse(response)