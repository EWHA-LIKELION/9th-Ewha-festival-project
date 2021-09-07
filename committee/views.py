from django.http.response import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import committeePost, committeeComment
from account.models import Profile
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
import json


def main(request):
    return render(request, 'frontScreens/main.html')

def committeeList(request):
    committee = committeePost.objects.all()
    return render(request, 'boards/centralCommitteeBoards.html', {'post' : committee})

def detailcommitteePost(request, pk_id):
    detailCommitteePost= get_object_or_404(committeePost, pk=pk_id)
    return render(request, 'details/detail.html', {'post' : detailCommitteePost})


#committe 댓글
def commentcommittee(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(committeePost, pk=pk_id)

        committee = committeeComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        committee.save()
        context = {
            'content':committee.comment_contents,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')
