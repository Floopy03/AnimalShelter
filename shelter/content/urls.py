from django.urls import path 
from . import views 


urlpatterns = [ 
    path('', views.main, name = 'start'),
    path('all/', views.show_all, name = 'all_animals'),
    path('one_animal/<int:animal_pk>/', views.onse_animal, name='one_animal'),
    ]