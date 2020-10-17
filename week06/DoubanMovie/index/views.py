from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Movie, Comment

def index(request):
    movie = Movie.objects.first()

    comments = Comment.objects.filter(movie__id=movie.id, stars__gt=3)

    return render(request, 'douban.html', locals())
