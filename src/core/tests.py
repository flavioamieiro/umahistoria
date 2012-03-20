from datetime import date, timedelta
from model_mommy import mommy

from django.core.urlresolvers import reverse
from django.test import TestCase

from forms import ChapterForm
from models import Chapter

class ChapterFormtTest(TestCase):

    def test_accept_image_url(self):
        url="https://www.djangoproject.com/m/img/site/hdr_logo.png"
        form = ChapterForm({"image_url": url, "phrase": "xxx"})
        url="https://www.djangoproject.com/m/img/site/hdr_logo.jpg"
        form = ChapterForm({"image_url": url, "phrase": "xxx"})
        self.assertTrue(form.is_valid())
        self.assertTrue(form.is_valid())
        url="https://www.djangoproject.com/m/img/site/hdr_logo.jpeg"
        form = ChapterForm({"image_url": url, "phrase": "xxx"})
        self.assertTrue(form.is_valid())
        url="https://www.djangoproject.com/m/img/site/hdr_logo.gif"
        form = ChapterForm({"image_url": url, "phrase": "xxx"})
        self.assertTrue(form.is_valid())

    def test_incorrect_image_url(self):
        url="https://www.djangoproject.com/m/img/site/hdr_logo"
        form = ChapterForm({"image_url": url, "phrase": "xxx"})
        self.assertFalse(form.is_valid())

    def test_all_required_fields_are_present(self):
        form = ChapterForm({})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.get('phrase'))
        self.assertTrue(form.errors.get('image_url'))


class RouterTest(TestCase):

    def test_index_correct_template(self):
        response = self.client.get(reverse("core:index"))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "core/index.html")

    def test_ChapterForm_template(self):
        response = self.client.get(reverse("core:new_chapter"))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "core/novo_capitulo.html")

    def test_correct_template(self):
        response = self.client.get(reverse("core:about"))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "core/sobre.html")

    def test_list_date_template(self):
        response = self.client.get(reverse("core:date_history"))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "core/dates.html")


class ListChaptersViewTest(TestCase):

    def setUp(self):
        mommy.make_one(Chapter)
        old = mommy.make_one(Chapter)
        old.day = date.today() - timedelta(days=1)
        old.save()

    def test_correct_list(self):
        response = self.client.get(reverse("core:index"))
        self.assertIn("chapters", response.context)
        self.assertEqual(list(Chapter.objects.filter(day=date.today())), list(response.context["chapters"]))


class NewChapterViewTest(TestCase):

    def setUp(self):
        self.post_data = {
            "image_url": "https://www.djangoproject.com/m/img/site/hdr_logo.png",
            "phrase": "xxxxxx",
        }

    def test_correct_form(self):
        response = self.client.get(reverse("core:new_chapter"))
        self.assertIn("form", response.context)
        self.assertIsInstance(response.context["form"], ChapterForm)

    def test_invalid_post(self):
        response = self.client.post(reverse("core:new_chapter"), {})
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "core/novo_capitulo.html")
        self.assertIn("form", response.context)
        self.assertIsInstance(response.context["form"], ChapterForm)
        self.assertTrue(response.context["form"].errors)

    def test_valid_post(self):
        self.assertEqual(Chapter.objects.count(), 0)
        response = self.client.post(reverse("core:new_chapter"), self.post_data)
        self.assertRedirects(response, reverse("core:index"))
        self.assertEqual(Chapter.objects.count(), 1)
