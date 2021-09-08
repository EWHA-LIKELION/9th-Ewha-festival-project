from festival.views import business
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.db import transaction
from django.views import generic
from account.models import Profile
from .forms import RegisterForm, LoginForm
from booth.models import boothComment, boothPost
from committee.models import committeeComment,committeePost
from festival.models import *
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlparse

# Create your views here.
def main(request):
    return render(request, "frontScreens/main.html")

def signup(request):
    register_form = RegisterForm()
    context = {'forms': register_form}

    if request.method =='GET':
        return render(request, 'auths/signup.html', context)

    elif request.method =='POST':
        register_form = RegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.user_image = request.FILES['user_image'],
            register_form.user_id = request.POST.get('user_id'),
            register_form.user_pw = request.POST.get('user_pw'),
            register_form.user_email = request.POST.get('user_email'),
            register_form.user_name = request.POST.get('user_image'),
            register_form.user_nickname = request.POST.get('user_nickname'),
            register_form.user_phone = request.POST.get('user_phone'),
            register_form.save()
            return redirect('/')
        else:
            context['forms'] = register_form
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'auths/signup.html', context)
       

@csrf_exempt
def login(request):
    loginform = LoginForm()
    context ={'forms': loginform}

    if request.method =='GET':
        return render(request,'auths/login.html', context)
    
    elif request.method =='POST':
        loginform = LoginForm(request.POST)
        loginform.user_id = request.POST.get('user_id')
        
        if loginform.user_id :
            loginform.user_id = request.POST.get('user_id')
            loginform.user_pw = request.POST.get('user_pw')

            request.session['user'] = loginform.user_id
            request.session.set_expiry(0) #브라우저 닫을 시 세션 쿠키 삭제
            return redirect('main') #유효성검사 통과시 홈으로 
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value          

def logout(request):
    request.session.flush()
    return redirect('main')

def mypage(request):
    user_id = request.session.get('user')
    if user_id :
        user = Profile.objects.get( user_id = user_id)
        return render(request, 'auths/myPage.html', {'user':user})
    else :
        return redirect('account:login')



def filterPost(college,collegeAll,user):
    commentPostList = collegeAll.filter(comment_writer = user).order_by('post_id')
    print(commentPostList.values())
    filtered = commentPostList.values_list('post_id',flat=True).distinct()
    filteredPost = college.filter(id__in=filtered)
    return filteredPost

def myboothComment(request):
    user_id = request.session.get('user')
    if not user_id:
        return redirect('account:login')

    else :
        user = Profile.objects.get(user_id = user_id)
        boothAll = boothPost.objects.all()
        commentbooth = boothComment.objects.all()

        filteredBooth =filterPost(boothAll,commentbooth,user)
        return render(request, 'auths/commentedBoothBoards.html', {'commentboothList':filteredBooth})


def mypostComment(request):
    user_id = request.session.get('user')
    if not user_id:
        return redirect('account:login')

    else :
        user = Profile.objects.get(user_id = user_id)

        #committee에서 댓글

        committeeAll =committeePost.objects.all()
        committee = committeeComment.objects.all()
        committeeList = filterPost(committeeAll,committee,user)

        #festival에서 글
        nursingAll = nursingPost.objects.all()
        convergenceAll = convergencePost.objects.all()
        businessAll = businessPost.objects.all()
        pharmacyAll = pharmacyPost.objects.all()
        engineeringAll = engineeringPost.objects.all()
        musicAll = musicPost.objects.all()
        humanitiesAll = humanitiesPost.objects.all()
        eduAll = eduPost.objects.all()
        socialAll = socialPost.objects.all()
        naturalAll = naturalPost.objects.all()
        scratonAll = scratonPost.objects.all()
        artAll = artPost.objects.all()
        hokmaAll = hokmaPost.objects.all()

        context = {
            'committeeList' : committeeList,
            'nursingList' : filterPost(nursingAll,nursing,user),
            'convergenceList' :  filterPost(convergenceAll,convergence,user),
            'businessList' :  filterPost(businessAll,business,user),
            'pharmacyList' :  filterPost(pharmacyAll,pharmacy,user),
            'engineeringList' :  filterPost(engineeringAll,engineering,user),
            'musicList' :  filterPost(musicAll,music,user),
            'eduList' :  filterPost(eduAll,edu,user),
            'humanitiesList' :  filterPost(humanitiesAll,humanities,user),
            'socialList' :  filterPost(socialAll,social,user),
            'naturalList' :  filterPost(naturalAll,natural,user),
            'scratonList' :  filterPost(scratonAll,scraton,user),
            'artList' :  filterPost(artAll,art,user),
            'hokmaList' :  filterPost(hokmaAll,hokma,user),


        return render(request, 'auths/commentedPostBoards.html', context)

def myLike(request):
    user_id = request.session.get('user')
    if user_id:
        user = Profile.objects.get(user_id = user_id)
        mylike = user.booth_like.all()
        return render(request, 'auths/likedBoothBoards.html', {'mylike':mylike})
    else :
        return redirect('account:login')

