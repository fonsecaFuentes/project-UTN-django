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
def load_motor(request, pump_id):
    context = {}
    pump = get_object_or_404(Pumps, pk=pump_id)
    if request.method == 'POST':
        motor_form = MotorForm(request.POST, request.FILES)
        context['motor_form'] = motor_form
        if motor_form.is_valid():
            brand = motor_form.cleaned_data['brand']
            quiver = motor_form.cleaned_data['quiver']
            hp = motor_form.cleaned_data['hp']
            rpm = motor_form.cleaned_data['rpm']
            antiexplosive = motor_form.cleaned_data['antiexplosive']
            description = motor_form.cleaned_data['description']
            image = motor_form.cleaned_data['image']

            new_motor = Motor(
                brand=brand,
                quiver=quiver,
                hp=hp,
                rpm=rpm,
                antiexplosive=antiexplosive,
                description=description,
                image=image
            )
            motor = new_motor.save(commit=False)
            motor.pump = pump
            motor.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')

            


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
