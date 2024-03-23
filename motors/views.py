from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import View
from .models import Motor
from pumps.models import Pumps
from couplings.models import Coupling
from bearings.models import MotorBearing
from seals.models import MotorSeal
from .forms import MotorForm


# Create your views here.
def add_motor(request, pump_id):
    template_name = 'motors/add_motor.html'
    pump = get_object_or_404(Pumps, pk=pump_id)
    if request.method == 'POST':
        motor_form = MotorForm(request.POST, request.FILES)
        if motor_form.is_valid():
            motor = motor_form.save(commit=False)
            motor.pump = pump
            motor.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        motor_form = MotorForm()

    context = {'motor_form': motor_form, 'pump': pump}

    return render(request, template_name, context)


def add_motor_list(request):
    template_name = 'motors/add_motor_list.html'
    if request.method == 'POST':
        motor_form = MotorForm(request.POST, request.FILES)
        if motor_form.is_valid():
            motor = motor_form.save(commit=False)

            pump_selected = request.POST.get('pump', None)

            if pump_selected:
                pump_selected = Pumps.objects.get(pk=pump_selected)
                motor.pump = pump_selected

                motor.save()

                messages.success(
                    request, '¡Los datos se han almacenado exitosamente!'
                )
                return redirect('motors')
            else:
                messages.error(request, '¡Debe seleccionar una bomba!')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        motor_form = MotorForm()

    available_pumps = Pumps.objects.filter(motor__isnull=True)

    context = {
        'motor_form': motor_form,
        'available_pumps': available_pumps,
    }

    return render(request, template_name, context)


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

        available_pumps = Pumps.objects.filter(motor__isnull=True)

        context = {
            'title': 'Motores',
            'available_pumps': available_pumps,
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

    context = {
        'motor': motor,
        'coupling': coupling,
    }
    return render(request, template, context)
