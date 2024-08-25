import uuid

from django.db import models
from django.utils.timesince import timesince



class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    cv = models.FileField(upload_to='uploads', blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
    
    def created_at_formatted(self):
       return timesince(self.created_at)
    