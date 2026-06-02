from django.shortcuts import render
from .models import Music
# Create your views here.
def music(request):
    music_records= Music.objects.all()
    if request.method == "POST":
        song = request.POST.get("song")
        artist = request.POST.get("artist")
        year = request.POST.get("year")
        album = request.POST.get("album")
        # Save to DB...
        
        if song:
            music_records=music_records.filter(song__icontains=song)
        
        if artist:
            music_records=music_records.filter(artist__icontains=artist)
        
        if year:
            music_records=music_records.filter(year__icontains=year)
            
        if album:
            music_records=music_records.filter(album__icontains=album)
    return render(request,'findmusic/music.html',{'music_records':music_records})