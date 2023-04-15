from django import template


register = template.Library()

@register.inclusion_tag('tags/draw_index_menu.html')
def draw_index_menu(menu):
    return {'menu': menu}

@register.inclusion_tag('tags/draw_menu.html')
def draw_menu(menu):
    return {'menu': menu}

@register.inclusion_tag('tags/show_parents.html')
def show_parents(menu):
    return {'menu': menu.parent}
        