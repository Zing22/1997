from web.models import *
from django.shortcuts import get_object_or_404

def get_index_info():
    return {
        'header': index_info.objects.all()[0],
        'sliders': slider.objects.all().order_by('order')
    }


def get_teacher_of(_id):
    return get_object_or_404(teacher, id=_id)