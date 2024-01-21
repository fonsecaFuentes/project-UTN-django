from django.shortcuts import render
from .models import Coupling


# Create your views here.
def coupling(request):
    coupling_list = Coupling.objects.all()
    context = {'title': 'Acoples', 'coupling_list': coupling_list}
    return render(request, 'couplings/coupling.html', context)
