from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def inst(request):
    insts = Inst.objects.all()
    return render(request, 'instBoard.html', {'insts': insts})


def instDetail(request, id):
    inst = get_object_or_404(Inst, pk=id)
    return render(request, 'instDetail.html', {'inst': inst})


def booth(request):
    booths = Booth.objects.all()
    return render(request, 'boothBoard.html', {'booths': booths})


def boothDetail(request, id):
    booth = get_object_or_404(Booth, pk=id)
    return render(request, 'boothDetail.html', {'booth': inst})
