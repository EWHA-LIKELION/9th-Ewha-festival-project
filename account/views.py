from festival.views import business
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.db import transaction
from django.views import generic
from account.models import Profile
from .forms import RegisterForm, LoginForm
from booth.models import boothComment, boothPost
from committee.models import committeeComment
from festival.models import *
from django.views.generic.base import View

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
       



def login(request):
    loginform = LoginForm()
    context ={'forms': loginform}

    if request.method =='GET':
        return render(request,'auths/login.html', context)
    
    elif request.method =='POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
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
    return render(request, 'auths/login.html', context)



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


@login_required(login_url='account:login')
def myboothComment(request, pk_id):
    commentbooth = boothComment.objects.all()
    user = get_object_or_404(Profile, pk = pk_id )
    commentboothList = commentbooth.filter(comment_writer = user)
    return render(request, 'auths/commentedBoothBoards.html', {'commentboothList':commentboothList})


@login_required(login_url='account:login')
def mycommitteeComment(request, pk_id):
    commentcommittee = committeeComment.objects.all()
    user = get_object_or_404(Profile, pk=pk_id)
    committeepostList = commentcommittee.filter(comment_writer = user)
    return render(request, 'auths/commentedPostBoards.html', {'committepostList':committeepostList})

@login_required(login_url='account:login')
def mypostComment(request, pk_id):
    user = get_object_or_404(Profile, pk=pk_id)

    nursing = nursingComment.objects.all()
    convergence = convergenceComment.objects.all()
    business = businessComment.objects.all()
    pharmacy = pharmacyComment.objects.all()
    engineering = engineeringComment.objects.all()
    music = musicComment.objects.all()
    edu = eduComment.objects.all()
    humanities = humanitiesComment.objects.all()
    social = socialComment.objects.all()
    natural = naturalComment.objects.all()
    scraton = scratonComment.objects.all()
    art = artComment.objects.all()
    hokma = hokmaComment.objects.all()
    
    nursingList = nursing.filter(comment_writer = user)
    convergenceList = convergence.filter(comment_writer = user)
    businessList = business.filter(comment_writer = user)
    pharmacyList = pharmacy.filter(comment_writer = user)
    engineeringList = engineering.filter(comment_writer = user)
    musicList = music.filter(comment_writer = user)
    eduList = edu.filter(comment_writer = user)
    humanitiesList = humanities.filter(comment_writer = user)
    socialList = social.filter(comment_writer = user)
    naturalList = natural.filter(comment_writer = user)
    scratonList = scraton.filter(comment_writer = user)
    artList = art.filter(comment_writer = user)
    hokmaList = hokma.filter(comment_writer = user)


    context = {
        'nursingList' : nursingList,
        'convergenceList' : convergenceList,
        'businessList' : businessList,
        'pharmacyList' : pharmacyList,
        'engineeringList' : engineeringList,
        'musicList' : musicList,
        'eduList' : eduList,
        'humanitiesList' : humanitiesList,
        'socialList' : socialList,
        'naturalList' : naturalList,
        'scratonList' : scratonList,
        'artList' : artList,
        'hokmaList' : hokmaList,
    }

    return render(request, 'auths/commentedPostBoards.html', context)

def myLike(request):
    user_id = request.session.get('user')
    if user_id:
        user = Profile.objects.get(user_id = user_id)
        mylike = user.booth_like.all()
        return render(request, 'auths/likedBoothBoards.html', {'mylike':mylike})
    else :
        return redirect('account:login')


