from django.shortcuts import render
from .models import MenuItem

def get_menu(menu_name):
    return MenuItem.objects.filter(menu_name=menu_name, parent__isnull=True)


def home(request, menu_name):
    menu_items = get_menu(menu_name)
    context = {
        'menu_items': menu_items,
        'active_url': request.path
    }
    return render(request, 'menu_app/home.html', context)

def about(request, menu_name):
    menu_items = get_menu(menu_name)
    context = {
        'menu_items': menu_items,
        'active_url': request.path
    }
    return render(request, 'menu_app/about.html', context)