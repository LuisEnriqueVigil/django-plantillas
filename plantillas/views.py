
from django.shortcuts import render ## UTIL PARA RENDERIZAR EL CONTENIDO PLANTILLA HMTL


def simple (request): 
    return render(
        request= request, 
        template_name= 'simple.html',
        context={}
    )

def dinamico (request,name):
    ##CREANDO LA VARIBALE DEL CONTEXTO
    context = {
        'name' : name
    }
    return render(
        request= request,
        template_name="dinamico.html",
        context= context
    )