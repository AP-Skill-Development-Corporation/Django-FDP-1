from django.shortcuts import render,redirect
from Movies.forms import Movies_form
from django.http import HttpResponse
from Movies.models import Movie
# Create your views here.
def moviereg(request):
	if request.method =="POST":
		data=Movies_form(request.POST)
		if data.is_valid():
			data.save()
			return redirect('/display')
		else:
			return HttpResponse("Invalid Data...!!!")
	mv_form=Movies_form()
	return render(request,'Movies/moviesreg.html',{'form':mv_form})

def display(request):
	Moviedata=Movie.objects.all()
	return render(request,'Movies/display.html',{'Mdata':Moviedata})
def update(request,id):
	data=Movie.objects.get(id=id)
	if request.method =="POST":
		data=Movies_form(request.POST,instance=data)
		data.save()
		return redirect('/display')
	form=Movies_form(instance=data)
	return render(request,'Movies/update.html',{'form':form,'data':data})

def delete(request,id):
	data=Movie.objects.get(id=id)
	data.delete()
	return redirect('/display')
def deleteall(request):
	data=Movie.objects.all()
	data.delete()
	return redirect('/display')
