from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib import messages
from .models import Pumps
from motors.models import Motor
from couplings.models import Coupling
from bearings.models import PumpBearing
from seals.models import PumpSeal
from .models import MechanicalSeal
from .models import Packing
from .forms import PumpsForm


# Create your views here.
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
        return render(request, 'pumps/load_pumps.html', context)


class ListPumps(View):
    template = 'pumps/pumps.html'

    def get(self, request):
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
        return render(request, self.template, context)


def pump_detail(request, pump_id):
    template = 'pumps/pump_detail.html'
    pump = get_object_or_404(Pumps, pk=pump_id)

    motor = pump.motor_set.first()
    coupling = pump.coupling_set.first()
    bearing = pump.bearings.all()
    seal = pump.seal.all()
    mechanicalSeal = pump.mechanicalseal_set.first()
    packing = pump.packing_set.first()

    if motor:
        motor_bearings = motor.bearings.all()
    else:
        motor_bearings = []

    if motor:
        motor_seals = motor.seal.all()
    else:
        motor_seals = []

    context = {
        'pump': pump,
        'motor': motor,
        'coupling': coupling,
        'pump_bearings': bearing,
        'pump_seal': seal,
        'mechanicalSeal': mechanicalSeal,
        'packing': packing,
        'motor_bearings': motor_bearings,
        'motor_seals': motor_seals,
    }
    return render(request, template, context)


class ListMechanicalSeal(View):
    template = 'pumps/mechanical_seals.html'

    def get(self, request):
        mechanicalseal_list = MechanicalSeal.objects.all()

        context = {
            'title': 'Sellos Mecánico',
            'mechanicalseal_list': mechanicalseal_list,
        }
        return render(request, self.template, context)


def mechanicalseal_detail(request, mechanicalseal_id):
    template = 'pumps/mechanicalseal_detail.html'
    mechanicalseal = get_object_or_404(MechanicalSeal, pk=mechanicalseal_id)

    context = {
        'mechanicalseal': mechanicalseal,
    }

    return render(request, template, context)


class ListPacking(View):
    template = 'pumps/packing.html'

    def get(self, request):
        packing_list = Packing.objects.all()

        context = {
            'title': 'Empaquetaduras',
            'packing_list': packing_list,
        }
        return render(request, self.template, context)


def packing_detail(request, packing_id):
    template = 'pumps/packing_detail.html'
    packing = get_object_or_404(Packing, pk=packing_id)

    context = {
        'packing': packing,
    }

    return render(request, template, context)
