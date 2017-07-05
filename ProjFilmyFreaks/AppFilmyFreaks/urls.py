from django.conf.urls import url
from AppFilmyFreaks import views
urlpatterns = [url(r'^$',views.homepage,name = 'home'),
               url(r'^movies/([a-zA-Z]+)/$', views.languagegenrepage, name = 'languageGenre'),
               url(r'^moviedetails/([a-zA-Z0-9]+)/$', views.displaymoviedetails, name = 'languageGenre'),
               ]
