from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    Navbars = Navbar.objects.all()
    Titulonav = TituloNav.objects.all()
    context = {
        "Navbars": Navbars,
        "Titulonav": Titulonav
    }
    return render(request, 'core/index.html', context)

def sobreNosotros(request):
    Navbars = Navbar.objects.all()
    Titulonav = TituloNav.objects.all()
    context = {
        "Navbars": Navbars,
        "Titulonav": Titulonav
    }
    return render(request, 'core/sobrenosotros.html', context)

def servicios(request):
    Navbars = Navbar.objects.all()
    Titulonav = TituloNav.objects.all()
    context = {
        "Navbars": Navbars,
        "Titulonav": Titulonav
    }
    return render(request, 'core/servicios.html', context)