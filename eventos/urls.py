from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro_evento, name='registro_evento'),
]