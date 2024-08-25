from django.forms import ModelForm

from .models import Project, ProjectAttachment


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('content', 'title', 'address',)


class AttachmentForm(ModelForm):
    class Meta:
        model = ProjectAttachment
        fields = ('image',)