from django.urls import path
from . import views

urlpatterns = [
    path('home/<str:menu_name>/', views.home, name='home'),
    path('about/<str:menu_name>/', views.about, name='about'),
]