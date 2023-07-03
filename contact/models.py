from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # lembrando que o blank e opcional isso quer dizer que não e obigatorio prencher este campo
    email = models.EmailField(max_length=254, blank=True)
    creaeted = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)