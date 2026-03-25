from django.db import models

class Genre(models.Model):
    name_en=models.CharField(max_length=500)
    name_ru=models.CharField(max_length=500)
    description=models.CharField(max_length=5000)
    def __str__(self):
        return self.name_ru

class Track(models.Model):
    title=models.CharField(max_length=500, unique=True)
    duration=models.IntegerField()
    genres=models.ManyToManyField(Genre)
    def __str__(self):
        return self.title
