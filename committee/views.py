from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import committeePost, committeeComment
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse


def main(request):
    return render(request, 'frontScreens/main.html')

def committeeList(request):
    committee = committeePost.objects.all()
    return render(request, 'boards/centralCommitteeBoards.html', {'post' : committee})

def detailcommitteePost(request, pk_id):
    committeePost= get_object_or_404(committeeList, pk=pk_id)
    return render(request, 'details/detail.html', {'post' : committeePost})


#committe 댓글
@login_required(login_url='account:login')
def commentCommittee(request, pk_id):
    if request.method == 'POST':
        committeepost = get_object_or_404(committeePost, pk_id=pk_id)
        context = {'committepost': committeepost, }
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        committeeComment.objects.create(
            post=committeepost, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)



@login_required(login_url='account:login')
def mycommitteeComment(request):
    comment = committeeComment.objects.all()
    commentList = comment.filter(comment_writer=request.user.user_nickname)
    return render(request, 'auths/commentedPostBoards.html', {'commentList':commentList})