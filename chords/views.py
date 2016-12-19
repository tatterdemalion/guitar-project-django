from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from chords.models import Song

class IndexView(ListView):
    model = Song
    template_name = 'index.html'

class ChordDetailView(DetailView):
    model = Song
    template_name = 'chords_detail.html'

