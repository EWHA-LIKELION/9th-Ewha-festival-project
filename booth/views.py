from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import boothPost, boothTags, boothComment
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
from account.models import Profile

# Create your views here.

def boardboothPost(request):
    booth = boothPost.objects.all()
    boothtags = boothTags.objects.all()
    return render(request, 'boards/boothBoards.html', {'post': booth,'hashtag':boothtags})


def detailboothPost(request, booth_id):
    detailBoothPost = get_object_or_404(boothPost, pk=booth_id)
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
    referer_url = request.META.get('HTTP_REFERER')
    path = urlparse(referer_url).path
    return HttpResponseRedirect(path)


@login_required(login_url='account:login')
def comment_write_booth(request, pk_id):
    if request.method == 'POST':
        boothpost = get_object_or_404(boothPost, pk_id=pk_id)
        context = {'committepost': boothpost, }
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = Profile.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

            committeeComment.objects.create(
            post=boothpost, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)

