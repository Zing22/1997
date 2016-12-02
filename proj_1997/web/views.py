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
    info = [{'ts': t, 'slots': t.get_time_slot()} for t in ts]
    return render(request, "web/teacher_slot.html", {'info': info})


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


@login_required()
def rsv_manage(request):
    rsvs = reservation.objects.all()
    info = [{'rsv': t, 'slots': t.get_time_slot()} for t in rsvs]
    return render(request, "web/rsv_manage.html", {'info': info})



def new_reservation(request, method=['POST']):
    # check code
    phone_num = request.POST.get("phone_num")
    print(request.session.get(phone_num), request.POST.get("code"))
    if request.session.get(phone_num) != request.POST.get("code"):
        return JsonResponse({
                'code': 1,
                'msgs': ['验证码错误']
            })

    name = request.POST.get("name")
    address = request.POST.get("address")
    teacher = get_teacher_of(request.POST.get("id"))
    time_slot = json.loads(request.POST.get("time_slot"))

    rsv = reservation(name=name, phone_num=phone_num, address=address, teacher=teacher)
    rsv.set_time_slot(time_slot)

    rsv.save()

    request.session.pop(phone_num);
    return JsonResponse({'code': 0})


from datetime import datetime
import random
def send_code(request, method=['POST']):
    if request.session.get("last-time"):
        delta = datetime.now() - datetime.strptime(request.session["last-time"],
                                    "%Y %m %d %H %M %S")
        if delta.seconds < 120:
            return JsonResponse({"code": 1, "delta": delta.seconds})
    # do sending things
    phone_num = request.POST.get("phone_num")
    c = str(random.randint(100000, 999999))
    request.session[phone_num] = c
    print(c)

    request.session["last-time"] = datetime.now().strftime("%Y %m %d %H %M %S")
    return JsonResponse({"code": 0})