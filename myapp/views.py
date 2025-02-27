from django.shortcuts import render, get_object_or_404
from .models import Band, Album, Song

def home(request):
    bands = Band.objects.all()  # Fetch all the bands
    albums = Album.objects.all()[:5]  # Fetch the first 5 albums
    return render(request, 'home.html', {'bands': bands, 'albums': albums})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    albums = Album.objects.filter(band=band)  # Get all albums for this band
    return render(request, 'band_detail.html', {'band': band, 'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_detail.html', {'album': album, 'songs': album.songs.all()})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'song_detail.html', {'song': song})

def search(request):
    query = request.GET.get('q', '')
    bands = Band.objects.filter(name__icontains=query)
    songs = Song.objects.filter(title__icontains=query)
    albums = Album.objects.filter(title__icontains=query)

    return render(request, 'databaze_punku/search.html', {'query': query, 'bands': bands, 'songs': songs, 'albums': albums})