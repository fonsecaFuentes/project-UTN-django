from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Motor
from couplings.models import Coupling
from bearings.models import MotorBearing
from seals.models import MotorSeal
from .forms import MotorForm


# Create your views here.
def load_motor(request):
    context = {}
    if request.method == 'POST':
        form = MotorForm(request.POST, request.FILES)
        context['form'] = form
        if


class ListMotors(View):
    template = 'motors/motors.html'

    def get(self, request):
        motor_list = Motor.objects.all()
        coupling_list = Coupling.objects.all()
        bearing_list = MotorBearing.objects.all()
        seal_list = MotorSeal.objects.all()

        for motor in motor_list:
            motor.has_coupling = Coupling.objects.filter(motor=motor).exists()
            motor.has_bearing = MotorBearing.objects.filter(
                motor=motor
            ).exists()
            motor.has_seal = MotorSeal.objects.filter(motor=motor).exists()

        context = {
            'title': 'Motores',
            'motor_list': motor_list,
            'coupling_list': coupling_list,
            'bearing_list': bearing_list,
            'seal_list': seal_list,
        }
        return render(request, self.template, context)


def motor_detail(request, motor_id):
    template = 'motors/motor_detail.html'
    motor = get_object_or_404(Motor, pk=motor_id)

    coupling = motor.coupling_set.first()
    # bearing = motor.bearings.all()
    # seal = motor.seal.all()

    context = {
        'motor': motor,
        'coupling': coupling,
        # 'motor_bearings': bearing,
        # 'motor_seal': seal,
    }
    return render(request, template, context)
