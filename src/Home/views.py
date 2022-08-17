from django.shortcuts import render
from .models import Casa,Reseña,Reservas,Contacto
from Home.forms import Formulariobusquedacasa,Formulariocontacto

# Create your views here.

def index (request):
    casas= Casa.objects.all()
    return render(request,"Home/index.html",{'casas': casas})

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
    return render(request, "Home/reservar.html")

def acercade(request):
    pass

def reseña(request):
    return request(request,"Home/reseñas.html")
