from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animals/', views.animals, name='animals'),
    path('equipements/', views.equipements, name='equipaments'),
    path('animal/<str:id_animal>/', views.animal_detail, name='animal_detail'),
    path('animal/<str:id_animal>/?<str:message>', views.animal_detail, name='animal_detail_mes'),
]