from django.contrib import admin

from .models import *


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'time_created')
    search_fields = ('time_created',)
    list_filter = ('time_created',)
