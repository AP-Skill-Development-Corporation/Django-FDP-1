from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
	return HttpResponse("<h1>Welcome to Django-Session</h1>")
def hello(request):
	return HttpResponse("<h1>This is from Hello</h1")
def data1(request,id):
	return HttpResponse("This is First value"+str(id))
def data2(request,name):
	return HttpResponse("This is Strin data"+name)
def data3(request,id,name):
	return HttpResponse("my name is "+name+"and My age is"+str(id))