from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.animals, name='animals'),
    path('', views.equipements, name='equipaments'),
]