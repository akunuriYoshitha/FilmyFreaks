from urllib.request import urlopen
import urllib
import json
from random import randint

from app1.models import MoviesLangGen, MovieBasicData, MovieDetails

def insertData():
    
    languages_list = ['en', 'hi', 'de', 'it', 'ja', 'pt', 'fr', 'ko', 'es', 'zh']
    for pagenum in range(122, 200):
        print(pagenum)
        url = "https://api.themoviedb.org/3/discover/movie?api_key=36c6b5e06500346bf5c9b6949cf2ed4a&sort_by=popularity.desc&include_adult=false&include_video=false&page=" + str(pagenum)
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        dict = res.read().decode('utf-8')
        data = json.loads(dict)
        list = data['results']
        for movie_det in range(1, len(list)):
            movie_dict = list[movie_det]
            id = str(movie_dict['id'])
            title = movie_dict['title']
            poster_path = movie_dict['poster_path']
            if (poster_path == None):
                poster_url = ""
            else:
                poster_url = "http://image.tmdb.org/t/p/w300" + poster_path
            language_id = movie_dict['original_language']
            if language_id == 'en':
                language_id = languages_list[randint(0, 9)]
            genreId_list = movie_dict['genre_ids']
            release = movie_dict['release_date']
            genre_str = '|'.join(str(e) for e in genreId_list)
            moviesLangGenObj = MoviesLangGen(movie_id=id, lang_id=language_id, gen_id=genre_str)
            moviesLangGenObj.save()
            print(title)
            movieBasicDataObj = MovieBasicData(movie_id=moviesLangGenObj, movie_title=title, movie_poster=poster_url)
            movieBasicDataObj.save()
            print(title)
            url1 = "https://api.themoviedb.org/3/movie/" + id + "?api_key=36c6b5e06500346bf5c9b6949cf2ed4a" 
            req1 = urllib.request.Request(url1)
            try:
                res1 = urllib.request.urlopen(req1)
            except Exception:
                continue
            
            print(title)
            dict1 = res1.read().decode('utf-8')
            data1 = json.loads(dict1) 
            movie_rating = str(data1['vote_average'])
            movie_time = str(data1['runtime']) + "min"
            movie_plot = data1['overview']
            movieDetailsObj = MovieDetails(movie_id=moviesLangGenObj, release_date=release, runtime=movie_time, director_name="", plot=movie_plot, actors="", rating=movie_rating)
            movieDetailsObj.save()
            print(title)
