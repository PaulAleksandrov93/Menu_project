from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent__isnull=True)

    def draw_children(menu_item):
        children = menu_item.children.all()
        result = f'<li><a href="{menu_item.url}">{menu_item.title}</a>'
        if children:
            result += '<ul>'
            for child in children:
                result += draw_children(child)
            result += '</ul>'
        result += '</li>'
        return result

    menu_html = ''
    for item in menu_items:
        menu_html += draw_children(item)

    return f'<ul>{menu_html}</ul>'