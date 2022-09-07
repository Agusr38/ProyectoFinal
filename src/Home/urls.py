from django.urls import path
from Home.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",index,name="inicio"),
    path("casas/",buscar_casa,name="casas"),
    path("casas/<pk>",CasaDetail.as_view(),name="casadetail"),
   
   
    path("contacto/",contacto,name="contacto"),
  
  
    path("reservar/",reservas,name="reservas"),
    
    
    path("reseñas/",reseña,name="reseñas"),
    path("reseñas/borrar/<id_reseña>",borrar_reseña,name="borrarreseña"),
    path("reseñas/editar/<pk>",Updatereseña.as_view(),name="editarreseña"),

    path("login/",iniciosesion, name="login"),
    path("register/",registrar_usuario, name="register"),
    path("logout/",LogoutView.as_view(template_name="Home/logout.html"), name="logout"),
    path("edit/",editar_usuario, name="editar_usuario"),
]