# Generated by Django 3.2 on 2021-09-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0002_auto_20210905_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='businessimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='convergenceimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='eduimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='engineeringimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='hokmaimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='humanitiesimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='musicimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='naturalimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='nursingimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='pharmacyimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='scratonmage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
        migrations.AlterField(
            model_name='socialimage',
            name='image',
            field=models.ImageField(upload_to='festivalImage/'),
        ),
    ]