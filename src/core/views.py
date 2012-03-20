from datetime import date

from django.views.generic import ListView, CreateView, TemplateView
from django.core.urlresolvers import reverse

from models import Chapter
from forms import ChapterForm

class ChapterListView(ListView):
    template_name = "core/index.html"
    context_object_name = "chapters"
    queryset = Chapter.objects.filter(day=date.today())


class NewChapterView(CreateView):
    template_name = "core/novo_capitulo.html"
    form_class = ChapterForm

    @property
    def success_url(self):
        return reverse("core:index")


class SobreView(TemplateView):
    template_name = "core/sobre.html"


class DateHistoryView(ListView):
    template_name = "core/dates.html"
    context_object_name = "dates"

    def get_queryset(self):
        return Chapter.objects.distinct('day').exclude(day=date.today()).values_list('day', flat=True)


class DayChaptersView(ListView):
    template_name = "core/index.html"
    context_object_name = "chapters"
    allow_empty = False

    def get_queryset(self):
        day = int(self.kwargs['day'])
        month = int(self.kwargs['month'])
        year = int(self.kwargs['year'])
        filter_date = date(year, month, day)
        today = date.today()
        return Chapter.objects.exclude(day=today).filter(day=filter_date)
