from django.contrib import admin
from .models import *

# Register your models here.
class boothImages(admin.TabularInline):
    model = boothImage
class boothAdmin(admin.ModelAdmin):
    inlines = [boothImages, ]
admin.site.register(boothPost, boothAdmin)
admin.site.register(boothComment)
admin.site.register(boothTags)