from django.shortcuts import render
from .models import Casa,Reseña,Reservas

# Create your views here.

def index (request):
    casas= Casa.objects.all()
    reseñas= Reseña.objects.all()
    reservas = Reservas.objects.all()

    return render(request,"Home/index.html",{'casas': casas})
