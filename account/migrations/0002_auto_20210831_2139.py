# Generated by Django 3.2.6 on 2021-08-31 12:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(null=True, upload_to='studentimages/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
