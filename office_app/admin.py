from django.contrib import admin
from office_app.models import Physician, Patient, Appointment, Secretary
# Register your models here.

admin.site.register(Physician)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Secretary)
