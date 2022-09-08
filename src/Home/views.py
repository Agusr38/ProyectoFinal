from django.shortcuts import render,HttpResponse,redirect
from .models import Casa,Reseña,Reservas,Contacto,Avatar
from Home.forms import Formulariobusquedacasa,Formulariocontacto,Formularioreserva,Formularioreseña,UserEditForm
from django.views.generic import ListView,DetailView,UpdateView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import logout,authenticate,login
from Home.forms import UserCustomCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
        
    casas= Casa.objects.all()
    return render(request,"Home/index.html",{'casas': casas})

  
#Contacto

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
         
    
    
    
#Rerservas    
@login_required
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




 








#Reseñas

def reseña(request):
    
    
       
    if request.method == "POST":
        
        mireseña = Formularioreseña(request.POST)
        if mireseña.is_valid():
            contenidoreseña = mireseña.cleaned_data
            reseña = Reseña(nombre=contenidoreseña['nombre'],reseña=contenidoreseña['reseña'])
            reseña.save()
            mireseña = Formularioreseña()
            reseñas= Reseña.objects.all()
            return render(request, "Home/reseñas.html",{"mireseña":mireseña,"reseñas":reseñas})
     
    else:
        mireseña = Formularioreseña()
        reseñas= Reseña.objects.all()
    return render(request, "Home/reseñas.html",{"mireseña":mireseña,"reseñas":reseñas})

def borrar_reseña(request, id_reseña):
    try:
        resenia = Reseña.objects.get(id = id_reseña)
        resenia.delete()
        return HttpResponse(f"Borraste la reseña de  {resenia}")
    except:
        return HttpResponse("No existe esa reseña")


class Updatereseña(LoginRequiredMixin,UpdateView):
    model = Reseña
    success_url ="/home/reseñas/"
    fields =  ['nombre','reseña']
    template_name ="Home/editarreseña.html"

class ReseñaDetail(DetailView):
    pass


#Casas


def buscar_casa(request):
    listado_casas= Casa.objects.all()
       
    
    if request.GET.get("nombre_casa"):
        
        formulario = Formulariobusquedacasa(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_casas=Casa.objects.filter(nombre__icontains =  data["nombre_casa"])
        
        
        return render(request,"Home/casas.html",{'casas': listado_casas,"formulario":formulario})
    
    else:
        formulario = Formulariobusquedacasa()

        return render(request,"Home/casas.html",{'casas': listado_casas,"formulario":formulario})




class CasasList(ListView):

    model = Casa
    template_name = "Home/casas_list.html"

class CasaDetail(DetailView):
    model = Casa
    template_name = "Home/casa_detail.html"





#Blog


class BlogDetail(DetailView):
    pass



def acercade(request):
    pass


def iniciosesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()
        context = {
            "form":formulario
        }
        return render (request,"home/login.html",context)

    else:
        formulario = AuthenticationForm(request,data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data.get("username"),password=data.get("password"))

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                context={
                    "error":"Credenciales no validas",
                    "form": formulario
                }
                return render(request,"home/login.html",context)

        else:
            
            context={
                "error":"Formulario no valido",
                "form": formulario
            }
            return render(request,"home/login.html",context)
    

def registrar_usuario(request):
    if request.method == "GET":
        formulario = UserCustomCreationForm()
        return render(request,"home/registro.html",{"form":formulario})
    else:
        formulario = UserCustomCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request,"home/registro.html",{"form":formulario,"error":"Formulario no valido"})



@login_required
def editar_usuario(request):

    if request.method == "GET":
        form = UserEditForm(initial={"email":request.user.email,"username":request.user.username,"first_name":request.user.first_name,"last_name":request.user.last_name})
        return render(request,"Home/update_user.html",{"form":form})
    else:
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data

            usuario = request.user

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            
            usuario.save()
            return redirect("inicio")
        return render(request,"Home/update_user.html",{"form":form})