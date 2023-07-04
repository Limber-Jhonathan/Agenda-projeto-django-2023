from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # lembrando que o blank=True e opcional isso quer dizer que não e obigatorio prencher este campo
    email = models.EmailField(max_length=254, blank=True)
    creaeted = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    #Os arquivos enviados pelo usuario irão para esta pasta
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
        
    