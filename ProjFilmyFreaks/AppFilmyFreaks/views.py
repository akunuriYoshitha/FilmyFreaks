from django.shortcuts import render 
from django.http import HttpResponse
from AppFilmyFreaks.models import UpcomingMovies,MoviesLangGen, GenreList, MovieBasicData, LanguagesList, MovieDetails
# Create your views here.

def homepage(request):
    newmovies = UpcomingMovies.objects.all()
    
    rendered = render(request,'AppFilmyFreaks/Homepage.html', {'newmovieslist' : newmovies})
    return HttpResponse(rendered)
    
def languagegenrepage(request, id):
   genre_name = str(id)
   genreId = list(GenreList.objects.filter(gen_name = genre_name))
   if len(genreId) == 0:
       return languagepage(request, id)
       
   genreId = str(genreId[0].genre_id)
   obj = MoviesLangGen.objects.all()
   obj = obj.filter(gen_id__icontains=genreId)
   moviesList = []
   for i in obj:
       moviesList.extend(list(MovieBasicData.objects.filter(movie_id=i.movie_id)))

   return HttpResponse(render(request, 'AppFilmyFreaks/genre.html', {'GenreName':genre_name, 'moviesList':moviesList}))
   
def languagepage(request, id):
   langId = list(LanguagesList.objects.filter(lang_name = id))
   langId = str(langId[0].lang_id)
   obj = MoviesLangGen.objects.filter(lang_id = langId)
   moviesList = []
   for i in obj:
       moviesList.extend(list(MovieBasicData.objects.filter(movie_id = i.movie_id)))
       
   return HttpResponse(render(request, 'AppFilmyFreaks/genre.html', {'GenreName':id, 'moviesList':moviesList}))

def displaymoviedetails(request, id):
    obj = MovieBasicData.objects.filter(movie_title = "Everest")
    movieDetails = MovieDetails.objects.filter(movie_id = obj[0].movie_id.movie_id)
    langGenre = MoviesLangGen.objects.filter(movie_id = obj[0].movie_id.movie_id)
    lang = LanguagesList.objects.filter(lang_id = langGenre[0].lang_id)[0]
    lang = lang.lang_name
    genids = langGenre[0].gen_id.split("|")
    genre = ""
    for i in range(len(genids)):
        genre = genre + str(list(GenreList.objects.filter(genre_id = genids[i]))[0]) + ","
    genre = genre[:len(genre)-1]
    HttpResponse("" + obj[0].movie_id.movie_id)
    return HttpResponse(render(request, 'AppFilmyFreaks/movieDet.html', {'movieBasicData':obj, 'movieDetails':movieDetails, 'language':lang, 'genre':genre}))
# Create your views here.

