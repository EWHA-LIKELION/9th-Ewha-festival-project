from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import transaction
from django.views import generic
from .models import User
from account.models import User
from .forms import RegisterForm, LoginForm
from booth.models import boothComment, boothPost
from committee.models import committeeComment
from festival.models import *


# Create your views here.
def main(request):
    return render(request, "frontScreens/main.html")

def signup(request):
    register_form = RegisterForm()
    context = {'forms': register_form}

    if request.method =='GET':
        return render(request, 'auths/signup.html', context)

    elif request.method =='POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = User (
                user_id = register_form.user_id,
                user_pw = register_form.user_pw,
                user_name = register_form.user_name,
                user_nickname = register_form.user_nickname,
                user_email = register_form.user_email
            )
            user.save()
            return redirect('/')
        else:
            context['forms'] = register_form
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'auths/signup.html', context)

def mypage(request):
    return render(request, "auths/mypage.html")

def login(request):
    loginform = LoginForm()
    context ={'forms': loginform}

    if request.method =='GET':
        return render(request,'auths/login.html', context)
    
    elif request.method =='POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session'] = loginform.login_session
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


def hello(request):
    context ={}

    login_session = request.session.get('login_session','') #로그인 세션 정보 갖고 있는지

    if login_session=='':
        context['login_session'] = False
    else: 
        context['login_session'] = True
    
    return render (request, 'main', context)


@login_required(login_url='account:login')
def myboothComment(request):
    commentbooth = boothComment.objects.all()
    commentboothList = commentbooth.filter(comment_writer = request.user)

    return render(request, 'auths/commentedBoothBoards.html', {'commentboothList':commentboothList})


@login_required(login_url='account:login')
def mypostComment(request):
    committeepost = committeeComment.objects.all()
    committeepostList = committeepost.filter(comment_writer = request.user)
    
    return render(request, 'auths/commentedPostBoards.html', {'committepostList':committeepostList})


class myLike(generic.ListView):
    model = boothPost
    template_name = 'auths/likedBoothBoards.html'

    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated: #로그인 확인
            messages.warning(request, '로그인을 먼저 하세요')
            return HttpResponseRedirect('/')
        return super(myLike, self).dispatch(request,*args, **kwargs)

    def get_queryset(self): #좋아요한 글 보여주기
        user = self.request.user
        queryset = user.booth_like.all()
        return queryset #좋아요한 글 전부 리턴