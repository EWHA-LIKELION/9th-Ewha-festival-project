from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def college(request):
    colleges = collegePost.objects.all()
    return render(request, 'collegeBoard.html', {'colleges': colleges})


def collegePost(request, id):
    college = get_object_or_404(collegePost, pk=college_id)
    return render(request, 'collegePost.html', {'college': college})


def booth(request):
    booths = boothPost.objects.all()
    return render(request, 'boothBoard.html', {'booths': booths})


def boothPost(request, id):
    booth = get_object_or_404(Booth, pk=booth_id)
    return render(request, 'boothDetail.html', {'booth': booth})
