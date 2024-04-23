from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("programas/", views.programas, name="programas"),
    path("servicios/", views.servicios, name="servicios"),
    path("contactos/", views.contactos, name="contactos"),
    path("formulario/", views.formulario, name="formulario"),
    path("suscripcion/", views.suscripcion, name="suscripcion"),


]
