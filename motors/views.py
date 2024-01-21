from django.shortcuts import render
from .models import Motor


# Create your views here.
def motors(request):
    motors_list = Motor.objects.all()
    context = {'title': 'Motores', 'motors_list': motors_list}
    return render(request, 'motors/motors.html', context)
