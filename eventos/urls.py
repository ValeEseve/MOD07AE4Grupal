from django.urls import path
from . import views

urlpatterns = [
    path('registro_evento', views.registrar_evento, name='registrar_evento'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('evento/<int:evento_id>/registrar_participante/', views.registrar_participante, name='registrar_participante'),
    path('', views.dashboard_eventos, name='dashboard_eventos'),
    path('borrar/<int:evento_id>/', views.borrar_evento, name='borrar_evento'),
]