# Generated by Django 3.2.6 on 2021-08-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0003_auto_20210831_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegepost',
            name='college_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]