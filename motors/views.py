from django.shortcuts import render
from django.views.generic import View
from .models import Motor
from pumps.models import Pumps
from couplings.models import Coupling
from bearings.models import MotorBearing
from seals.models import MotorSeal


# Create your views here.
class ListMotors(View):
    template = 'motors/motors.html'

    def get(self, request):
        pump_list = Pumps.objects.all()
        motor_list = Motor.objects.all()
        coupling_list = Coupling.objects.all()
        bearing_list = MotorBearing.objects.all()
        seal_list = MotorSeal.objects.all()

        for motor in motor_list:
            motor.has_pump = Pumps.objects.filter(motor=motor).exists()
            motor.has_coupling = Coupling.objects.filter(motor=motor).exists()
            motor.has_bearing = MotorBearing.objects.filter(
                motor=motor
            ).exists()
            motor.has_seal = MotorSeal.objects.filter(motor=motor).exists()

        context = {
            'title': 'Motores',
            'pump_list': pump_list,
            'motor_list': motor_list,
            'coupling_list': coupling_list,
            'bearing_list': bearing_list,
            'seal_list': seal_list,
        }
        return render(request, self.template, context)
