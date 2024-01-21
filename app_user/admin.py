from django.contrib import admin
from .models import DataUser
from .models import Tasks
from .models import Observations

# Register your models here.
admin.site.register(DataUser)
admin.site.register(Tasks)
admin.site.register(Observations)
