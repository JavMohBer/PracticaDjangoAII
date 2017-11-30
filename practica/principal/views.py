#encoding:utf-8

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf.urls import include

# Create your views here.

def ejemplo(request):
    html = "<html><body>Holaa</body></html>"
    return HttpResponse(html)

def inicio(request):
    receta = "Receta"
    return render_to_response('inicio.html', {'receta':receta})