from django.shortcuts import render
from .utils import google_search
from .models import Usuarios
from django.http import JsonResponse
from django.shortcuts import render
from .models import ErrorLog
# Create your views here.
from django.http import HttpResponse

'''def index(request): 
    return HttpResponse("<h1> Hola Mundo! </h1>") '''

def index(request):
    return render(request, 'index.html', status= 200)

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request, exception):
    return render(request, '500.html', status=500)

def generar_error(request):
    return 7/0

def onepage (request):
    return render(request,'onepage.html',status=200)

def prueba_front(request):
    texto=request.GET.get('texto','')
    #Vamos a generar informacion en python
    objeto1 = {
        'id':'002',
        'titulo':texto,
        'descripcion':'texto generico 2'
    }
    objeto2={
        'id':'003',
        'titulo':'titulo 3',
        'descripcion':'texto generico 3'
    }
    objeto3={
        'id':'004',
        'titulo':'titulo 4',
        'descripcion':'texto generico 4'
    }
    conjunto=[objeto1,objeto2,objeto3]
    #Como mandar un objeto (variable) de python a la vista:
    #Obteber los datos de la BD
    personas = Usuarios.objects.values('id','nombres','apellidos','edad')
    listaPersonas = list(personas)
    
    return render(
        request,
        'prueba.html',
        {'objeto':objeto1,'arreglo':conjunto,'lista':listaPersonas}
    )

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})
   
def error_logs(request):
     return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})