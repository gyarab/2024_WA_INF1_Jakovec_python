from django.shortcuts import render, get_object_or_404, redirect
from .models import Band, Album, Song, Comment

def home(request):
    bands = Band.objects.all()
    albums = Album.objects.all()[:5]
    return render(request, 'home.html', {'bands': bands, 'albums': albums})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    albums = Album.objects.filter(band=band)
    return render(request, 'band_detail.html', {'band': band, 'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = Song.objects.filter(album=album)

    if request.method == "POST":
        cover_url = request.POST.get("cover_url")
        if cover_url:
            album.cover_url = cover_url
            album.save()

        return redirect('album_detail', album_id=album.id)

    return render(request, 'album_detail.html', {'album': album, 'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    comments = song.comments.all()

    if request.method == "POST":
        username = request.POST.get("username")
        text = request.POST.get("text")

        if username and text:
            Comment.objects.create(username=username, text=text, song=song)
            return redirect('song_detail', song_id=song.id)

    return render(request, 'song_detail.html', {'song': song, 'comments': comments})

def search(request):
    query = request.GET.get('q', '')
    bands = Band.objects.filter(name__icontains=query)
    songs = Song.objects.filter(title__icontains=query)
    albums = Album.objects.filter(title__icontains=query)

    return render(request, 'databaze_punku/search.html', {'query': query, 'bands': bands, 'songs': songs, 'albums': albums})