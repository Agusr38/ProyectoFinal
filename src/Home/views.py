from django.shortcuts import render
from .models import Casa,Reseña,Reservas,Contacto
from Home.forms import Formulariobusquedacasa

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