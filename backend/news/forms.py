from django.forms import ModelForm

from .models import *


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('content', 'title',)


class AttachmentForm(ModelForm):
    class Meta:
        model = NewsAttachment
        fields = ('image',)