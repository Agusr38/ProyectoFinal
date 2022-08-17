from django.forms import Form,CharField,EmailField

#formulario busqueda casa
class Formulariobusquedacasa(Form):
    nombre_casa = CharField(max_length=25)

#formulario contacto
class Formulariocontacto(Form):
    nombre= CharField(max_length=35)
    apellido=CharField(max_length=35)
    email=EmailField(max_length=40)
    asunto=CharField(max_length=150)
    mensaje=CharField()



#formulario reservas









#formulario reservas
