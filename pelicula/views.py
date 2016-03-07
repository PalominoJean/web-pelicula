from django.shortcuts import render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from pelicula.models import Pelicula
from django.utils import timezone


# Create your views here.
def lista_fechaAdicion(request):
    lista_peliculas=Pelicula.objects.all().order_by('-fecha_publicacion')
    paginador=Paginator(lista_peliculas,12)
    page=request.GET.get('page')
    try:
        peliculas=paginador.page(page)
    except PageNotAnInteger:
        peliculas=paginador.page(1)
    except EmptyPage:
        peliculas=paginador.page(paginador.num_pages)
    return render(request,'pelicula/lista_fechaAdicion.html',{'peliculas':peliculas,'paginador':paginador})



