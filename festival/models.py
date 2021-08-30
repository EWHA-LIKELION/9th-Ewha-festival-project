from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import BLANK_CHOICE_DASH, DateField, TextField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

# Create your models here.
class collegePost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    hashtag_set = models.ManyToManyField('collegeTags', blank=True)

    # 저장하기
    college_like = models.ManyToManyField(User, related_name='college_like', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class collegeTags(models.Model):
    college_tag = models.CharField(max_length=10, unique=True)

class boothPost(models.Model):
    title = models.CharField(max_length=50)
    intro = models.CharField(max_length=30)
    pub_time = models.DateTimeField(auto_now_add=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    hashtag_set = models.ManyToManyField('boothTags', blank=True)

    # 저장하기
    booth_like = models.ManyToManyField(User, related_name='booth_like', blank=True)

    def __str__(self):
        return self.title


class boothTags(models.Model):
    booth_tag = models.CharField(max_length=10, unique=True)