from django.shortcuts import render
from django.http import JsonResponse
from web.models import *
from .database_lib import *
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

def index(request):
    return render(request, "web/index.html", {'info': get_index_info()})

def detail(request):
    teacher = get_teacher_of(request.GET.get('id'))
    # print(type())
    # teacher.settime_slot(['周六下午'])
    # teacher.save()
    return render(request, "web/detail.html", {'teacher': teacher,
                            'slots': teacher.get_time_slot()})


def teachers(request):
    return render(request, "web/teachers.html")


def about(request):
    return render(request, "web/about.html", {'ab': about_us.objects.all()[0]})


@login_required()
def teacher_slot(request):
    ts = teacher.objects.all()
    return render(request, "web/teacher_slot.html", {'ts': ts})


@login_required()
def detail_slot(request, mothods=['GET', 'POST']):
    if request.method == 'POST':
        print(request.POST.get('id'))
        te = get_teacher_of(request.POST.get('id'))
        te.set_time_slot(json.loads(request.POST.get('slots')))
        te.save()
        return JsonResponse({'code':0})
    teacher = get_teacher_of(request.GET.get('id'))
    return render(request, "web/detail_slot.html", {'t': teacher,
                            'slots': teacher.get_time_slot()})