from django.shortcuts import render
from .models import Casa,Reseña,Reservas,Contacto
from Home.forms import Formulariobusquedacasa,Formulariocontacto,Formularioreserva,Formularioreseña

# Create your views here.

def index (request):
    casas= Casa.objects.all()
    return render(request,"Home/index.html",{'casas': casas})

  

def contacto(request):
 
    if request.method == "POST":
        
        micontacto = Formulariocontacto(request.POST)
        if micontacto.is_valid():
            contenidocontacto = micontacto.cleaned_data
            contacto = Contacto(nombre=contenidocontacto['nombre'],apellido=contenidocontacto['apellido'],email=contenidocontacto['email'],asunto=contenidocontacto['asunto'],mensaje=contenidocontacto['mensaje'])
            contacto.save()
            return render(request, "Home/index.html")
     
    else:
        micontacto = Formulariocontacto()
    return render(request, "Home/contacto.html",{"micontacto":micontacto})
         
    
    
    
    

def reservas(request):
    
    if request.method == "POST":
        
        mireserva = Formularioreserva(request.POST)
        if mireserva.is_valid():
            contenidoreserva = mireserva.cleaned_data
            reserva = Reservas(nombrecompleto=contenidoreserva['nombrecompleto'],Telefono=contenidoreserva['telefono'],Email=contenidoreserva['Email'],Dia_Check_In=contenidoreserva['Dia_Check_In'],Dia_Check_Out=contenidoreserva['Dia_Check_Out'],Adultos=contenidoreserva['Adultos'],Niños=contenidoreserva['Niños'],Nota=contenidoreserva['Nota'])
            reserva.save()
            return render(request, "Home/index.html")
     
    else:
        mireserva = Formularioreserva()
    return render(request, "Home/reservar.html",{"mireserva":mireserva})

def reseña(request):
    if request.method == "POST":
        
        mireseña = Formularioreseña(request.POST)
        if mireseña.is_valid():
            contenidoreseña = mireseña.cleaned_data
            reseña = Reseña(nombre=contenidoreseña['nombre'],reseña=contenidoreseña['reseña'])
            reseña.save()
            return render(request, "Home/index.html")
     
    else:
        mireseña = Formularioreseña()
    return render(request, "Home/reseñas.html",{"mireseña":mireseña})















def buscar_casa(request):
    listado_casas= Casa.objects.all()
       
    
    if request.GET.get("nombre_casa"):
        
        formulario = Formulariobusquedacasa(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_casas=Casa.objects.filter(nombre__icontains =  data("nombre_casa"))
        
        
        return render(request,"Home/casas.html",{'casas': listado_casas,"formulario":formulario})
    
    else:
        formulario = Formulariobusquedacasa()

        return render(request,"Home/casas.html",{'casas': listado_casas,"formulario":formulario})



def acercade(request):
    pass


