import uuid

from django.conf import settings
from django.db import models
from django.utils.timesince import timesince

from account.models import User


class NewsAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='News_attachments')
    # created_by = models.ForeignKey(User, related_name='News_attachments', on_delete=models.CASCADE)

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    
    attachments = models.ManyToManyField(NewsAttachment, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='Newss', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
    
    def created_at_formatted(self):
       return timesince(self.created_at)
    