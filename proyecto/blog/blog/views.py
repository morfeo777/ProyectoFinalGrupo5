from django.http import HttpResponse

from django.shortcuts import render


def contacto(request):
    return render(request, 'posts/contacto.html')

def agregar_post(request):
    return render(request, 'posts/agregar_post.html')

def acerca_de(request):
    return render(request, 'acerca_de.html')

#def saludo(request):
#    return render(request, 'index.html')

#def despedida(request):
#    return HttpResponse("Buenas Noches")