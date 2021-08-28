from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, DateField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.


class Inst(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_time = models.DateTimeField(null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Booth(models.Model):
    title = models.CharField(max_length=30)
    intro = models.CharField(max_length=30)
    pub_time = models.DateTimeField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
