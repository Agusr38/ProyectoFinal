from django.urls import path
from mensajes.views import *

urlpatterns = [
    path('', MensajesList.as_view(), name='mensajes_list'),
    path('enviar/',mensaje_send, name='mensajes_send')
    ]