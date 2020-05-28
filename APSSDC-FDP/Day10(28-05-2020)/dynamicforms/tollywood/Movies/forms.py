from django.forms import ModelForm
from Movies.models import Movie

class Movies_form(ModelForm):
	class Meta:
		model=Movie
		fields='__all__'
		# fields=['producer','director','moviename']
