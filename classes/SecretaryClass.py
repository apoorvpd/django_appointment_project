from classes.PhysicianClass import PhysicianClass
from classes.PatientClass import PatientClass
from office_app.models import Appointment, Patient, Physician
from datetime import datetime

class SecretaryClass:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_patient(self, first_name, last_name, age):
        patient_instance = PatientClass(first_name, last_name, age)
        return patient_instance.save_details()

    def add_doctor(self, first_name, last_name, speciality):
        physician_instance = PhysicianClass(first_name, last_name, speciality)
        return physician_instance.save_details()

    def set_appointment(self, doctor_name, patient_name, month, day, hour, minute):
        doctor_name = doctor_name.split()
        patient_name = patient_name.split()
        try:
            doctor = Physician.objects.get(first_name=doctor_name[0], last_name=doctor_name[1])
        except Physician.DoesNotExist:
            return f"Doctor with {doctor_name} doesn't exist in the system!"
        try:
            patient = Patient.objects.get(first_name=patient_name[0], last_name=patient_name[1])
        except Patient.DoesNotExist:
            return f"Patient with {patient_name} doesn't exist yet!"
        appointment_time = datetime(datetime.now().year, month, day, hour, minute, 0, 0)
        appointment = Appointment.objects.create(physician=doctor, patient=patient, appointment_time=appointment_time)
        return f"Appointment has been set for ({patient.first_name} {patient.last_name}) with Physician Dr. ({doctor.first_name} {doctor.last_name})"

    def update_doctor_info(self):
        pass

    def update_patient_info(self):
        pass

    def delete_patient(self):
        pass

    def delete_physician(self):
        pass