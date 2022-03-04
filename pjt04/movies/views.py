from multiprocessing import reduction
from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommendations(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/278/recommendations'
    params = {
        'api_key': '460e7cd63d0e5d631ca97c33b07c2497',
        'language': 'ko',
    }
        
    response = requests.get(BASE_URL + path, params=params)
    movie_dict = response.json()
    movie_details = movie_dict.get("results", None)
    movie1 = movie_details[0]
    
    context = {
        'title' : movie1.get('title', None),
        'vote_average' : movie1.get('vote_average', None),
        'overview' : movie1.get('overview', None),
        'poster_path' : movie1.get('poster_path', None),
        'release_date' : movie1.get('release_date', None)
    }
    
    return render(request, 'recommendations.html', context)