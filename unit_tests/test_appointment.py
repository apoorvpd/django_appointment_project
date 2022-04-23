from django.test import TestCase
from office_app.models import Appointment, Physician, Patient
from django.utils import timezone
from django.utils.timezone import get_current_timezone
from datetime import datetime

class AppointmentUnitTestSuite(TestCase):
    def setUp(self):
        self.nigel = Physician.objects.create(first_name='Nigel', last_name='Parris', speciality='Cardiologist')
        self.jacey = Physician.objects.create(first_name='Jacey', last_name='Kellen', speciality='Cardiologist')
        self.anna = Physician.objects.create(first_name='Annabelle', last_name='Jasper', speciality='Cardiologist')
        self.luke = Physician.objects.create(first_name='Luke', last_name='Peyton', speciality='Pediatrician')
        self.edytha = Physician.objects.create(first_name='Edytha', last_name='Melesina', speciality='Pediatrician')

        self.azalea = Patient.objects.create(first_name='Azalea', last_name='Clive', age=25,
                                             problem='itchy nose and throat')
        self.candace = Patient.objects.create(first_name='Candace', last_name='Clement', age=45,
                                              problem='Difficulty breathing or wheezing')
        self.sharyl = Patient.objects.create(first_name='Sharyl', last_name='Charity', age=32, problem='headache')
        self.alison = Patient.objects.create(first_name='Alison', last_name='Iggy', age=17, problem='Eye irritation')

        self.appointment1 = Appointment.objects.create(physician=self.luke, patient=self.alison, appointment_time=datetime(timezone.now().year,
                                                       timezone.now().month, timezone.now().day, 18, 30, 0 ,0, tzinfo=get_current_timezone()))
        self.appointment2 = Appointment.objects.create(physician=self.anna, patient=self.candace, appointment_time=datetime(timezone.now().year,
                                                       timezone.now().month, timezone.now().day, 20, 30, 0 ,0, tzinfo=get_current_timezone()))


    def test_num_appointments_with_cardiologist(self):
        appointments = list(Appointment.objects.filter(physician__speciality='Cardiologist'))
        self.assertEqual(len(appointments), 1)

    def test_num_appointments_with_pediatrician(self):
        appointments = list(Appointment.objects.filter(physician__speciality='Pediatrician'))
        self.assertEqual(len(appointments), 1)

    def test_num_morning_appointments(self):
        appointments = list(Appointment.objects.filter(appointment_time__hour__lt = 12))
        self.assertEqual(len(appointments), 0)

    def test_num_evening_appointments(self):
        appointments = list(Appointment.objects.filter(appointment_time__hour__gte = 16))
        self.assertEqual(len(appointments), 2)