from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request, 'pump_care/index.html')


def base(request):
    params = {}
    params['site_name'] = 'Pump Manager'
    return render(request, 'pump_care/base.html', params)


def nav(request):
    return render(request, 'nav.html')


def exit(request):
    logout(request)
    return redirect('home')
