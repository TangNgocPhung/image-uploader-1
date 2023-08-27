from django.db import models
from django.utils import timezone
# Create your models here.
class Image(models.Model):
    photo = models.CharField(max_length=10000)
    def __str__(self):
        return f"{self.id} , {self.photo}"

class File(models.Model):
    file = models.CharField(max_length = 1000, null = True, blank = True)
    
    def __str__(self):
        return f"{self.id} , {self.file}"