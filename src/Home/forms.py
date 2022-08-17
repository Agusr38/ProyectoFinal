from django.forms import Form,CharField,EmailField,DateField,IntegerField


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

class Formularioreserva(Form):
    nombrecompleto = CharField(max_length=35)
    Telefono = IntegerField()
    Email = EmailField(max_length=40)
    Dia_Check_In = DateField(input_formats=["yyyy-mm-dd"])
    Dia_Check_Out  = DateField(input_formats=["yyyy-mm-dd"])
    Adultos = IntegerField() 
    Niños = IntegerField()
    Nota = CharField()

#formulario reservas
class Formularioreseña(Form):
    nombre = CharField(max_length=35)
    reseña = CharField(max_length=300)