from django import template


register = template.Library()

@register.inclusion_tag('tags/draw_index_menu.html')
def draw_index_menu(menu):
    return {'menu': menu}