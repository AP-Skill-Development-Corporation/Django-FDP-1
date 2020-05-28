from django.db import models

# Create your models here.
class Movie(models.Model):
	moviename=models.CharField(max_length=50)
	heroname=models.CharField(max_length=50)
	heroinename=models.CharField(max_length=50)
	producername=models.CharField(max_length=50)
	Directorname=models.CharField(max_length=50)
	Budget=models.FloatField(max_length=50)
	noofworkers=models.IntegerField()
