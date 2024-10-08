from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def cat_decorate(name,character, color):
	cat = "{}是{}的, 颜色是{}".format(name, character, color)
	return cat


@register.simple_tag
def my_html(v1, v2):
    temp_html = "<input type='text' id='%s' class='%s' />" %(v1, v2)
    return mark_safe(temp_html)
