from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import BLANK_CHOICE_DASH, DateField, TextField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# -------------------------간호대
class nursingPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
class nursingComment(models.Model):
    post = models.ForeignKey(nursingPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents


#-------------------------신융대
class convergencePost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
class convergenceComment(models.Model):
    post = models.ForeignKey(convergencePost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents


#-------------------------경영대
class businessPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
  
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
class businessComment(models.Model):
    post = models.ForeignKey(businessPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents


#-------------------------약대
class pharmacyPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
class pharmacyComment(models.Model):
    post = models.ForeignKey(pharmacyPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents




#-------------------------공대
class engineeringPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
class engineeringComment(models.Model):
    post = models.ForeignKey(engineeringPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents




#-------------------------음대
class musicPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
class musicComment(models.Model):
    post = models.ForeignKey(musicPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents



#-------------------------사범대
class eduPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    hashtag_set = models.ManyToManyField('eduTags', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class eduTags(models.Model):
    college_tag = models.CharField(max_length=20, unique=True)

class eduComment(models.Model):
    post = models.ForeignKey(eduPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents



#-------------------------인문대
class humanitiesPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    hashtag_set = models.ManyToManyField('humanitiesTags', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class humanitiesTags(models.Model):
    college_tag = models.CharField(max_length=20, unique=True)

class humanitiesComment(models.Model):
    post = models.ForeignKey(humanitiesPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents


#-------------------------사회대
class socialPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    hashtag_set = models.ManyToManyField('socialTags', blank=True)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class socialTags(models.Model):
    college_tag = models.CharField(max_length=20, unique=True)

class socialComment(models.Model):
    post = models.ForeignKey(socialPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents


#-------------------------자연대
class naturalPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    hashtag_set = models.ManyToManyField('naturalTags', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class naturalTags(models.Model):
    college_tag = models.CharField(max_length=20, unique=True)

class naturalComment(models.Model):
    post = models.ForeignKey(naturalPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents




#-------------------------스크랜튼
class scratonPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    hashtag_set = models.ManyToManyField('scratonTags', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class scratonTags(models.Model):
    college_tag = models.CharField(max_length=20, unique=True)

class scratonComment(models.Model):
    post = models.ForeignKey(scratonPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents



#-------------------------조예대
class artPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    hashtag_set = models.ManyToManyField('artTags', blank=True)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class artTags(models.Model):
    college_tag = models.CharField(max_length=20, unique=True)

class artComment(models.Model):
    post = models.ForeignKey(artPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents



#-------------------------호크마
class hokmaPost(models.Model):
    title = models.CharField(max_length=50)
    college_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class hokmaComment(models.Model):
    post = models.ForeignKey(hokmaPost, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.TextField()
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save

    def __str__(self):
        return self.comment_contents
