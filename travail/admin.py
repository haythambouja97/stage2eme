from django.contrib import admin

# Register your models here.
from .models import Country
admin.site.register(Country)
from .models import Speciality
admin.site.register(Speciality)
from .models import Worker
admin.site.register(Worker)