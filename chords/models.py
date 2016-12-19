from django.db import models
from django.urls import reverse

class Song(models.Model):
    artistname = models.CharField(max_length=50)
    songname = models.CharField(max_length=50)
    strummingpattern = models.CharField(max_length=50)
    chord1 = "one chord"
    chord2 = "two chord"
    chord3 = "three chord"
    chord4 = "four chord"
    chord5 = "five chord"
    chord6 = "six chord"
    chordnumber = (
        ('1', chord1),
        ('2', chord2),
        ('3', chord3),
        ('4', chord4),
        ('5', chord5),
        ('6', chord6)
    )
    howmanychords = models.CharField(max_length=255, choices=chordnumber, default=None, blank=True)


    songchord1 = models.FileField(max_length=255, upload_to="media/", default=None , blank=True  )
    songchord2 = models.FileField(max_length=255, upload_to="media/", default=None  , blank=True  )
    songchord3 = models.FileField(max_length=255, upload_to="media/" , default=None, blank=True )
    songchord4 = models.FileField(max_length=255, upload_to="media/" ,default=None, blank=True )
    songchord5 = models.FileField(max_length=255, upload_to="media/", default=None , blank=True )
    songchord6 = models.FileField(max_length=255, upload_to="media/",  default=None , blank=True )




    def __str__(self):
        return self.songname

    def get_absolute_url(self):
        return reverse('chords-detail', args=[str(self.id)])


