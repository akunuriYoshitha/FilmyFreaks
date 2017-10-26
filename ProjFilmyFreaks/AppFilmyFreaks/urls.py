from django.conf.urls import url
from AppFilmyFreaks import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [url(r'^$',views.homepage,name = 'home'),
               url(r'^movies/([a-zA-Z]+)/$', views.languagegenrepage, name = 'languageGenre'),
               url(r'^moviedetails/([a-zA-Z0-9]+)/$', views.displaymoviedetails, name = 'languageGenre'),
               url(r'^signup/$', views.signup, name = 'signup'),
               url(r'^Login/$', auth_views.login, name='login'),
               url(r'^Logout/$', auth_views.logout, name='logout'),
               ]
