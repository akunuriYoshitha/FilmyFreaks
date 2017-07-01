from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class LanguagesList(models.Model):
    lang_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.lang_name


class GenreList(models.Model):
    gen_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.gen_name

class MoviesLangGen(models.Model):
    
    movie_id = models.CharField(max_length = 30, primary_key = True)
    lang_id = models.ForeignKey('LanguagesList')
    gen_id = models.ForeignKey('GenreList')

    def __str__(self):
        return self.movie_id

class MovieBasicData(models.Model):
    movie_id = models.ForeignKey('MoviesLangGen', primary_key = True)
    movie_title = models.CharField(max_length = 100)
    movie_poster = models.ImageField()

    def __str__(self):
        return self.movie_title

class MovieDetails(models.Model):
    movie_id = models.ForeignKey('MoviesLangGen', primary_key = True)
    release_date = models.DateTimeField()
    runtime = models.CharField(max_length = 10)
    director_name = models.CharField(max_length = 50)
    plot = models.CharField(max_length = 1000)
    actors = models.CharField(max_length = 300)
    rating = models.FloatField()
    website_link = models.URLField()

    def __str__(self):
        return self.director_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    fname = models.CharField(max_length = 100)
    mname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    lname = models.CharField(max_length = 50, null = True, blank = True, default = None)


@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)


@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class UserReviews(models.Model):
    movie_id = models.ForeignKey('MoviesLangGen', primary_key = True)
    review = models.CharField(max_length = 1000)

    def __str__(self):
        return self.movie_id

class UserPreferences(models.Model):
    languages = models.CharField(max_length = 1000)
    genres = models.CharField(max_length = 1000)

    def __str__(self):
        return languages

