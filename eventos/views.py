from django.shortcuts import render
from .forms import EventoForm, ParticipanteForm
from .models import Evento, Participante


def registro_evento(request):
    # mensaje por defecto (None evita error si el template lo espera)
    mensaje = None  

    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        participante_form = ParticipanteForm(request.POST)

        if evento_form.is_valid() and participante_form.is_valid():
            nombre_evento = evento_form.cleaned_data['nombre']
            fecha_evento = evento_form.cleaned_data['fecha']
            ubicacion_evento = evento_form.cleaned_data['ubicacion']
            nombre_participante = participante_form.cleaned_data['nombre']
            email_participante = participante_form.cleaned_data['email']

            evento = Evento.objects.create(
                nombre=nombre_evento,
                fecha=fecha_evento,
                ubicacion=ubicacion_evento
            )
            participante = Participante.objects.create(
                nombre=nombre_participante,
                email=email_participante
            )
            evento.participantes.add(participante)

            mensaje = "Evento y participante registrados correctamente."

            evento_form = EventoForm()
            participante_form = ParticipanteForm()

    else:
        evento_form = EventoForm()
        participante_form = ParticipanteForm()

    return render(request, 'eventos/registro.html', {
        'evento_form': evento_form,
        'participante_form': participante_form,
        'mensaje': mensaje
    })
