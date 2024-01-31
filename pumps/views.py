from django.shortcuts import render
from .models import Pumps
from motors.models import Motor
from couplings.models import Coupling
from bearings.models import PumpBearing
from seals.models import PumpSeal
from .models import MechanicalSeal


def list_pumps(request):
    pumps_list = Pumps.objects.all()
    motor_list = Motor.objects.all()
    coupling_list = Coupling.objects.all()
    bearing_list = PumpBearing.objects.all()
    seal_list = PumpSeal.objects.all()
    mechanicalSeal_list = MechanicalSeal.objects.all()

    for pump in pumps_list:
        pump.has_motor = Motor.objects.filter(pump=pump).exists()
        pump.has_coupling = Coupling.objects.filter(pump=pump).exists()
        pump.has_bearing = PumpBearing.objects.filter(pump=pump).exists()
        pump.has_seal = PumpSeal.objects.filter(pump=pump).exists()
        pump.has_mechanicalSeal = pump.mechanicalseal_set.exists()

    context = {
        'title': 'Bombas',
        'pumps_list': pumps_list,
        'motor_list': motor_list,
        'coupling_list': coupling_list,
        'bearing_list': bearing_list,
        'seal_list': seal_list,
        'mechanicalSeal_list': mechanicalSeal_list
    }
    return render(request, 'pumps/pumps.html', context)
