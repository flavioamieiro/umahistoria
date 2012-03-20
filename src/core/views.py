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
