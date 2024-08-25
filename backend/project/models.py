import uuid

from django.conf import settings
from django.db import models
from django.utils.timesince import timesince

from account.models import User


class ProjectAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='Project_attachments')
    created_by = models.ForeignKey(User, related_name='Project_attachments', on_delete=models.CASCADE)

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    # category = 
    
    attachments = models.ManyToManyField(ProjectAttachment, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='Projects', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
    
    def created_at_formatted(self):
       return timesince(self.created_at)
    