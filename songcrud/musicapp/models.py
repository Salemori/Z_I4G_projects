from turtle import onclick
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=225)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyric(models.Model):
    content = models.TextField(max_length=1000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
