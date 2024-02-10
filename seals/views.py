from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import PumpSeal
from .models import MotorSeal
from .models import Seal


# Create your views here.
class ListSeals(View):
    template = 'seals/seals.html'

    def get(self, request):
        pump_seals = PumpSeal.objects.all()
        motor_seals = MotorSeal.objects.all()

        seals_combined = list(pump_seals) + list(motor_seals)

        context = {
            'title': 'Retenes',
            'seals_combined': seals_combined,
        }
        return render(request, self.template, context)


def seal_detail(request, seal_id):
    template = 'seals/seal_detail.html'
    seal = get_object_or_404(Seal, pk=seal_id)

    pump_seals = seal.pump_seal.all()
    motor_seals = seal.motor_seal.all()

    list_seals = []

    for seal_pump in pump_seals:
        list_seals.append({'type': 'pump', 'object': seal_pump})

    for seal_motor in motor_seals:
        list_seals.append({'type': 'pump', 'object': seal_motor})

    context = {
        'seal': seal,
        'pump_seals': pump_seals,
        'motor_seals': motor_seals,
        'list_seals': list_seals,
    }
    return render(request, template, context)
