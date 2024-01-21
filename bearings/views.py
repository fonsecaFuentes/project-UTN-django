from django.shortcuts import render
from .models import Bearing


# Create your views here.
def bearings(request):
    bearings_list = Bearing.objects.all()
    context = {'title': 'Motores', 'bearings_list': bearings_list}
    return render(request, 'bearings/bearings.html', context)
