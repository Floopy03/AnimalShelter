from django.urls import path 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [ 
    path('', views.main, name = 'start'),
    path('onse/', views.second, name = 'onse_animal')

    ]