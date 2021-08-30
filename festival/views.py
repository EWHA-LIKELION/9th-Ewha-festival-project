from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import collegePost, collegeTags, boothPost, boothTags
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
# Create your views here.

def main(request):
    return render(request, 'frontScreens/main.html')

def boardcollegePost(request):
    collegePost = collegePost.objects.all()
    return render(request, 'boards/boothBords.html', {'collegePost':collegePost})

def detailcollegePost(request, college_id):
    collegePost = get_object_or_404(collegePost, pk=college_id)
    return render(request, 'details/boothDetail.html', {'collegePost':collegePost})

def boardboothPost(request):
    boothPost = boothPost.objects.all()
    return render(request, 'boards/boothBords.html', {'boothPost':boothPost})

def detailcollegePost(request, booth_id):
    boothePost = get_object_or_404(boothPost, pk=booth_id)
    return render(request, 'details/boothDetail.html', {'boothPost':boothPost})


@login_required(login_url='account:login')
def collegeLike(View):
    def get(Self, request, *args, **kwargs):
        if collegePost_id in kwargs:
            collegePost_id = kwargs['collegePost_id']
            collegePost = collegePost.objects.get(pk=college_id)
            user = request.user
            if user in collegePost.college_like.all():
                collegePost.college_like.remove(user)
            else:
                collegePost.college_like.add(user)
        
        referer_url = request.META.get('HTTP_REFERER')
        path = urlparse(referer_url).path
        return HttpResponseRedirect(path)
