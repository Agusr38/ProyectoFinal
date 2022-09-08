from django.forms import Form,CharField,EmailField,DateField,IntegerField,PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class UserCustomCreationForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar Contraseña", widget=PasswordInput)

    class Meta:
        model = User
        fields =  ["username","email","password1","password2"]
        help_texts = {k : "" for k in fields}

class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar Contraseña", widget=PasswordInput)
    first_name = CharField(label="Nombre")
    last_name = CharField(label="Apellido")
    

    class Meta:
        model = User
        fields =  ["email","password1","password2","first_name","last_name"]
        help_texts = {k : "" for k in fields}
