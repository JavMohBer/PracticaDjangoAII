from django.conf.urls import url

from . import views

# Aquí pondremos las urls de las plantillas que crearemos

urlpatterns = [
    url(r'^ejemplo/$', views.ejemplo),
    url(r'^inicio/$', views.inicio),
]