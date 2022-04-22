from django.contrib import admin
from office_app.models import Physician, Patient, Appointment
# Register your models here.

admin.site.register(Physician)
admin.site.register(Patient)
admin.site.register(Appointment)
