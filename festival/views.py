from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse


# Create your views here.

# main
def main(request):
    return render(request, 'frontScreens/main.html')

# 부스보드 인포화면
def collegeList(request):
    return render(request, 'frontScreens/collegeList.html')


#-------------- 간호대
def nursing(request): #글리스트
    post = nursingPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailnursing(request, pk_id): #글 상세보기
    post = get_object_or_404(nursingPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def nursingComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(nursingPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        nursingComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)


#-------------- 신융대
def convergence(request): #글리스트
    post = convergencePost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailconvergence(request, pk_id): #글 상세보기
    post = get_object_or_404(convergencePost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def convergenceComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(convergencePost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        convergenceComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)

#-------------------------경영대
def business(request): #글리스트
    post = businessPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailbusiness(request, pk_id): #글 상세보기
    post = get_object_or_404(businessPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def businessComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(businessPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        businessComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)


#-------------------------약대
def pharmacy(request): #글리스트
    post = pharmacyPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailpharmacy(request, pk_id): #글 상세보기
    post = get_object_or_404(pharmacyPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')

def pharmacyComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(pharmacyPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        pharmacyComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)


#--------------------------공대
def engineering(request): #글리스트
    post = engineeringPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailengineering(request, pk_id): #글 상세보기
    post = get_object_or_404(engineeringPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def engineeringComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(engineeringPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        engineeringComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)




#--------------------------음대
def music(request): #글리스트
    post = musicPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailmusic(request, pk_id): #글 상세보기
    post = get_object_or_404(musicPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def musicComment(request, pk_id): 
    post = get_object_or_404(musicPost, pk=pk_id)
    if request.method == 'POST':
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        musicComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)



#----------------------------사범대
def edu(request): #글리스트
    post = eduPost.objects.all()
    hashtag = eduTags.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post, 'hashtag':hashtag})

def detailedu(request, pk_id): #글 상세보기
    post = get_object_or_404(eduPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def eduComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(eduPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        eduComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)


#---------------------------인문대
def humanities(request): #글리스트
    post = humanitiesPost.objects.all()
    hashtag = humanitiesTags.objects.all()

    return render(request, 'boards/collegeBoards.html', {'post':post,'hashtag':hashtag})

def detailhumanities(request, pk_id): #글 상세보기
    post = get_object_or_404(humanitiesPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def humanitiesComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(humanitiesPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        humanitiesComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)


#--------------------------사회대
def social(request): #글리스트
    post = socialPost.objects.all()
    hashtag = socialTags.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post, 'hashtag':hashtag})

def detailsocial(request, pk_id): #글 상세보기
    post = get_object_or_404(socialPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def socialComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(socialPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        socialComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)


#--------------------------자연대
def natural(request): #글리스트
    post = naturalPost.objects.all()
    hashtag = naturalPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailnatural(request, pk_id): #글 상세보기
    post = get_object_or_404(naturalPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def naturalComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(naturalPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        naturalComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)


#--------------------------스크랜튼
def scraton(request): #글리스트
    post = scratonPost.objects.all()
    hashtag = scratonTags.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post, 'hashtag':hashtag})

def detailscraton(request, pk_id): #글 상세보기
    post = get_object_or_404(scratonPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def scratonComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(scratonPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        scratonComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)




#--------------------------조예대
def art(request): #글리스트
    post = artPost.objects.all()
    hashtag = artTags.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post, 'hashtag':hashtag})

def detailart(request, pk_id): #글 상세보기
    post = get_object_or_404(artPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def artComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(artPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        artComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)


#--------------------------호크마
def hokma(request): #글리스트
    post = hokmaPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailhokma(request, pk_id): #글 상세보기
    post = get_object_or_404(hokmaPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

@login_required(login_url='account:login')
def hokmaComment(request, pk_id):
    if request.method == 'POST':
        post = get_object_or_404(hokmaPost, pk=pk_id)
        context = {'post': post}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = User.objects.get(user=conn_user)

        if not content:
            messages.info(request, '내용이 없습니다')
            return render(request, 'details/detail.html', context=content)

        hokmaComment.objects.create(
            post=post, comment_writer=conn_profile, comment_contents=content)
        return render(request, 'details/detail.html', context=content)





# 검색
def search(request):
    collegepost = collegePost.objects.all().order_by('-id')
    q1 = request.POST.get('q1', "")

    boothpost = boothPost.objects.all().order_by('-id')
    q2 = request.POST.get('q2', "")

    if q1:
        collegepost = collegepost.filter(title__icontains=q1)
        return render(request, 'searches/searchBoards.html', {'collegeposts': collegepost, 'q1': q1})

    elif q2:
        boothpost = boothpost.filter(title__icontains=q2)
        return render(request, 'searches/searchBooth.html', {'boothposts': boothpost, 'q2': q2})

    else:
        return render(request, 'searches/search.html')


