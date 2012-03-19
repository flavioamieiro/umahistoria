from django.conf.urls.defaults import patterns, include, url

from views import ChapterListView, NewChapterView

urlpatterns = patterns('',
    url(r'^$', ChapterListView.as_view(), name="index"),
    url(r'^novo-capitulo/$', NewChapterView.as_view(), name="new_chapter"),
)
