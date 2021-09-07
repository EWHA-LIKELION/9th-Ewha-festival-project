from django.contrib import admin
from .models import *

# Register your models here.
class committeeImages(admin.TabularInline):
    model = committeeImage
class committeeAdmin(admin.ModelAdmin):
    inlines = [committeeImages, ]

admin.site.register(committeePost, committeeAdmin)
admin.site.register(committeeComment)