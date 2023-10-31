from django import template
import photo.views as views

register = template.Library()


@register.simple_tag()
def get_photo():
    return views.photo_db


def show_photo():
    return views.photo_db
