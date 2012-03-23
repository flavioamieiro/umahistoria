from django.conf.urls.defaults import patterns, include, url

from views import ChapterListView, NewChapterView, SobreView, DateHistoryView, DayChaptersView, ChapterDetailView
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', ChapterListView.as_view(), name="index"),
    url(r'^capitulo/(?P<pk>\d+)/$', ChapterDetailView.as_view(), name="chapter"),
    url(r'^novo-capitulo/$', NewChapterView.as_view(), name="new_chapter"),
    url(r'^sobre/$', SobreView.as_view(), name="about"),
    url(r'^historias-passadas/$', DateHistoryView.as_view(), name="date_history"),
    url(r'^historias-passadas/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)$', DayChaptersView.as_view(), name="day_chapters"),
)
