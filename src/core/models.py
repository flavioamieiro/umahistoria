#coding:UTF-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


def validate_url_is_image(url):
    acceptable_ends = [".jpg", ".jpeg", ".gif", ".png"]
    acceptable_ends += [end.upper() for end in acceptable_ends]
    url_end = "." + url.split(".")[-1]
    if not url_end in acceptable_ends:
        raise ValidationError(_(u"A imagem adicionada não é válida!"))

class Chapter(models.Model):
    phrase = models.CharField(_(u"Frase"), max_length=140)
    image_url = models.URLField(_(u"URL da imagem"), verify_exists=False, validators=[validate_url_is_image])
    day = models.DateField(_(u"Data da publicação"), auto_now_add=True)