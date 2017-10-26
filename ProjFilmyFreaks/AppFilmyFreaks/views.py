from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from AppFilmyFreaks.forms import SignUpForm
from AppFilmyFreaks.models import UpcomingMovies,MoviesLangGen, GenreList, MovieBasicData, LanguagesList, MovieDetails, UserPreferences
# Create your views here.

def homepage(request):
    newmovies = UpcomingMovies.objects.all()
    status = "Login"
    lang_list = ["en", "fr", "es", "de"]
    if request.user.is_authenticated():
        userPreferenceLang = list(UserPreferences.objects.filter(username = request.user.username))
        status = "Logout"
        j = 0
        for i in range(len(userPreferenceLang)):
            if j >= 4:
                break
            else:
                if userPreferenceLang[i].preferLanguage in lang_list:
                    continue
                lang_list[j] = userPreferenceLang[i].preferLanguage
                j += 1
    moviesid1 = []
    moviesid2 = []
    moviesid3 = []
    moviesid4 = []
    langNames = []
    for i in range(len(lang_list)):
        langNames.extend(list(LanguagesList.objects.filter(lang_id = lang_list[i])))        
        movieids = MoviesLangGen.objects.filter(lang_id = lang_list[i])
        if i == 0:
            moviesid1.extend(list(movieids))
            movieData1 = []
            for j in range(10):
                movieData1.extend(list(MovieBasicData.objects.filter(movie_id = moviesid1[j].movie_id)))
        elif i == 1:
            moviesid2.extend(list(movieids))
            movieData2 = []
            for j in range(10):
                movieData2.extend(list(MovieBasicData.objects.filter(movie_id = moviesid2[j].movie_id)))
        elif i == 2:
            moviesid3.extend(list(movieids))
            movieData3 = []
            for j in range(10):
                movieData3.extend(list(MovieBasicData.objects.filter(movie_id = moviesid3[j].movie_id)))
        else:
            moviesid4.extend(list(movieids))
            movieData4 = []
            for j in range(10):
                movieData4.extend(list(MovieBasicData.objects.filter(movie_id = moviesid4[j].movie_id)))
                """
    print(moviesid1[0].movie_id)
    
    print(len(moviesid2))
    print(len(moviesid3))
    print(len(moviesid4))
    print(len(movieData1))
    print(movieData1[0].movie_id.movie_id)
    print(movieData1[0].movie_poster)
    print(movieData1[0].movie_title)
    print(movieData4[0].movie_poster)
        
        """
    rendered = render(request,'AppFilmyFreaks/Homepage.html', {'newmovieslist' : newmovies, 'langNames':langNames, 'lang1':movieData1, 'lang2':movieData2, 'lang3':movieData3, 'lang4':movieData4, 'status':status})
    return HttpResponse(rendered)
    
def languagegenrepage(request, id):
   status = "Login"
   if request.user.is_authenticated():
       status = "Logout"
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

   return HttpResponse(render(request, 'AppFilmyFreaks/genre.html', {'GenreName':genre_name, 'moviesList':moviesList, 'status': status}))
   
def languagepage(request, id):
   status = "Login"
   langId = list(LanguagesList.objects.filter(lang_name = id))
   if request.user.is_authenticated():
       status = "Logout"
       userPref = UserPreferences(username = request.user.username, preferLanguage = langId[0].lang_id)
       userPref.save()
   langId = str(langId[0].lang_id)
   
   obj = MoviesLangGen.objects.filter(lang_id = langId)
   moviesList = []
   for i in obj:
       moviesList.extend(list(MovieBasicData.objects.filter(movie_id = i.movie_id)))
       
   return HttpResponse(render(request, 'AppFilmyFreaks/genre.html', {'GenreName':id, 'moviesList':moviesList, 'status': status}))

def displaymoviedetails(request, id):
    status = "Login"
    if request.user.is_authenticated():
         status = "Logout"
    obj = MovieBasicData.objects.filter(movie_id = id)
    movieDetails = list(MovieDetails.objects.filter(movie_id = id))
    langGenre = MoviesLangGen.objects.filter(movie_id = id)
    lang = LanguagesList.objects.filter(lang_id = langGenre[0].lang_id)[0]
    lang = lang.lang_name
    genids = langGenre[0].gen_id.split("|")
    genre = ""
    for i in range(len(genids)):
        genre = genre + str(list(GenreList.objects.filter(genre_id = genids[i]))[0]) + ","
    genre = genre[:len(genre)-1]
    #HttpResponse("" + obj[0].movie_id.movie_id)
    return HttpResponse(render(request, 'AppFilmyFreaks/movieDet.html', {'movieBasicData':list(obj), 'movieDetails':movieDetails, 'language':lang, 'genre':genre, 'status': status}))
# Create your views here.

def signup(request):
    """print("enter signup")"""
    HttpResponse(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = raw_password)
            #login(request, user)
            print("Logged in succesfully")
            return redirect("http://127.0.0.1:8000/filmyfreaks/Login")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})

