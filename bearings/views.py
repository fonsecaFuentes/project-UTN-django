from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import PumpBearing
from .models import MotorBearing
from .models import Bearing


# Create your views here.
class ListBearings(View):
    template = 'bearings/bearings.html'

    def get(self, request):
        pump_bearings = PumpBearing.objects.all()
        motor_bearings = MotorBearing.objects.all()

        bearings_combined = list(pump_bearings) + list(motor_bearings)

        context = {
            'title': 'Rodamientos',
            'bearings_combined': bearings_combined
        }
        return render(request, self.template, context)


def bearing_detail(request, bearing_id):
    template = 'bearings/bearings_detail.html'
    bearing = get_object_or_404(Bearing, pk=bearing_id)

    pump_bearings = bearing.pump_bearings.all()
    motor_bearings = bearing.motor_bearings.all()

    list_bearings = []

    for bearing_pump in pump_bearings:
        list_bearings.append({'type': 'pump', 'object': bearing_pump})
    for bearing_motor in motor_bearings:
        list_bearings.append({'type': 'motor', 'object': bearing_motor})

    context = {
        'bearing': bearing,
        'pump_bearings': pump_bearings,
        'motor_bearings': motor_bearings,
        'list_bearings': list_bearings,
    }
    return render(request, template, context)
