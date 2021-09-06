from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import boothPost, boothTags, boothComment
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
from account.models import Profile
import json

# Create your views here.

def boardboothPost(request):
    booth = boothPost.objects.all()
    boothtags = boothTags.objects.all()
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        return render(request, 'boards/boothBoards.html', {'post': booth,'hashtag':boothtags, 'user':user})
    else :
        return render(request, 'boards/boothBoards.html', {'post': booth,'hashtag':boothtags})
    


def detailboothPost(request, booth_id):
    user_id = request.session.get('user')
    detailBoothPost = get_object_or_404(boothPost, pk=booth_id)
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        return render(request, 'details/boothDetail.html', {'post': detailBoothPost,'user':user})
    else :
        return render(request, 'details/boothDetail.html', {'post': detailBoothPost})

def likelist(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        booth = boothPost.objects.get(pk=pk_id)
        if user in booth.booth_like.all():
            booth.booth_like.remove(user)
        else:
            booth.booth_like.add(user)
    else :
        return redirect('account:login')

    referer_url = request.META.get('HTTP_REFERER')
    path = urlparse(referer_url).path
    return HttpResponseRedirect(path)


def commentbooth(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(boothPost, pk=pk_id)

        booth = boothComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        booth.save()
        context = {
            'content':booth.comment_contents,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')
