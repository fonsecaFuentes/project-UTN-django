from django.shortcuts import render
from .models import Seal


# Create your views here.
def seals(request):
    seals_list = Seal.objects.all()
    context = {'title': 'Motores', 'seals_list': seals_list}
    return render(request, 'seals/seals.html', context)
