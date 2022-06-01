from django.shortcuts import render
from colecciones.models import Novelas, Comics, Mangas
from django.http import HttpResponse
from colecciones.forms import Novelas_formularios, Comics_formularios, Mangas_formularios

def home_view(request,*args, **kwargs):
    return render( request, "home.html" )
   
def inicio(request):
    return render( request , "index.html")

def novelas(request):
    return render (request, "novelas.html")  

def comics(request):
    return render (request, "comics.html")    

def mangas(request):
    return render (request, "mangas.html")  

def novelas_formulario(request):
    
    if request.method == "POST":

      
        novelas = Novelas( titulo=request.POST['titulo'], autor=request.POST['autor'], editorial=request.POST['editorial'])
        novelas.save()

      
        return render (request , "novelas_formulario.html")

    
    return render( request, "novelas_formulario.html")

def comics_formulario(request):

   if request.method == "POST":
        
        comics = Comics( titulo=request.POST['titulo'], numero=request.POST['numero'], guionista=request.POST['guionista'], dibujante=request.POST['dibujante'], editorial=request.POST['editorial'])
        comics.save()
        return render (request , "comics_formulario.html")

   return render( request, "comics_formulario.html")

def mangas_formulario(request):

    if request.method == "POST":
        
        mangas = Mangas( titulo=request.POST['titulo'], numero=request.POST['numero'], autor=request.POST['autor'], editorial=request.POST['editorial'])
        mangas.save()
        return render (request , "mangas_formulario.html")


    return render( request, "mangas_formulario.html")


def buscar_novelas(request):
    
    return render(request, "buscar_novelas.html")

def buscar_comics(request):
    
    return render(request, "buscar_comics.html")

def buscar_mangas(request):
    
    return render(request, "buscar_mangas.html")

def busqueda_novelas(request):

    if request.GET['titulo']:
        titulo = request.GET['titulo']
        novelas = Novelas.objects.filter(titulo__contains= titulo)
        return render( request, "resultado_busqueda_novelas.html", {"novelas": novelas} )

    else:
        return HttpResponse("Campo vacío")
       

def busqueda_comics(request):

    if request.GET['titulo']:
        titulo = request.GET['titulo']
        comics = Comics.objects.filter(titulo__contains= titulo)
        return render( request, "resultado_busqueda_comics.html", {"comics": comics} )

    else:
        return HttpResponse("Campo vacío")
  

def busqueda_mangas(request):

    if request.GET['titulo']:
        titulo = request.GET['titulo']
        mangas = Mangas.objects.filter(titulo__contains= titulo)
        return render( request, "resultado_busqueda_mangas.html", {"mangas": mangas} )

    else:
        return HttpResponse("Campo vacío")
        
   
