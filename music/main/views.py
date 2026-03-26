from django.shortcuts import render, redirect
from .models import Genre, Track, Artist
from .forms import GenreForm, TrackForm, ArtistForm

def index(request):
    return render(request, 'index.html')

def genre(request):
    g=Genre.objects.all()
    return render(request, 'genres.html', {'genres': g})

def add_genre(request):
    if request.method=="POST":
        genre=GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect('/genre')
    else:
        genreform=GenreForm()
    return render(request, 'addGenre.html', {'form': genreform})

def edit_genre(request,id_genre):
    g=Genre.objects.get(id=id_genre)
    if request.method=="POST":
        genre=GenreForm(request.POST,instance=g)
        if genre.is_valid():
            genre.save()
        return redirect('/genre')
    else:
        genreform=GenreForm(instance=g)
    return render(request, 'updateGenres.html', {'form': genreform})

def deleteGenre(request, id_genre):
    genre=Genre.objects.get(id=id_genre)
    genre.delete()
    return redirect('/genre')

def track(request):
    t=Track.objects.all()
    return render(request, 'tracks.html', {'tracks': t})

def add_track(request):
    if request.method=="POST":
        track=TrackForm(request.POST)
        if track.is_valid():
            track.save()
        return redirect('/track')
    else:
        trackform=TrackForm()
    return render(request, 'addTrack.html', {'form': trackform})

def edit_track(request,id_track):
    t=Track.objects.get(id=id_track)
    if request.method=="POST":
        track=TrackForm(request.POST,instance=t)
        if track.is_valid():
            track.save()
        return redirect('/track')
    else:
        trackform=TrackForm(instance=t)
    return render(request, 'updateTrack.html', {'form': trackform})

def deleteTrack(request, id_track):
    track=Track.objects.get(id=id_track)
    track.delete()
    return redirect('/track')

def artists(request):
    a=Artist.objects.all()
    return render(request, 'artists.html', {'artists': a})




