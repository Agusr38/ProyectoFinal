from django.urls import path
from Home.views import *

urlpatterns = [
    path("",index),
    path("casas/",buscar_casa),
    path("contacto/",contacto),
    path("reservar/",reservas),
]