from django import forms

from models import Chapter

class ChapterForm(forms.ModelForm):

    phrase = forms.CharField(widget=forms.TextInput
        (attrs={"class": "input-xlarge"}))
    image_url = forms.URLField(required=False, widget=forms.TextInput
        (attrs={"class": "input-xlarge"}))

    class Meta:
        model = Chapter
