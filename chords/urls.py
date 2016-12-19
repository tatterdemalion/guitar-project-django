from django.conf.urls import url,include
from chords import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ChordDetailView.as_view(), name='chords-detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+\
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^d/', include(debug_toolbar.urls)),
    ]