from datetime import date

from django.views.generic import ListView, CreateView, TemplateView, DetailView
from django.core.urlresolvers import reverse
from django.http import Http404

from models import Chapter
from forms import ChapterForm

class ChapterListView(ListView):
    template_name = "core/index.html"
    context_object_name = "chapters"
    queryset = Chapter.objects.filter(day=date.today())

class ChapterDetailView(DetailView):
    context_object_name = "chapter"
    queryset = Chapter.objects.all()


class NewChapterView(CreateView):
    template_name = "core/novo_capitulo.html"
    form_class = ChapterForm

    @property
    def success_url(self):
        return reverse("core:index") + "#%d" % self.object.id


class SobreView(TemplateView):
    template_name = "core/sobre.html"


class DateHistoryView(ListView):
    template_name = "core/dates.html"
    context_object_name = "dates"

    def get_queryset(self):
        return Chapter.objects.distinct('day').exclude(day=date.today()).values_list('day', flat=True)


class DayChaptersView(ListView):
    template_name = "core/historia_antiga.html"
    context_object_name = "chapters"
    allow_empty = False

    @property
    def date_params(self):
        day = int(self.kwargs['day'])
        month = int(self.kwargs['month'])
        year = int(self.kwargs['year'])
        try:
            return date(year, month, day)
        except:
            raise Http404

    def get_queryset(self):
        today = date.today()
        return Chapter.objects.exclude(day=today).filter(day=self.date_params)

    def get_context_data(self, **kwargs):
        context = super(DayChaptersView, self).get_context_data(**kwargs)
        context.update({'full_date': self.date_params})
        return context
