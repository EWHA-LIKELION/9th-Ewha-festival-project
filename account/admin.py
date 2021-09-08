from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProflieAdmin(admin.ModelAdmin):
    list_display =(
        'user_id',
        'user_pw',
        'user_name',
        'user_image',
        'user_phone',
        'user_nickname',
        'user_email',
    )