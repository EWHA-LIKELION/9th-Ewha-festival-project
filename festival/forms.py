from django import forms
from django.db.models import fields
from .models import collegeComment, boothComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = collegeComment, boothComment
        fields = ('comment_contents')
