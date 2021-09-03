from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import BLANK_CHOICE_DASH, DateField, TextField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class committeePost(models.Model):
    title = models.CharField(max_length=50)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)

    # 저장하기
    committee_like = models.ManyToManyField(User, related_name='committee_like', blank=True)

    def __str__(self): 
        return self.title

    def summary(self):
        return self.body[:30]

class committeeComment(models.Model):
    post = models.ForeignKey(committeePost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents
