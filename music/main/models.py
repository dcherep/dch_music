from django.db import models

class Genre(models.Model):
    name_en=models.CharField(max_length=500)
    name_ru=models.CharField(max_length=500)
    description=models.CharField(max_length=5000)
    def __str__(self):
        return self.name_ru
    
class Artist(models.Model):
    name=models.CharField(max_length=500, unique=True)
    image=models.ImageField(upload_to='artists/',blank=True,null=True)

    def __str__(self):
        return self.name

class Track(models.Model):
    title=models.CharField(max_length=500, unique=True)
    duration=models.IntegerField(help_text="Длительность в секундах")
    genres=models.ManyToManyField(Genre)
    artist=models.ForeignKey(Artist, on_delete=models.RESTRICT,null=True)
    audio_file=models.FileField(upload_to='music/tracks/',blank=True,null=True)
    
    def __str__(self):
        return self.title
