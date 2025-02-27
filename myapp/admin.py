from django.contrib import admin
from .models import Band, Album, Song

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'url')  # Display URL in admin panel for ease

admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Song, SongAdmin)  # Register the Song model with the custom admin