from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(boothPost)
admin.site.register(boothComment)
admin.site.register(boothTags)