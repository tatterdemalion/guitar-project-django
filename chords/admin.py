from django.contrib import admin
from chords.models import Song

class ChordsAdmin(admin.ModelAdmin):
    list_display = ('artistname', 'songname' , 'strummingpattern', 'songchord1',
                    'songchord2','songchord3','songchord4','songchord5','songchord6',
    )
    list_filter = ('howmanychords',)

admin.site.register(Song, ChordsAdmin)