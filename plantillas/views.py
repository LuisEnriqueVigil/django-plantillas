
from django.shortcuts import render ## UTIL PARA RENDERIZAR EL CONTENIDO PLANTILLA HMTL


def simple (request): 
    return render(
        request= request, 
        template_name= 'simple.html',
        context={}
    )

def dinamico (request,name):
    ##CREANDO LA VARIBALE DEL CONTEXTO
    ##TAMBIEN PODEMOS PASAR OBJETOS ATRAVEZ DEL CONTEXTO 
    ## Y USAR SUS METODOS
    categories = ["code","desing","marketing","UX/UI"]
    context = {
        'name' : name, 
        "categories": categories
    }
    return render(
        request= request,
        template_name="dinamico.html",
        context= context
    )