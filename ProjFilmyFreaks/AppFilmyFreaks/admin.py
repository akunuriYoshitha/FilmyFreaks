from django.contrib import admin
from AppFilmyFreaks.models import UpcomingMovies, LanguagesList, GenreList, MoviesLangGen, MovieBasicData, MovieDetails, Profile, UserReviews, UserPreferences

admin.site.register(UpcomingMovies)
admin.site.register(LanguagesList)
admin.site.register(GenreList)
admin.site.register(MoviesLangGen)
admin.site.register(MovieBasicData)
admin.site.register(MovieDetails)
admin.site.register(Profile)
admin.site.register(UserReviews)
admin.site.register(UserPreferences)
# Register your models here.
