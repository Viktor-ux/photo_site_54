from django.contrib import admin

from .models import *


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'time_created')
    search_fields = ('time_created',)
    list_filter = ('time_created',)


admin.site.register(Photo, PhotoAdmin)