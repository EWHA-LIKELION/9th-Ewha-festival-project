from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import collegePost, collegeTags, boothPost, boothTags
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse


# Create your views here.

def main(request):
    return render(request, 'frontScreens/main.html')

def collegeList(request):
    return render(request, 'frontScreens/collegeList.html')

def boardcollegePost(request, college_id):
    college = collegePost.objects.filter(college_name='college_id')
    return render(request, 'boards/collegeBoards.html', {'college': college})


def detailcollegePost(request, college_id, pk_id):
    college = collegePost.objects.filter(college_name='college_id')
    detailcollegePost = get_object_or_404(collegePost, pk=pk_id)
    return render(request, 'details/detail.html', {'college':college, 'detialcollegePost': detailcollegePost})


def boardboothPost(request):
    booth = boothPost.objects.all()
    return render(request, 'boards/boothBoards.html', {'booth': booth})


def detailboothPost(request, booth_id):
    boothePost = get_object_or_404(boothPost, pk=booth_id)
    return render(request, 'details/detail.html', {'boothPost': boothPost})


@login_required(login_url='account:login')
def collegeLike(View):
    def get(Self, request, *args, **kwargs):
        if college_id in kwargs:
            college_id = kwargs['college_id']
            collegePost = collegePost.objects.get(pk=college_id)
            user = request.user
            if user in collegePost.college_like.all():
                collegePost.college_like.remove(user)
            else:
                collegePost.college_like.add(user)

        referer_url = request.META.get('HTTP_REFERER')
        path = urlparse(referer_url).path
        

@login_required(login_url='account:login')
def boothLike(View):
    def get(Self, request, *args, **kwargs):
        if booth_id in kwargs:
            booth_id = kwargs['booth_id']
            boothPost = boothPost.objects.get(pk=booth_id)
            user = request.user
            if user in boothPost.college_like.all():
                boothPost.college_like.remove(user)
            else:
                boothPost.college_like.add(user)

        referer_url = request.META.get('HTTP_REFERER')
        path = urlparse(referer_url).path
        return HttpResponseRedirect(path)



# 검색
def search(request):
    collegepost = collegePost.objects.all().order_by('-id')
    q1 = request.POST.get('q1', "")

    boothpost = boothPost.objects.all().order_by('-id')
    q2 = request.POST.get('q2', "")

    if q1:
        collegepost = collegepost.filter(title__icontains=q1)
        return render(request, 'search.html', {'collegeposts': collegepost, 'q1': q1})

    elif q2:
        boothpost = boothpost.filter(title__icontains=q2)
        return render(request, 'search.html', {'boothposts': boothpost, 'q2': q2})

    else:
        return render(request, 'search.html')


# 부스글에 댓글
@login_required
def comment_write_booth(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=booth_id)
        context = {'boothposts': boothpost, }
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'festival/booth_detail.html', context=content)

        boothComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'festival/booth_detail.html', context=content)


# 단과대게시판글에 댓글
@login_required
def comment_write_college(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=college_id)
        context = {'collegeposts': collegepost, }
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'festival/college_detail.html', context=content)

        collegeComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'board/college_detail.html', context=content)
