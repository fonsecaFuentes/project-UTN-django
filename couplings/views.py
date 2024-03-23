from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import View
from .models import Coupling
from .forms import CouplingForm
from pumps.models import Pumps
from motors.models import Motor


# Create your views here.
def add_coupling(request, pump_id, motor_id):
    template_name = 'couplings/add_coupling.html'
    pump = get_object_or_404(Pumps, pk=pump_id)
    motor = get_object_or_404(Motor, pk=motor_id)

    if request.method == 'POST':
        coupling_form = CouplingForm(request.POST, request.FILES)
        if coupling_form.is_valid():
            coupling = coupling_form.save(commit=False)
            coupling.pump = pump
            coupling.motor = motor
            coupling.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        coupling_form = CouplingForm()

    context = {'coupling_form': coupling_form, 'pump': pump, 'motor': motor}

    return render(request, template_name, context)


def add_coupling_list(request):
    template_name = 'couplings/add_coupling_list.html'

    if request.method == 'POST':
        coupling_form = CouplingForm(request.POST, request.FILES)
        if coupling_form.is_valid():
            coupling = coupling_form.save(commit=False)

            pump_selected = request.POST.get('pump', None)
            motor_selected = Motor.objects.get(pump=pump_selected)

            if pump_selected:
                pump_selected = Pumps.objects.get(pk=pump_selected)
                coupling.pump = pump_selected

                coupling.motor = motor_selected
                coupling.save()

                messages.success(
                    request, '¡Los datos se han almacenado exitosamente!'
                )
                return redirect('motors')
            else:
                messages.error(request, '¡Debe seleccionar una bomba!')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        coupling_form = CouplingForm()

    pumps_with_motor_and_coupling = Pumps.objects.filter(
        motor__isnull=False, coupling__isnull=True
    )

    context = {
        'coupling_form': coupling_form,
        'pumps_with_motor_and_coupling': pumps_with_motor_and_coupling
    }

    return render(request, template_name, context)


class ListCoupling(View):
    template = 'couplings/coupling.html'

    def get(self, request):
        coupling_list = Coupling.objects.all()

        pumps_with_motor_and_coupling = Pumps.objects.filter(
            motor__isnull=False, coupling__isnull=True
        )

        context = {
            'title': 'Acoples',
            'coupling_list': coupling_list,
            'pumps_with_motor_and_coupling': pumps_with_motor_and_coupling
        }
        return render(request, self.template, context)


def coupling_detail(request, coupling_id):
    template = 'couplings/coupling_detail.html'
    coupling = get_object_or_404(Coupling, pk=coupling_id)

    context = {
        'coupling': coupling,
    }

    return render(request, template, context)
