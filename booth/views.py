from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import boothPost, boothTags, boothComment
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse

# Create your views here.

# 부스 게시판


def boardboothPost(request):
    booth = boothPost.objects.all()
    return render(request, 'boards/boothBoards.html', {'post': booth})

# 부스 게시판 상세 글


def detailboothPost(request, booth_id):
    boothePost = get_object_or_404(boothPost, pk=booth_id)
    return render(request, 'details/detail.html', {'post': boothPost})


# 최신순(recent), 오래된순(old), 댓글많은순(review) 부스글 정렬
class boothPostSort(View):
    def get(self, request):
        sort = request.GET.get('sort', None)

        if sort == 'recent':  # 최신순
            booth_posts = boothPost.objects.order_by('pub_time')

        if sort == 'old':  # 오래된순
            booth_posts = boothPost.objects.order_by('-pub_time')

        if sort == 'review':  # 댓글 많은 순
            booth_posts = boothPost.annotate(
                review_count=Count('comments')).order_by('-review_count')

# 부스 좋아요 (저장 기능)


@login_required(login_url='account:login')
def boothLike(View):
    def get(Self, request, *args, **kwargs):
        if booth_id in kwargs:
            booth_id = kwargs['booth_id']
            boothPost = boothPost.objects.get(pk=booth_id)
            user = request.user
            if user in boothPost.booth_like.all():
                boothPost.booth_like.remove(user)
            else:
                boothPost.booth_like.add(user)

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
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

            committeeComment.objects.create(
                post=boothpost, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)
