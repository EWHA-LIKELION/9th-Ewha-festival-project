from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import collegePost, collegeTags, boothPost, boothTags
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse

# 검색에 필요한 임포트
from django.views.generic.edit import FormView
from .forms import SearchForm
from django.db.models import Q


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
    return render(request, 'details/detail.html', {'college': college, 'detialcollegePost': detailcollegePost})


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


# 단대별 게시판에서 검색
class CollegeSearchView(FormView):
    v  v
    # forms.py에서 만든 form객체(SearchForm)를 form_class로 지정
   form_class = SearchForm
    # 사용할 템플릿(검색어를 입력하면 리스트를 보여줄 html페이지)
    template_name = 'templates/searches/search.html'

    def form_valid(self, form):  # post method로 값이 전달됐을 경우
        schWord = '%s' % self.request.POST['search_word']  # 검색어
        post_list_college = collegePost.objects.filter(Q(title__icontains=schWord) | Q(
            body__icontains=schWord)   # title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사
        ).distinct()  # 중복을 제거

        # 결과값 반환 form
        context = {}
        context['form'] = form
        context['search_term'] = schWord
        # 검색된 결과를 컨텍스트 변수에 담는다.
        context['object_list_college'] = post_list_college
        # form_valid()함수는 리다이렉트 처리를 위해 HttpResponseRedirect객체를 반환하는데 render()함수는 httpResponse객체를 반환하도록 도와준다(리다이렉트 처리 되지 않도록)
        return render(self.request, self.template_name, context)


# 부스 글 검색
class BoothSearchView(FormView):

    form_class = SearchForm
    template_name = 'templates/searches/search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list_booth = boothPost.objects.filter(Q(title__icontains=schWord) | Q(
            body__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list_booth'] = post_list_booth
        return render(self.request, self.template_name, context)


# 부스글에 댓글
@login_required(login_url='account:login')
def comment_write_booth(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(boothPost, pk=booth_id)
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
@login_required(login_url='account:login')
def comment_write_college(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(collegePost, pk=college_id)
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
