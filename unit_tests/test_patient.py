from django.test import TestCase
from office_app.models import Patient
from django.db.models import Q

class PatientUnitTestSuite(TestCase):
    def setUp(self):
        self.azalea = Patient.objects.create(first_name='Azalea', last_name='Clive', age=25, problem='itchy nose and throat')
        self.candace = Patient.objects.create(first_name='Candace', last_name='Clement', age=45, problem='Difficulty breathing or wheezing')
        self.sharyl = Patient.objects.create(first_name='Sharyl', last_name='Charity', age=32, problem='headache')

        self.alison = Patient.objects.create(first_name='Alison', last_name='Iggy', age=17, problem='Eye irritation')

    def test_adult_patients(self):
        adult_patients_list = list(Patient.objects.filter(age__gte=18))
        self.assertEqual(adult_patients_list, [self.azalea, self.candace, self.sharyl])

    def test_teen_patients(self):
        adult_patients_list = list(Patient.objects.filter(Q(age__gte=13) & Q(age__lte=19)))
        self.assertEqual(adult_patients_list, [self.alison])

    def test_patients_with_headache(self):
        headache_patients = list(Patient.objects.filter(problem__iexact='HeaDachE'))
        self.assertEqual(headache_patients, [self.sharyl])

