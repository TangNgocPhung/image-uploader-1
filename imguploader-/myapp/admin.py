from django.contrib import admin
from .models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo']

admin.site.register(Image,ImageAdmin)