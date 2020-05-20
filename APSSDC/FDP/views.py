from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hi(request):
	txt = '''uug<br>
	kdggkdff
	ergesjdgfj
	wwyygj
	wgfj
	kdgfds
	k'''
	return HttpResponse('<center><b>{}</b></center>'.format(txt))
