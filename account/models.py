from django.db import models
# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')
    user_pw = models.CharField(max_length=128, verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=16, verbose_name='유저 이름')
    user_image = models.ImageField(upload_to="studentimages/", null=True)
    user_phone = models.CharField(max_length=16, null=True)
    user_nickname = models.CharField(max_length=16, unique=True, verbose_name='유저 닉네임')
    user_email = models.CharField(max_length=128, unique=True, verbose_name='유저 이메일')
    

    def __str__(self):
        return self.user_name

    def __str__(self):
        return self.user_nickname

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'


