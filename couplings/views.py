from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Coupling


# Create your views here.
class ListCoupling(View):
    template = 'couplings/coupling.html'

    def get(self, request):
        coupling_list = Coupling.objects.all()

        context = {
            'title': 'Acoples',
            'coupling_list': coupling_list,
        }
        return render(request, self.template, context)


def coupling_detail(request, coupling_id):
    template = 'couplings/coupling_detail.html'
    coupling = get_object_or_404(Coupling, pk=coupling_id)

    context = {
        'coupling': coupling,
    }

    return render(request, template, context)
