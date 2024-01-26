from django.shortcuts import render
from django.views.generic import View
from django.views.generic import FormView
# from .models import Consult
from .forms import ConsultForm


# Create your views here.
class Contact(FormView):
    template_name = 'contact/contact.html'
    form_class = ConsultForm
    success_url = 'message_sent'

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super().form_valid(form)


class MessageSent(View):
    template = 'contact/message_sent.html'

    def get(self, request):
        params = {}
        params['Mensaje'] = 'Mensaje'
        return render(request, self.template, params)
