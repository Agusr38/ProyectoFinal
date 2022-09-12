from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from mensajes.models import *
from mensajes.forms import *
# Create your views here.
class MensajesList(LoginRequiredMixin, ListView):

    model = Mensajes
    template_name = "mensajes/mensajes_list.html"


@login_required
def mensaje_send(request):

    if request.method == "GET":
        form = MensajesForm()
        return render(request, "mensajes/mensajes_send.html", {"form": form})

    else:
        form = MensajesForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = User.objects.filter(username=request.user.username).first()
            texto = data["mensajes"]

            mensaje = Mensajes(usuario=usuario, mensaje=texto)

            mensaje.save()

            return redirect("mensajes_list")

        else:
            context = {
                "form": form,
                "error": "Formulario no válido"
            }

            return render(request, "mensajes/mensajes_send.html", context)