from django.shortcuts import render
from .models import Pumps


# Create your views here.
def pumps(request):
    pumps_list = Pumps.objects.all()
    context = {'title': 'Bombas', 'pumps_list': pumps_list}
    return render(request, 'pumps/pumps.html', context)
