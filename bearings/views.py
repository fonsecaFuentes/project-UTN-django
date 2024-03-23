from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from django.views.generic import View
from .models import PumpBearing
from .models import MotorBearing
from .models import Bearing
from pumps.models import Pumps
from motors.models import Motor
from .forms import BearingBaseForm
from .forms import BearingForm


# Create your views here.
def add_bearing(request, pump_id=None, motor_id=None):
    template_name = 'bearings/add_bearing.html'
    print('hola')

    if request.method == 'POST':
        print('hola123')
        bearing_form = BearingBaseForm(request.POST, request.FILES)
        try:
            if bearing_form.is_valid():
                bearing_instance = bearing_form.save(commit=False)

                description = bearing_instance.description
                image = bearing_instance.image

                equipment_check = request.POST.get('equipment_check', '')
                bearing_count = int(request.POST.get('bearing_count', 0))
                print(bearing_count)

                if equipment_check == 'pump':
                    pump_id = request.POST.get('pump', None)
                    if pump_id:
                        pump = get_object_or_404(Pumps, pk=pump_id)

                        for i in range(bearing_count):
                            bearing = Bearing.objects.create(
                                types=request.POST.get(f'types_{i}'),
                                brand=request.POST.get(f'brand_{i}'),
                                side=request.POST.get(f'side_{i}'),
                                number_reference=request.POST.get(
                                    f'number_reference_{i}'
                                ),
                                inner_diameter=request.POST.get(
                                    f'inner_diameter_{i}'
                                ),
                                outer_diameter=request.POST.get(
                                    f'outer_diameter_{i}'
                                ),
                                broad=request.POST.get(f'broad_{i}'),
                                description=description,
                                image=image,
                            )
                            PumpBearing.objects.create(
                                pump=pump, bearing=bearing
                            )

                        messages.success(
                            request,
                            '¡Los datos se han almacenado exitosamente!'
                        )
                        return redirect('pumps')
                elif equipment_check == 'motor':
                    motor_id = request.POST.get('motor', None)
                    if motor_id:
                        motor = get_object_or_404(Motor, pk=motor_id)
                        for i in range(bearing_count):
                            bearing = Bearing.objects.create(
                                types=request.POST.get(f'types_{i}'),
                                brand=request.POST.get(f'brand_{i}'),
                                side=request.POST.get(f'side_{i}'),
                                number_reference=request.POST.get(
                                    f'number_reference_{i}'
                                ),
                                inner_diameter=request.POST.get(
                                    f'inner_diameter_{i}'
                                ),
                                outer_diameter=request.POST.get(
                                    f'outer_diameter_{i}'
                                ),
                                broad=request.POST.get(f'broad_{i}'),
                                description=description,
                                image=image
                            )
                            MotorBearing.objects.create(
                                motor=motor, bearing=bearing
                            )
                        messages.success(
                            request,
                            '¡Los datos se han almacenado exitosamente!'
                        )
                        return redirect('motors')
                else:
                    messages.error(
                        request, 'Debe seleccionar un equipo (bomba o motor).'
                    )
            else:
                messages.error(
                    request, '¡Hubo un error al almacenar los datos!'
                )
                print(bearing_form.errors)
        except IntegrityError:
            messages.error(
                request, '¡Error! Ya existe una bomba en la base de datos.'
            )
            bearing_form = BearingBaseForm(request.POST, request.FILES)
    else:
        bearing_form = BearingBaseForm()

    pumps_with_bearings = Pumps.objects.filter(
        bearings__isnull=True
    )

    motors_with_bearings = Motor.objects.filter(
        bearings__isnull=True
    )

    context = {
        'bearing_form': bearing_form,
        'pump_id': pump_id,
        'motor_id': motor_id,
        'pumps_with_bearings': pumps_with_bearings,
        'motors_with_bearings': motors_with_bearings
    }

    return render(request, template_name, context)


class AddBearingView(View):
    template_name = 'bearings/add_bearing.html'

    def get(self, request, pump_id):
        pump = get_object_or_404(Pumps, pk=pump_id)
        bearing_form = BearingForm()
        context = {'bearing_form': bearing_form, 'pump': pump}
        return render(request, self.template_name, context)

    def post(self, request, pump_id):
        pump = get_object_or_404(Pumps, pk=pump_id)
        bearing_form = BearingForm(request.POST, request.FILES)
        if bearing_form.is_valid():
            bearing = bearing_form.save()
            PumpBearing.objects.create(pump=pump, bearing=bearing)
            messages.success(
                request, '¡El rodamiento ha sido agregado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al agregar el rodamiento!')
            context = {'bearing_form': bearing_form, 'pump': pump}
            return render(request, self.template_name, context)


class ListBearings(View):
    template = 'bearings/bearings.html'

    def get(self, request):
        pump_bearings = PumpBearing.objects.all()
        motor_bearings = MotorBearing.objects.all()

        bearings_combined = list(pump_bearings) + list(motor_bearings)

        pumps_with_bearings = Pumps.objects.filter(
            bearings__isnull=True
        )

        motors_with_bearings = Motor.objects.filter(
            bearings__isnull=True
        )

        context = {
            'title': 'Rodamientos',
            'bearings_combined': bearings_combined,
            'pumps_with_bearings': pumps_with_bearings,
            'motors_with_bearings': motors_with_bearings
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
