from committee.models import committeePost
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from booth.models import boothPost
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
from account.models import Profile
from django.db.models import Q
import json


# Create your views here.

# main
def main(request):
    return render(request, 'frontScreens/main.html')

# 부스보드 인포화면
def collegeList(request):
    return render(request, 'frontScreens/collegeList.html')

def search(request):
    return render(request, 'searches/search.html')
    
def searchPost(request):  # 검색
    query = request.GET['search']

    nursing = nursingPost.objects.all()
    convergence = convergencePost.objects.all()
    business = businessPost.objects.all()
    pharmacy = pharmacyPost.objects.all()
    engineering = engineeringPost.objects.all()
    music = musicPost.objects.all()
    edu = eduPost.objects.all()
    humanities = humanitiesPost.objects.all()
    social = socialPost.objects.all()
    natural = naturalPost.objects.all()
    scraton = scratonPost.objects.all()
    art = artPost.objects.all()
    hokma = hokmaPost.objects.all()
    committee = committeePost.objects.all()
    booth = boothPost.objects.all()

    if query:
        nursing = nursing.filter(Q(title__icontains=query) | Q(body__icontains=query))
        convergence = convergence.filter(Q(title__icontains=query) | Q(body__icontains=query))
        business = business.filter(Q(title__icontains=query) | Q(body__icontains=query))
        pharmacy = pharmacy.filter(Q(title__icontains=query) | Q(body__icontains=query))
        engineering = engineering.filter(Q(title__icontains=query) | Q(body__icontains=query))
        music = music.filter(Q(title__icontains=query) | Q(body__icontains=query))
        edu = edu.filter(Q(title__icontains=query) | Q(body__icontains=query))
        humanities = humanities.filter(Q(title__icontains=query) | Q(body__icontains=query))
        social = social.filter(Q(title__icontains=query) | Q(body__icontains=query))
        natural = natural.filter(Q(title__icontains=query) | Q(body__icontains=query))
        scraton = scraton.filter(Q(title__icontains=query) | Q(body__icontains=query))
        art = art.filter(Q(title__icontains=query) | Q(body__icontains=query))
        hokma = hokma.filter(Q(title__icontains=query) | Q(body__icontains=query))
        committee = committee.filter(Q(title__icontains=query) | Q(body__icontains=query))
        booth = booth.filter(Q(title__icontains=query) | Q(body__icontains=query))

        context = {
            'nursing' : nursing,
            'convergence' : convergence,
            'business' : business,
            'pharmacy' : pharmacy,
            'engineering' : engineering,
            'music' : music,
            'edu' : edu,
            'humanities' : humanities,
            'social' : social,
            'natural' : natural,
            'scraton' : scraton,
            'art' : art,
            'hokma' : hokma,
            'committee' : committee,
            'booth' : booth,
            'query' : query,
        }        

        return render(request, 'searches/search.html', context)
        
    else :
        return redirect('main')


#-------------- 간호대
def nursing(request): #글리스트
    post = nursingPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailnursing(request, pk_id): #글 상세보기
    post = get_object_or_404(nursingPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentnursing(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(nursingPost, pk=pk_id)

        nursing = nursingComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        nursing.save()

        context = {
            'content':nursing.comment_contents,
            'user': nursing.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')

def nursingSearch(request):  # 검색
    nursing = nursingPost.objects.all()
    query = request.GET['search']

    if query:
        nursing = nursing.filter(Q(title__icontains=query) | Q(body__icontains=query))
        context = {
            'nursing' : nursing,
        }        
        return render(request, 'searches/search.html', context)   
          
    else :
        return redirect('main')

#-------------- 신융대
def convergence(request): #글리스트
    post = convergencePost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailconvergence(request, pk_id): #글 상세보기
    post = get_object_or_404(convergencePost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentconvergence(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(convergencePost, pk=pk_id)

        convergence = convergenceComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        convergence.save()
        context = {
            'content':convergence.comment_contents,
            'user': convergence.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')

#-------------------------경영대
def business(request): #글리스트
    post = businessPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailbusiness(request, pk_id): #글 상세보기
    post = get_object_or_404(businessPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentbusiness(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(businessPost, pk=pk_id)

        business = businessComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        business.save()
        context = {
            'content':business.comment_contents,
            'user': business.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')


#-------------------------약대
def pharmacy(request): #글리스트
    post = pharmacyPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailpharmacy(request, pk_id): #글 상세보기
    post = get_object_or_404(pharmacyPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentpharmacy(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(pharmacyPost, pk=pk_id)

        pharmacy = pharmacyComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        pharmacy.save()
        context = {
            'content':pharmacy.comment_contents,
            'user': pharmacy.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')



#--------------------------공대
def engineering(request): #글리스트
    post = engineeringPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailengineering(request, pk_id): #글 상세보기
    post = get_object_or_404(engineeringPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentengineering(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(engineeringPost, pk=pk_id)

        engineering = engineeringComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        engineering.save()
        context = {
            'content':engineering.comment_contents,
            'user': engineering.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')




#--------------------------음대
def music(request): #글리스트
    post = musicPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailmusic(request, pk_id): #글 상세보기
    post = get_object_or_404(musicPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentmusic(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(musicPost, pk=pk_id)

        music = musicComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        music.save()
        context = {
            'content':music.comment_contents,
            'user': music.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')




#----------------------------사범대
def edu(request): #글리스트
    post = eduPost.objects.all()
    hashtag = eduTags.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post, 'hashtag':hashtag})

def detailedu(request, pk_id): #글 상세보기
    post = get_object_or_404(eduPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentedu(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(eduPost, pk=pk_id)

        edu = eduComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        edu.save()
        context = {
            'content':edu.comment_contents,
            'user': edu.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')


#---------------------------인문대
def humanities(request): #글리스트
    post = humanitiesPost.objects.all()
    hashtag = humanitiesTags.objects.all()

    return render(request, 'boards/collegeBoards.html', {'post':post,'hashtag':hashtag})

def detailhumanities(request, pk_id): #글 상세보기
    post = get_object_or_404(humanitiesPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commenthumanities(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(humanitiesPost, pk=pk_id)

        humanities = humanitiesComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        humanities.save()
        context = {
            'content':humanities.comment_contents,
            'user': humanities.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')

#--------------------------사회대
def social(request): #글리스트
    post = socialPost.objects.all()
    hashtag = socialTags.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post, 'hashtag':hashtag})

def detailsocial(request, pk_id): #글 상세보기
    post = get_object_or_404(socialPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentsocial(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(socialPost, pk=pk_id)

        social = socialComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        social.save()
        context = {
            'content':social.comment_contents,
            'user': social.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')


#--------------------------자연대
def natural(request): #글리스트
    post = naturalPost.objects.all()
    hashtag = naturalTags.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post, 'hashtag':hashtag})

def detailnatural(request, pk_id): #글 상세보기
    post = get_object_or_404(naturalPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentnatural(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(naturalPost, pk=pk_id)

        natural = naturalComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        natural.save()
        context = {
            'content':natural.comment_contents,
            'user': natural.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')



#--------------------------스크랜튼
def scraton(request): #글리스트
    post = scratonPost.objects.all()
    hashtag = scratonTags.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post, 'hashtag':hashtag})

def detailscraton(request, pk_id): #글 상세보기
    post = get_object_or_404(scratonPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentscraton(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(scratonPost, pk=pk_id)

        scraton = scratonComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        scraton.save()
        context = {
            'content':scraton.comment_contents,
            'user': scraton.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')




#--------------------------조예대
def art(request): #글리스트
    post = artPost.objects.all()
    hashtag = artTags.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post, 'hashtag':hashtag})

def detailart(request, pk_id): #글 상세보기
    post = get_object_or_404(artPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commentart(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(artPost, pk=pk_id)

        art = artComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        art.save()
        context = {
            'content':art.comment_contents,
            'user': art.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')


#--------------------------호크마
def hokma(request): #글리스트
    post = hokmaPost.objects.all()
    return render(request, 'boards/collegeBoards.html', {'post':post})

def detailhokma(request, pk_id): #글 상세보기
    post = get_object_or_404(hokmaPost, pk=pk_id)
    return render(request, 'details/detail.html', {'post':post})

def commenthokma(request, pk_id):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get(user_id = user_id)
        jsonObject = json.loads(request.body)
        post = get_object_or_404(hokmaPost, pk=pk_id)

        hokma = hokmaComment.objects.create(
            post = post,
            comment_writer = user,
            comment_contents = jsonObject.get('content')
        )
        hokma.save()
        context = {
            'content':hokma.comment_contents,
            'user': hokma.comment_writer.user_nickname,
        }
        return JsonResponse(context)
    else :
        return redirect('account:login')




    
        

