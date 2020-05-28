from django.shortcuts import render
from Movies.forms import Movies_form
# Create your views here.
def moviesreg(request):
	mv_form=Movies_form()
	return render(request,'Movies/moviesreg.html',{'form':mv_form})
