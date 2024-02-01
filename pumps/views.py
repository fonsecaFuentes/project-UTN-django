from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Pumps
from motors.models import Motor
from couplings.models import Coupling
from bearings.models import PumpBearing
from seals.models import PumpSeal
from .models import MechanicalSeal
from .models import Packing
from .forms import PumpsForm


def load_pump(request):
    context = {}
    if request.method == 'POST':
        form = PumpsForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            tag = form.cleaned_data['tag']
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            types = form.cleaned_data['types']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']

            new_pump = Pumps(
                tag=tag,
                brand=brand,
                model=model,
                types=types,
                description=description,
                image=image
            )
            new_pump.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        form = PumpsForm()
        context['form'] = form
        return render(request, 'pumps/loadPumps.html', context)


def list_pumps(request):
    pumps_list = Pumps.objects.all()
    motor_list = Motor.objects.all()
    coupling_list = Coupling.objects.all()
    bearing_list = PumpBearing.objects.all()
    seal_list = PumpSeal.objects.all()
    mechanicalSeal_list = MechanicalSeal.objects.all()
    packing_list = Packing.objects.all()

    for pump in pumps_list:
        pump.has_motor = Motor.objects.filter(pump=pump).exists()
        pump.has_coupling = Coupling.objects.filter(pump=pump).exists()
        pump.has_bearing = PumpBearing.objects.filter(pump=pump).exists()
        pump.has_seal = PumpSeal.objects.filter(pump=pump).exists()
        pump.has_mechanicalSeal = pump.mechanicalseal_set.exists()
        pump.has_packing = pump.packing_set.exists()

    context = {
        'title': 'Bombas',
        'pumps_list': pumps_list,
        'motor_list': motor_list,
        'coupling_list': coupling_list,
        'bearing_list': bearing_list,
        'seal_list': seal_list,
        'mechanicalSeal_list': mechanicalSeal_list,
        'packing_list': packing_list
    }
    return render(request, 'pumps/pumps.html', context)
