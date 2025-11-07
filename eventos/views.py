from django.shortcuts import get_object_or_404, redirect, render
from .forms import EventoForm, ParticipanteForm
from .models import Evento, Participante

def dashboard_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/dashboard_eventos.html', {'eventos': eventos})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    participantes = evento.participantes.all()
    return render(request, 'eventos/detalle_evento.html', {
        'evento': evento,
        'participantes': participantes
    })

def registrar_evento(request):
    mensaje = None  

    if request.method == 'POST':
        evento_form = EventoForm(request.POST)

        if evento_form.is_valid():
            nombre_evento = evento_form.cleaned_data['nombre']
            fecha_evento = evento_form.cleaned_data['fecha']
            ubicacion_evento = evento_form.cleaned_data['ubicacion']

            evento = Evento.objects.create(
                nombre=nombre_evento,
                fecha=fecha_evento,
                ubicacion=ubicacion_evento
            )
            evento.save()

            mensaje = "Evento registrado correctamente."

            evento_form = EventoForm()
            return redirect('dashboard_eventos')

    else:
        evento_form = EventoForm()

    return render(request, 'eventos/registro_eventos.html', {
        'evento_form': evento_form,
        'mensaje': mensaje
    })

# registro de participante usando el id de un evento
def registrar_participante(request, evento_id):
    mensaje = None  
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        participante_form = ParticipanteForm(request.POST)

        if participante_form.is_valid():
            nombre_participante = participante_form.cleaned_data['nombre']
            email_participante = participante_form.cleaned_data['email']

            participante = Participante.objects.create(
                nombre=nombre_participante,
                email=email_participante,
                evento=evento
            )
            participante.save()

            mensaje = "Participante registrado correctamente."

            participante_form = ParticipanteForm()
            return redirect('dashboard_eventos')
    else:
        participante_form = ParticipanteForm()

    return render(request, 'eventos/registro_participante.html', {
        'participante_form': participante_form,
        'mensaje': mensaje
    })


def borrar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    return redirect('dashboard_eventos')
