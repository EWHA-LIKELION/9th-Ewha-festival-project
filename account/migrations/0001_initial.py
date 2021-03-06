# Generated by Django 3.2.6 on 2021-09-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')),
                ('user_pw', models.CharField(max_length=128, verbose_name='유저 비밀번호')),
                ('user_name', models.CharField(max_length=16, verbose_name='유저 이름')),
                ('user_image', models.ImageField(null=True, upload_to='studentimages/')),
                ('user_phone', models.CharField(max_length=16, null=True)),
                ('user_nickname', models.CharField(max_length=16, unique=True, verbose_name='유저 닉네임')),
                ('user_email', models.CharField(max_length=128, unique=True, verbose_name='유저 이메일')),
            ],
        ),
    ]
