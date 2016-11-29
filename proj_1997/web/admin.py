from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.about_us)

class index_info_admin(admin.ModelAdmin):
    list_display= ('id', 'image_tag', 'subtitle', 'slider_delay')
    readonly_fields = ('image_tag',)
    fields = ('image', 'image_tag', 'subtitle', 'slider_delay')

admin.site.register(models.index_info, index_info_admin)

class slider_admin(admin.ModelAdmin):
    list_display= ('image_tag', 'order', 'description',)
    readonly_fields = ('image_tag',)
    fields = ('image', 'image_tag', 'description', 'order')
    ordering = ('order', )

admin.site.register(models.slider, slider_admin)

class teacher_admin(admin.ModelAdmin):
    list_display= ('name', 'avatar_tag', 'school', 'college', 'grade', 'order')
    readonly_fields = ('avatar_tag', 'card_tag')
    # fields = ('image', 'avatar_tag', 'card_tag' 'description', 'order')
    ordering = ('order', )
    exclude = ('time_slot',)

admin.site.register(models.teacher, teacher_admin)