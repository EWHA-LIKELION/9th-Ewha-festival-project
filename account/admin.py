from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =(
        'user_id',
        'user_pw',
        'user_name',
        'user_image',
        'user_phone',
        'user_nickname',
        'user_email',
    )