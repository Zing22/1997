from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.translation import ugettext_lazy as _

import json

import ast
 
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"
 
    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)
 
    def to_python(self, value):
        if not value:
            value = []
 
        if isinstance(value, list):
            return value
 
        return ast.literal_eval(value)
 
    def get_prep_value(self, value):
        if value is None:
            return value
 
        return str(value) # use str(value) in Python 3
 
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class about_us(models.Model):
    content = RichTextUploadingField()


class index_info(models.Model):
    image = models.ImageField(upload_to='index/', max_length=256)

    def image_tag(self):
        return u'<img src="%s" width="200px" />' % self.image.url

    image_tag.short_description = 'logo 预览'
    image_tag.allow_tags = True

    subtitle = models.TextField(max_length=4096)

    slider_delay = models.IntegerField()

    def __str__(self):
        return "index_info <id: %d>" % self.id


class slider(models.Model):
    image = models.ImageField(upload_to='slider/', max_length=256)

    def image_tag(self):
        return u'<img src="%s" width="200px" />' % self.image.url

    image_tag.short_description = 'slider 图片'
    image_tag.allow_tags = True

    description = models.TextField(max_length=4096)

    order = models.PositiveIntegerField()

    def __str__(self):
        return "slider <id: %d>" % self.id


class teacher(models.Model):
    name = models.CharField(max_length=265)

    MALE = 0
    FEMALE = 1
    gender = models.BooleanField(choices=((MALE,'Male'), (FEMALE,'Female')), default=MALE)

    subject = models.CharField(max_length=1024)

    school = models.CharField(max_length=512)
    college = models.CharField(max_length=512)
    grade = models.CharField(max_length=265)
    order = models.PositiveIntegerField(default=0)

    avatar = models.ImageField(upload_to='avatar/', max_length=256)
    def avatar_tag(self):
        return u'<img src="%s" width="200px" />' % self.avatar.url
    avatar_tag.short_description = '头像 图片'
    avatar_tag.allow_tags = True

    card = models.ImageField(upload_to='card/', max_length=256)
    def card_tag(self):
        return u'<img src="%s" width="200px" />' % self.card.url
    card_tag.short_description = '校园卡 图片'
    card_tag.allow_tags = True

    description = RichTextUploadingField()

    time_slot = models.TextField(max_length=4096, default='[]')

    def set_time_slot(self, x):
        self.time_slot = json.dumps(x)

    def get_time_slot(self):
        return json.loads(self.time_slot)

    def __str__(self):
        return self.name


class reservation(models.Model):
    name = models.CharField(max_length=265)
    phone_num = models.CharField(max_length=32)
    address = models.TextField(max_length=2048)

    teacher = models.ForeignKey(teacher, models.CASCADE,
                related_name="reservations");

    ctime = models.DateTimeField(auto_now=True)

    time_slot = models.TextField(max_length=4096, default='[]')

    def set_time_slot(self, x):
        self.time_slot = json.dumps(x)

    def get_time_slot(self):
        return json.loads(self.time_slot)

    UNPROCESSED = 0
    SUCCEED = 1
    EXPIRED = 2
    status = models.IntegerField(choices=((UNPROCESSED, '未处理'), 
                                        (SUCCEED, '成功'),
                                        (EXPIRED, '失效')),
                                default=UNPROCESSED)

    def __str__(self):
        return "RSV <%s to %s>" % (self.name, self.teacher.name)