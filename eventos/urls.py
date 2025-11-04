from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro_evento, name='registro_evento'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('evento/<int:evento_id>/registrar_participante/', views.registrar_participante, name='registrar_participante'),
    path('dashboard/', views.dashboard_eventos, name='dashboard_eventos'),
]